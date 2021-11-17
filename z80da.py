import re
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

import timeit


#
# parameter flags:
# a: absolute address (16 bit)
# r: relative address (8 bit)
# A: absolute data (16 bit)
# D: displacement (8 bit)
# B: byte data (8 bit)
# W: word data (16 bit)
#

modules = [jump(), prefix(), load(), alu(), incdec()]
modules += [stack(), inout(), block(), bits()]
insmap = []
pc = 0
instr = ""


def inmem(addr):
    return addr in rom


def findinstr(p):

    start = timeit.timeit()
    instr = ""
    addr = "{:04X}".format(p)

    while True:
        d = "{:02X}".format(rom[p])
        p = p + 1
        if (d in ["DD", "ED", "FD"]) and (instr in "DD", "ED", "FD"):
            instr = d
        else:
            instr += d

        if len(instr) > 8:
            return False

        for i in insmap:
            m = re.match(i[0], instr)
            if m:
                v = list(m.groups())
                dis = i[2]
                l = []
                # for c in range(len(i[1])):
                for c in range(len(v)):
                    x = i[1][c]
                    if x in "aAW":
                        v[c] = v[c][2:] + v[c][:2]
                    elif x == "r":
                        v[c] = "{:04X}".format(adddsp(p, int(v[c], 16)))
                    l.append([x, v[c]])

                next = "{:04X}".format(p)
                end = timeit.timeit()
                print("time = {}", end-start)
                return {"addr": addr,
                        "next": next,
                        "instr": instr,
                        "disass": dis,
                        "pars": l}


with open("roms/PROPRIMO.rom", "rb") as f:
    d = f.read()
    rom = {c: d[c] for c in range(len(d))}

for mod in modules:
    insmap += mod.getinstr()

caddr = [0x0000]
caddr += [0x0008, 0x0010, 0x0018, 0x0020, 0x0028, 0x0030, 0x0038]
caddr += [0x0066]
disass = {}
labc = {}
labd = {}
extc = {}
extd = {}

while caddr:

    p = caddr[0]
    caddr = caddr[1:]

    if inmem(p):

        rv = findinstr(p)
        if not rv:
            break

        mnemo = rv["disass"]
        pars = rv["pars"]

        flag = ""
        if mnemo[0] in "-":
            flag = mnemo[0]
            mnemo = mnemo[1:]

        parlist = (pars[r][1] for r in range(len(pars)))
        print("({:4d}) {:4s}: {:10s}".format(
            len(caddr), rv["addr"], rv["instr"]), end="")
        print(mnemo.format(* parlist))

        disass[int(rv["addr"], 16)] = {
            "disass": rv["disass"],
            "pars": rv["pars"]
        }

        # next addresses to disassemble
        if flag != "-":
            a = int(rv["next"], 16)
            if a not in disass:
                if inmem(a):
                    caddr += [a]
                else:
                    extc[a] = ""

        for r in range(len(pars)):
            a = int(pars[r][1], 16)
            if pars[r][0].islower():
                if inmem(a):
                    if a not in disass:
                        caddr += [a]
                    labc[a] = ""
                else:
                    extc[a] = ""
            elif pars[r][0] in "A":
                if inmem(a):
                    labd[a] = ""
                else:
                    extd[a] = ""

    else:
        extc[p] = ""


print(rom[0])
print(insmap)

