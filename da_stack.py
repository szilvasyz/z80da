#
# Z80 pushes, pops, calls, rets
#


from da_utils import *


class stack:

    def getinstr(self):
        rv = []
        for rp in range(4):
            r = rp2name[rp]
            rx = rp2xname[rp]
            ry = rp2yname[rp]
            s = "{:02X}".format(0xC5 | (rp << 4))
            rv.append([s, "", "PUSH " + r])
            rv.append(["DD" + s, "", "PUSH " + rx])
            rv.append(["FD" + s, "", "PUSH " + ry])
            s = "{:02X}".format(0xC1 | (rp << 4))
            rv.append([s, "", "POP " + r])
            rv.append(["DD" + s, "", "POP " + rx])
            rv.append(["FD" + s, "", "POP " + ry])

        rv.append(["CD(....)", "a", "CALL {0}"])
        rv.append(["DDCD(....)", "a", "CALL {0}"])
        rv.append(["FDCD(....)", "a", "CALL {0}"])
        rv.append(["C9", "", "-RET"])
        rv.append(["DDC9", "", "-RET"])
        rv.append(["FDC9", "", "-RET"])

        rv.append(["C4(....)", "a", "CALL NZ,{0}"])
        rv.append(["DDC4(....)", "a", "CALL NZ,{0}"])
        rv.append(["FDC4(....)", "a", "CALL NZ,{0}"])
        rv.append(["CC(....)", "a", "CALL Z,{0}"])
        rv.append(["DDCC(....)", "a", "CALL Z,{0}"])
        rv.append(["FDCC(....)", "a", "CALL Z,{0}"])

        rv.append(["D4(....)", "a", "CALL NC,{0}"])
        rv.append(["DDD4(....)", "a", "CALL NC,{0}"])
        rv.append(["FDD4(....)", "a", "CALL NC,{0}"])
        rv.append(["DC(....)", "a", "CALL C,{0}"])
        rv.append(["DDDC(....)", "a", "CALL C,{0}"])
        rv.append(["FDDC(....)", "a", "CALL C,{0}"])

        rv.append(["E4(....)", "a", "CALL PO,{0}"])
        rv.append(["DDE4(....)", "a", "CALL PO,{0}"])
        rv.append(["FDE4(....)", "a", "CALL PO,{0}"])
        rv.append(["EC(....)", "a", "CALL PE,{0}"])
        rv.append(["DDEC(....)", "a", "CALL PE,{0}"])
        rv.append(["FDEC(....)", "a", "CALL PE,{0}"])

        rv.append(["F4(....)", "a", "CALL P,{0}"])
        rv.append(["DDF4(....)", "a", "CALL P,{0}"])
        rv.append(["FDF4(....)", "a", "CALL P,{0}"])
        rv.append(["FC(....)", "a", "CALL M,{0}"])
        rv.append(["DDFC(....)", "a", "CALL M,{0}"])
        rv.append(["FDFC(....)", "a", "CALL M,{0}"])

        rv.append(["C0", "", "RET NZ"])
        rv.append(["DDC0", "", "RET NZ"])
        rv.append(["FDC0", "", "RET NZ"])
        rv.append(["C8", "", "RET Z"])
        rv.append(["DDC8", "", "RET Z"])
        rv.append(["FDC8", "", "RET Z"])

        rv.append(["D0", "", "RET NC"])
        rv.append(["DDD0", "", "RET NC"])
        rv.append(["FDD0", "", "RET NC"])
        rv.append(["D8", "", "RET C"])
        rv.append(["DDD8", "", "RET C"])
        rv.append(["FDD8", "", "RET C"])

        rv.append(["E0", "", "RET PO"])
        rv.append(["DDE0", "", "RET PO"])
        rv.append(["FDE0", "", "RET PO"])
        rv.append(["E8", "", "RET PE"])
        rv.append(["DDE8", "", "RET PE"])
        rv.append(["FDE8", "", "RET PE"])

        rv.append(["F0", "", "RET P"])
        rv.append(["DDF0", "", "RET P"])
        rv.append(["FDF0", "", "RET P"])
        rv.append(["F8", "", "RET M"])
        rv.append(["DDF8", "", "RET M"])
        rv.append(["FDF8", "", "RET M"])

        for r0 in range(8):
            r = "{:02X}".format(r0 << 3)
            s = "{:02X}".format(0xC7 | (r0 << 3))
            rv.append([s, "", "RST " + r])
            rv.append(["DD" + s, "", "RST " + r])
            rv.append(["FD" + s, "", "RST " + r])

            s = "{:02X}".format(0x45 | (r0 << 3))
            rv.append(["ED" + s, "", "-RETN"])

        rv.append(["ED4D", "", "-RETI"])

        return rv

