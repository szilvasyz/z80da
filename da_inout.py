#
# Z80 ins, outs
#


from da_utils import *


class inout:

    def getinstr(self):
        rv = []
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            s = "{:02X}".format(0x40 | (r1 << 3))
            rv.append(["ED" + s, "", "IN " + r + ",(C)"])
            s = "{:02X}".format(0x41 | (r1 << 3))
            rv.append(["ED" + s, "", "OUT (C)," + r])

        # ina, outa
        rv.append(["D3(..)", "B", "OUT {0},A"])
        rv.append(["DDD3(..)", "B", "OUT {0},A"])
        rv.append(["FDD3(..)", "B", "OUT {0},A"])
        rv.append(["DB(..)", "B", "IN A,{0}"])
        rv.append(["DDDB(..)", "B", "IN A,{0}"])
        rv.append(["FDDB(..)", "B", "IN A,{0}"])

        # in0c, outc0
        rv.append(["ED70", "", "IN (C)"])
        rv.append(["ED71", "", "OUT (C),0"])

        return rv

