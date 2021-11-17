#
# Z80 load and exchange instructions
#


from da_utils import *


class load:

    def getinstr(self):
        rv = []

        # load r, r
        for r0 in [0, 1, 2, 3, 4, 5, 7]:
            for r1 in [0, 1, 2, 3, 4, 5, 7]:
                s = "{:02X}".format(0x40 | (r0 << 3) | r1)
                rv.append([s, "", "LD {},{}".format(rname[r0], rname[r1])])
                rv.append(["DD" + s, "", "LD {},{}".format(rxname[r0], rxname[r1])])
                rv.append(["FD" + s, "", "LD {},{}".format(ryname[r0], ryname[r1])])

        # load r,m; load m,r; load r,imm
        for r0 in [0, 1, 2, 3, 4, 5, 7]:
            s = "{:02X}".format(0x46 | (r0 << 3))
            r = rname[r0]
            rx = rxname[r0]
            ry = ryname[r0]
            rv.append([s, "", "LD " + r + ",(HL)"])
            rv.append(["DD" + s + "(..)", "D", "LD " + r + ",(IX+{0})"])
            rv.append(["FD" + s + "(..)", "D", "LD " + r + ",(IY+{0})"])

            s = "{:02X}".format(0x70 | r0)
            rv.append([s, "", "LD (HL)," + r])
            rv.append(["DD" + s + "(..)", "D", "LD (IX+{0})," + r])
            rv.append(["FD" + s + "(..)", "D", "LD (IY+{0})," + r])

            s = "{:02X}".format(0x06 | (r0 << 3))
            rv.append([s + "(..)", "B", "LD " + r + ",{0}"])
            rv.append(["DD" + s + "(..)", "B", "LD " + rx + ",{0}"])
            rv.append(["FD" + s + "(..)", "B", "LD " + ry + ",{0}"])

        # load m,imm; load xm,imm; load ym,imm
        rv.append(["36(..)", "B", "LD (HL),{0}"])
        rv.append(["DD36(..)(..)", "DB", "LD (IX+{0}),{1}"])
        rv.append(["FD36(..)(..)", "DB", "LD (IY+{0}),{1}"])

        # load rp,imm
        for rp in range(4):
            s = "{:02X}".format(0x01 | (rp << 4))
            r = rpname[rp]
            rx = rpxname[rp]
            ry = rpyname[rp]
            rv.append([s + "(....)", "W", "LD " + r + ",{0}"])
            rv.append(["DD" + s + "(....)", "W", "LD " + rx + ",{0}"])
            rv.append(["FD" + s + "(....)", "W", "LD " + ry + ",{0}"])

        # load (rp),a; load a,(rp)
        for rp in range(2):
            s = "{:02X}".format(0x02 | (rp << 4))
            r = rpname[rp]
            rv.append([s, "", "LD (" + r + "),A"])
            rv.append(["DD" + s, "", "LD (" + r + "),A"])
            rv.append(["FD" + s, "", "LD (" + r + "),A"])

            s = "{:02X}".format(0x0A | (rp << 4))
            rv.append([s, "", "LD A,(" + r + ")"])
            rv.append(["DD" + s, "", "LD A,(" + r + ")"])
            rv.append(["FD" + s, "", "LD A,(" + r + ")"])

        # load (ind),a; load a,(ind)
        rv.append(["32(....)", "A", "LD ({0}),A"])
        rv.append(["DD32(....)", "A", "LD ({0}),A"])
        rv.append(["FD32(....)", "A", "LD ({0}),A"])
        rv.append(["3A(....)", "A", "LD A,({0})"])
        rv.append(["DD3A(....)", "A", "LD A,({0})"])
        rv.append(["FD3A(....)", "A", "LD A,({0})"])

        # load (ind),hl; load hl,(ind)
        rv.append(["22(....)", "A", "LD ({0}),HL"])
        rv.append(["DD22(....)", "A", "LD ({0}),IX"])
        rv.append(["FD22(....)", "A", "LD ({0}),IY"])
        rv.append(["2A(....)", "A", "LD HL,({0})"])
        rv.append(["DD2A(....)", "A", "LD IX,({0})"])
        rv.append(["FD2A(....)", "A", "LD IY,({0})"])

        # load (ind),rp; load rp,(ind)
        for rp in range(4):
            s1 = "{:02X}".format(0x43 | (rp << 4))
            s2 = "{:02X}".format(0x4B | (rp << 4))
            r = rpname[rp]
            rv.append(["ED" + s1 + "(....)", "A", "LD ({0})," + r])
            rv.append(["ED" + s2 + "(....)", "A", "LD " + r + ",({0})"])

        rv.append(["F9", "", "LD SP,HL"])
        rv.append(["DDF9", "", "LD SP,IX"])
        rv.append(["FDF9", "", "LD SP,IY"])

        rv.append(["ED47", "", "LD I,A"])
        rv.append(["ED57", "", "LD A,I"])
        rv.append(["ED4F", "", "LD R,A"])
        rv.append(["ED5F", "", "LD A,R"])

        rv.append(["08", "", "EX AF,AF'"])
        rv.append(["DD08", "", "EX AF,AF'"])
        rv.append(["FD08", "", "EX AF,AF'"])
        rv.append(["D9", "", "EX AF,AF'"])
        rv.append(["DDD9", "", "EXX"])
        rv.append(["FDD9", "", "EXX"])
        rv.append(["EB", "", "EX DE,HL"])
        rv.append(["DDEB", "", "EX DE,HL"])
        rv.append(["FDEB", "", "EX DE,HL"])

        rv.append(["E3", "", "EX (SP),HL"])
        rv.append(["DDE3", "", "EX (SP),IX"])
        rv.append(["FDE3", "", "EX (SP),IY"])

        return rv
