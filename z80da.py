from da_engine import disassembler

import time


def lname(i):
    return disass.labels[i] + "_{:04X}".format(i)


disass = disassembler()
disass.addmem(0x0000, "ROM", "roms/PROPRIMO.rom")
disass.reset([0x0000, 0x0008, 0x0010, 0x0018, 0x0020, 0x0028, 0x0030, 0x0038, 0x0066])
disass.resvmem(0x15DD, 1)
# disass.resvmem(0x412, 1)

print(disass.findinstr(0))
disass.run()
print("Disassembling done.")

fout = open("disass.lst", "w")

next = False
for i in sorted(disass.disass):
    if next:
        if next != i:
            fout.write(";...\n")

    if i in disass.xrefs:
        n = 0
        for k in disass.xrefs[i]:
            if n == 0:
                fout.write("\n; xref: ")
            fout.write("{:04X}({:s}) ".format(k, disass.xrefs[i][k]))
            n += 1
            if n == 5:
                n = 0
        fout.write("\n;\n")

    if i in disass.labels:
        label = lname(i)
    else:
        label = ""

    r = disass.disass[i]
#    parlist = (r["pars"][p][1] for p in range(len(r["pars"])))
    parlist = []
    for p in r["pars"]:
        if (p[0] in "arA") and (int(p[1], 16) in disass.labels):
            parlist += [lname(int(p[1], 16))]
        else:
            parlist += [p[1]]
    s = "{:04X}: {:10s} {:10s} {:s}\n".format(i, r["instr"], label, r["disass"].format(* parlist))
    fout.write(s)
    next = int(r["next"], 16)

fout.close()

print(disass.mem[0])
print(disass.insmap)

