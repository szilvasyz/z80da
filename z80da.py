from da_engine import disassembler

import time


def lname(i):
    return disass.labels[i] + "_{:04X}".format(i)


disass = disassembler()
disass.addmem(0x0000, "ROM", "roms/PROPRIMO.rom")
disass.reset([0x0000, 0x0008, 0x0010, 0x0018, 0x0020, 0x0028, 0x0030, 0x0038, 0x0066])
#disass.resvmem("skip", 0x0001, "B", 1, "")
disass.resvmem("jump", 0x0134, "B", 1, "")
disass.resvmem("cptr", 0x0135, "C", 1, "")

disass.resvmem("jump", 0x0137, "B", 1, "")
disass.resvmem("cptr", 0x0138, "C", 1, "")

disass.resvmem("jump", 0x013A, "B", 1, "")
disass.resvmem("cptr", 0x013B, "C", 1, "")

disass.resvmem("jump", 0x013D, "B", 1, "")
disass.resvmem("cptr", 0x013E, "C", 1, "")

disass.resvmem("jump", 0x0140, "B", 1, "")
disass.resvmem("cptr", 0x0141, "C", 1, "")

disass.resvmem("jump", 0x0143, "B", 1, "")
disass.resvmem("cptr", 0x0144, "C", 1, "")

disass.resvmem("jump", 0x0146, "B", 1, "")
disass.resvmem("cptr", 0x0147, "C", 1, "")

disass.resvmem("jump", 0x0149, "B", 1, "")
disass.resvmem("cptr", 0x014A, "C", 1, "")

disass.resvmem("jump", 0x014C, "B", 1, "")
disass.resvmem("cptr", 0x014D, "C", 1, "")

disass.resvmem("jump", 0x014F, "B", 1, "")
disass.resvmem("cptr", 0x0150, "C", 1, "")

disass.resvmem("jump", 0x0152, "B", 1, "")
disass.resvmem("cptr", 0x0153, "C", 1, "")

disass.resvmem("jump", 0x0155, "B", 1, "")
disass.resvmem("cptr", 0x0156, "C", 1, "")

disass.resvmem("jump", 0x0158, "B", 1, "")
disass.resvmem("cptr", 0x0159, "C", 1, "")

disass.resvmem("jump", 0x015B, "B", 1, "")
disass.resvmem("cptr", 0x015C, "C", 1, "")

disass.resvmem("jump", 0x015E, "B", 1, "")
disass.resvmem("cptr", 0x015F, "C", 1, "")

disass.resvmem("jump", 0x0161, "B", 1, "")
disass.resvmem("cptr", 0x0162, "C", 1, "")

disass.resvmem("jump", 0x0164, "B", 1, "")
disass.resvmem("cptr", 0x0165, "C", 1, "")

disass.resvmem("jump", 0x0167, "B", 1, "")
disass.resvmem("cptr", 0x0168, "C", 1, "")

disass.resvmem("jump", 0x016A, "B", 1, "")
disass.resvmem("cptr", 0x016B, "C", 1, "")

disass.resvmem("dptr", 0x016D, "D", 1, "")
disass.resvmem("data", 0x016F, "B", 1, "")

disass.resvmem("skip", 0x15DD, "B", 1, "")

# disass.resvmem(0x412, 1)
# disass.resvmem(0x56D, 1)

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
        if (p[0] in "arA") and (p[1] in disass.labels):
            parlist += [lname(p[1])]
        else:
            parlist += ["{:02X}".format(p[1])]
    s = "{:04X}: {:10s} {:10s} {:s}\n".format(i, r["instr"], label, r["disass"].format(* parlist))
    fout.write(s)
    next = r["next"]

fout.close()

print(disass.mem[0])
print(disass.insmap)

