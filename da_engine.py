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

    def addmem(self, addr, label, fname):
        with open(fname, "rb") as f:
            d = f.read()
            self.mem.update({addr + c: [d[c], label] for c in range(len(d))})

    def inmem(self, addr):
        return addr in self.mem

    def findinstr(self, p):

        instr = ""
        addr = "{:04X}".format(p)

        while True:
            if not self.inmem(p):
                return False
            d = "{:02X}".format(self.mem[p][0])
            p = p + 1
            if (d in ["DD", "ED", "FD"]) and (instr in "DD", "ED", "FD"):
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
                        v[c] = v[c][2:] + v[c][:2]
                    elif x == "r":
                        v[c] = "{:04X}".format(adddsp(p, int(v[c], 16)))
                    l.append([x, v[c]])

                next = "{:04X}".format(p)
                return {"addr": addr,
                        "next": next,
                        "instr": instr,
                        "disass": dis,
                        "pars": l}

    def run(self):
        while self.caddr:

            p = self.caddr[0]
            self.caddr = self.caddr[1:]

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

            self.disass[int(rv["addr"], 16)] = {
                "instr": rv["instr"],
                "next": rv["next"],
                "disass": mnemo,
                "pars": rv["pars"]
            }

            # next addresses to disassemble
            if flag != "-":
                a = int(rv["next"], 16)
                if a not in self.disass:
                    self.caddr += [a]

            # process addresses in instruction
            for r in range(len(pars)):
                a = int(pars[r][1], 16)
                if pars[r][0].islower():
                    self.labels.update({a: "code"})
                    xref = {p: "code"}
                    if a in self.xrefs:
                        self.xrefs[a].update(xref)
                    else:
                        self.xrefs[a] = xref
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
                    if a in self.xrefs:
                        self.xrefs[a].update(xref)
                    else:
                        self.xrefs[a] = xref

                    # if inmem(a):
                    #     labd[a] = ""
                    # else:
                    #     extd[a] = ""

        # else:
        #     extc[p] = ""

