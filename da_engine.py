from da_utils import *
from da_jump import jump
from da_prefix import prefix
from da_load import load
from da_alu import alu
from da_incdec import incdec
from da_stack import stack
from da_inout import inout
from da_block import block
from da_bits import bits

import re

#
# parameter flags:
# a: absolute address (16 bit)
# r: relative address (8 bit)
# A: absolute data (16 bit)
# D: displacement (8 bit)
# B: byte data (8 bit)
# W: word data (16 bit)
#


class disassembler():

    def __init__(self):
        self.insmap = []
        self.mem = {}
        self.caddr = []
        self.disass = {}
        self.labels = {}
        self.xrefs = {}
        self.resvd = {}
        self.equs = {}

        modules = [jump(), prefix(), load(), alu(), incdec()]
        modules += [stack(), inout(), block(), bits()]
        for mod in modules:
            self.insmap += mod.getinstr()

        for i in self.insmap:
            i[0] = re.compile(i[0])

    def reset(self, caddrlist):
        self.caddr = caddrlist
        self.disass = {}
        self.labels = {}
        self.xrefs = {}
        for a in caddrlist:
            self.labels.update({a: "init"})

    def clearmem(self):
        self.mem = {}

    def addmem(self, addr, section, fname):
        with open(fname, "rb") as f:
            d = f.read()
            self.mem.update({addr + c: [d[c], section] for c in range(len(d))})

    def resvmem(self, label, addr, type, length, name):
        if type == "B":
            instr = ""
            s = "DB "
            p = []
            self.labels.update({addr: label})
            for i in range(length):
                self.resvd[addr + i] = True
                s += "{{{}}},".format(i)
                p += [["B", self.mem[addr + i][0]]]
                instr += "{:02X}".format(self.mem[addr + i][0])
            self.disass.update({addr: {
                "next": addr + length,
                "instr": instr,
                "disass": s[:-1],
                "pars": p
            }})
        elif type == "W":
            instr = ""
            s = "DW "
            p = []
            self.labels.update({addr: label})
            for i in range(length):
                a = addr + 2 * i
                self.resvd[a] = True
                self.resvd[a + 1] = True
                s += "{{{}}},".format(i)
                p += [["W", mkword(self.mem[a + 1][0], self.mem[a][0])]]
                instr += "{:02X}{:02X}".format(self.mem[a][0], self.mem[a + 1][0])
            self.disass.update({addr: {
                "next": addr + 2 * length,
                "instr": instr,
                "disass": s[:-1],
                "pars": p
            }})
        elif type == "C":
            instr = ""
            s = "DW "
            p = []
            self.labels.update({addr: label})
            for i in range(length):
                a = addr + 2 * i
                # self.resvd[a] = True
                # self.resvd[a + 1] = True
                s += "{{{}}},".format(i)
                w = mkword(self.mem[a + 1][0], self.mem[a][0])
                p += [["a", w]]
                instr += "{:02X}{:02X}".format(self.mem[a][0], self.mem[a + 1][0])
                self.caddr += [w]
                self.labels.update({w: "code"})
                xref = {a: "cptr"}
                if w not in self.xrefs:
                    self.xrefs[w] = {}
                self.xrefs[w].update(xref)
            self.disass.update({addr: {
                "next": addr + 2 * length,
                "instr": instr,
                "disass": s[:-1],
                "pars": p
            }})
        elif type == "D":
            instr = ""
            s = "DW "
            p = []
            self.labels.update({addr: label})
            for i in range(length):
                a = addr + 2 * i
                self.resvd[a] = True
                self.resvd[a + 1] = True
                s += "{{{}}},".format(i)
                w = mkword(self.mem[a + 1][0], self.mem[a][0])
                p += [["a", w]]
                instr += "{:02X}{:02X}".format(self.mem[a][0], self.mem[a + 1][0])
                self.labels.update({w: "data"})
                xref = {a: "dptr"}
                if w not in self.xrefs:
                    self.xrefs[w] = {}
                self.xrefs[w].update(xref)
            self.disass.update({addr: {
                "next": addr + 2 * length,
                "instr": instr,
                "disass": s[:-1],
                "pars": p
            }})

    def inmem(self, addr):
        return addr in self.mem

    def findinstr(self, p):

        instr = ""
#        addr = "{:04X}".format(p)
        addr = p

        while True:
            if not self.inmem(p):
                return False
            d = "{:02X}".format(self.mem[p][0])
            p = p + 1
            if (d in ["DD", "ED", "FD"]) and (instr in ["DD", "ED", "FD"]):
                instr = d
            else:
                instr += d

            if len(instr) > 8:
                return False

            for i in self.insmap:
                m = re.match(i[0], instr)
                if m:
                    break

            if m:
                v = list(m.groups())
                dis = i[2]
                l = []

                for c in range(len(v)):
                    x = i[1][c]
                    if x in "aAW":
                        v[c] = mkword(int(v[c][2:], 16), int(v[c][:2], 16))
                    elif x == "r":
                        v[c] = adddsp(p, int(v[c], 16))
                    else:
                        v[c] = int(v[c], 16)

                    l.append([x, v[c]])

                next = p
                return {"addr": addr,
                        "next": next,
                        "instr": instr,
                        "disass": dis,
                        "pars": l}

    def run(self):
        while self.caddr:

            p = self.caddr[0]
            self.caddr = self.caddr[1:]

            if p == 0x1561:
                print(0)

            if p in self.resvd:
                while p in self.resvd:
                    self.disass[p] = {
                        "instr": "{:02X}".format(self.mem[p][0]),
                        "next": p + 1,
                        "disass": "DB {0}",
                        "pars": [["B", self.mem[p][0]]]
                    }
                    p = p + 1
                break

            rv = self.findinstr(p)
            if not rv:
                break

            mnemo = rv["disass"]
            pars = rv["pars"]

            flag = ""
            if mnemo[0] in "-":
                flag = mnemo[0]
                mnemo = mnemo[1:]

            # parlist = (pars[r][1] for r in range(len(pars)))
            # print("({:4d}) {:4s}: {:10s}".format(
            #     len(caddr), rv["addr"], rv["instr"]), end="")
            # print(mnemo.format(* parlist))

            self.disass[rv["addr"]] = {
                "instr": rv["instr"],
                "next": rv["next"],
                "disass": mnemo,
                "pars": rv["pars"]
            }

            # next addresses to disassemble
            if flag != "-":
                a = rv["next"]
                if a not in self.disass:
                    self.caddr += [a]

            # process addresses in instruction
            for r in range(len(pars)):
                a = pars[r][1]
                if pars[r][0].islower():
                    self.labels.update({a: "code"})
                    xref = {p: "code"}
                    if a not in self.xrefs:
                        self.xrefs[a] = {}
                    self.xrefs[a].update(xref)
                    if self.inmem(a):
                        if a not in self.disass:
                            self.caddr += [a]
                    # if inmem(a):
                    #     if a not in disass:
                    #         caddr += [a]
                    #     labc[a] = ""
                    # else:
                    #     extc[a] = ""
                elif pars[r][0] in "A":
                    self.labels.update({a: "data"})
                    xref = {p: "data"}
                    self.xrefs.update({a: xref})

                    # if inmem(a):
                    #     labd[a] = ""
                    # else:
                    #     extd[a] = ""

        # else:
        #     extc[p] = ""

