#
# Z80 increments/decrements
#


from da_utils import *


class incdec:

    def getinstr(self, disass=False):
        rv = []

        # incr, incrx, incry, decr, decrx, decry
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            rx = rxname[r1]
            ry = ryname[r1]
            s = "{:02X}".format(0x04 | (r1 << 3))
            rv.append([s, "", "INC " + r])
            rv.append(["DD" + s, "", "INC " + rx])
            rv.append(["FD" + s, "", "INC " + ry])

            s = "{:02X}".format(0x05 | (r1 << 3))
            rv.append([s, "", "DEC " + r])
            rv.append(["DD" + s, "", "DEC " + rx])
            rv.append(["FD" + s, "", "DEC " + ry])

        # incm, incmx, decm, decmx
        rv.append(["34", "", "INC (HL)"])
        rv.append(["DD34(..)", "D", "INC (IX+{0})"])
        rv.append(["FD34(..)", "D", "INC (IY+{0})"])
        rv.append(["35", "", "DEC (HL)"])
        rv.append(["DD35(..)", "D", "DEC (IX+{0})"])
        rv.append(["FD35(..)", "D", "DEC (IY+{0})"])

        # incrp, incrpx, incrpy
        # decrp, decrpx, decrpy
        for rp in range(4):
            r = rpname[rp]
            rx = rpxname[rp]
            ry = rpyname[rp]
            s = "{:02X}".format(0x03 | (rp << 4))
            rv.append([s, "", "INC " + r])
            rv.append(["DD" + s, "", "INC " + rx])
            rv.append(["FD" + s, "", "INC " + ry])
            s = "{:02X}".format(0x0B | (rp << 4))
            rv.append([s, "", "DEC " + r])
            rv.append(["DD" + s, "", "DEC " + rx])
            rv.append(["FD" + s, "", "DEC " + ry])

        return rv
