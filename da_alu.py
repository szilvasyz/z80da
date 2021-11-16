#
# Z80 arithmetic and logic instructions
#


from da_utils import *


class alu:

    def getinstr(self):
        rv = []

        # addai, adcai, subai, sbcai
        rv.append(["C6(..)", "B", "ADD A,{0}"])
        rv.append(["DDC6(..)", "B", "ADD A,{0}"])
        rv.append(["FDC6(..)", "B", "ADD A,{0}"])
        rv.append(["CE(..)", "B", "ADC A,{0}"])
        rv.append(["DDCE(..)", "B", "ADC A,{0}"])
        rv.append(["FDCE(..)", "B", "ADC A,{0}"])
        rv.append(["D6(..)", "B", "SUB A,{0}"])
        rv.append(["DDD6(..)", "B", "SUB A,{0}"])
        rv.append(["FDD6(..)", "B", "SUB A,{0}"])
        rv.append(["DE(..)", "B", "SBC A,{0}"])
        rv.append(["DDDE(..)", "B", "SBC A,{0}"])
        rv.append(["FDDE(..)", "B", "SBC A,{0}"])

        # andai, xorai, orai, cpai
        rv.append(["E6(..)", "B", "AND {0}"])
        rv.append(["DDE6(..)", "B", "AND {0}"])
        rv.append(["FDE6(..)", "B", "AND {0}"])
        rv.append(["EE(..)", "B", "XOR {0}"])
        rv.append(["DDEE(..)", "B", "XOR {0}"])
        rv.append(["FDEE(..)", "B", "XOR {0}"])
        rv.append(["F6(..)", "B", "OR {0}"])
        rv.append(["DDF6(..)", "B", "OR {0}"])
        rv.append(["FDF6(..)", "B", "OR {0}"])
        rv.append(["FE(..)", "B", "CP {0}"])
        rv.append(["DDFE(..)", "B", "CP {0}"])
        rv.append(["FDFE(..)", "B", "CP {0}"])

        # addar, adcar, subar, sbcar
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            rx = rxname[r1]
            ry = ryname[r1]
            s = "{:02X}".format(0x80 | r1)
            rv.append([s, "", "ADD A," + r])
            rv.append(["DD" + s, "", "ADD A," + rx])
            rv.append(["FD" + s, "", "ADD A," + ry])

            s = "{:02X}".format(0x88 | r1)
            rv.append([s, "", "ADC A," + r])
            rv.append(["DD" + s, "", "ADC A," + rx])
            rv.append(["FD" + s, "", "ADC A," + ry])

            s = "{:02X}".format(0x90 | r1)
            rv.append([s, "", "SUB A," + r])
            rv.append(["DD" + s, "", "SUB A," + rx])
            rv.append(["FD" + s, "", "SUB A," + ry])

            s = "{:02X}".format(0x98 | r1)
            rv.append([s, "", "SBC A," + r])
            rv.append(["DD" + s, "", "SBC A," + rx])
            rv.append(["FD" + s, "", "SBC A," + ry])

        # andar, xorar, orar, cpar
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            rx = rxname[r1]
            ry = ryname[r1]
            s = "{:02X}".format(0xA0 | r1)
            rv.append([s, "", "AND " + r])
            rv.append(["DD" + s, "", "AND " + rx])
            rv.append(["FD" + s, "", "AND " + ry])

            s = "{:02X}".format(0xA8 | r1)
            rv.append([s, "", "XOR " + r])
            rv.append(["DD" + s, "", "XOR " + rx])
            rv.append(["FD" + s, "", "XOR " + ry])

            s = "{:02X}".format(0xB0 | r1)
            rv.append([s, "", "OR " + r])
            rv.append(["DD" + s, "", "OR " + rx])
            rv.append(["FD" + s, "", "OR " + ry])

            s = "{:02X}".format(0xB8 | r1)
            rv.append([s, "", "CP " + r])
            rv.append(["DD" + s, "", "CP " + rx])
            rv.append(["FD" + s, "", "CP " + ry])

        # addam, addamx, addamy, adcam, adcamx, adcamy
        # subam, subamx, subamy, sbcam, sbcamx, sbcamy
        rv.append(["86", "", "ADD A,(HL)"])
        rv.append(["DD86(..)", "D", "ADD A,(IX+{0})"])
        rv.append(["FD86(..)", "D", "ADD A,(IY+{0})"])
        rv.append(["8E", "", "ADC A,(HL)"])
        rv.append(["DD8E(..)", "D", "ADC A,(IX+{0})"])
        rv.append(["FD8E(..)", "D", "ADC A,(IY+{0})"])
        rv.append(["96", "", "SUB A,(HL)"])
        rv.append(["DD96(..)", "D", "SUB A,(IX+{0})"])
        rv.append(["FD96(..)", "D", "SUB A,(IY+{0})"])
        rv.append(["9E", "", "SBC A,(HL)"])
        rv.append(["DD9E(..)", "D", "SBC A,(IX+{0})"])
        rv.append(["FD9E(..)", "D", "SBC A,(IY+{0})"])

        # andam, andamx, andamy, xoram, xoramx, xoramy
        # oram, oramx, oramy, cpam, cpamx, cpamy
        rv.append(["A6", "", "AND (HL)"])
        rv.append(["DDA6(..)", "D", "AND (IX+{0})"])
        rv.append(["FDA6(..)", "D", "AND (IY+{0})"])
        rv.append(["AE", "", "XOR (HL)"])
        rv.append(["DDAE(..)", "D", "XOR (IX+{0})"])
        rv.append(["FDAE(..)", "D", "XOR (IY+{0})"])
        rv.append(["B6", "", "OR (HL)"])
        rv.append(["DDB6(..)", "D", "OR (IX+{0})"])
        rv.append(["FDB6(..)", "D", "OR (IY+{0})"])
        rv.append(["BE", "", "CP (HL)"])
        rv.append(["DDBE(..)", "D", "CP (IX+{0})"])
        rv.append(["FDBE(..)", "D", "CP (IY+{0})"])

        # addrp, addrpx, addrpy, adcrp, sbcrp
        # nega
        for rp in range(4):
            r = rpname[rp]
            rx = rpxname[rp]
            ry = rpyname[rp]
            s = "{:02X}".format(0x09 | (rp << 4))
            rv.append([s, "", "ADD HL," + r])
            rv.append(["DD" + s, "", "ADD IX," + rx])
            rv.append(["FD" + s, "", "ADD IY," + ry])

            s = "{:02X}".format(0x4A | (rp << 4))
            rv.append(["ED" + s, "", "ADC HL," + r])
            s = "{:02X}".format(0x42 | (rp << 4))
            rv.append(["ED" + s, "", "SBC HL," + r])
            s = "{:02X}".format(0x44 | (rp << 4))
            rv.append(["ED" + s, "", "NEG A"])
            s = "{:02X}".format(0x4C | (rp << 4))
            rv.append(["ED" + s, "", "NEG A"])

        # daa, cpla, rla, rra, rlca, rrca
        rv.append(["27", "", "DAA"])
        rv.append(["DD27", "", "DAA"])
        rv.append(["FD27", "", "DAA"])
        rv.append(["2F", "", "CPLA"])
        rv.append(["DD2F", "", "CPLA"])
        rv.append(["FD2F", "", "CPLA"])
        rv.append(["17", "", "RLA"])
        rv.append(["DD17", "", "RLA"])
        rv.append(["FD17", "", "RLA"])
        rv.append(["07", "", "RLCA"])
        rv.append(["DD07", "", "RLCA"])
        rv.append(["FD07", "", "RLCA"])
        rv.append(["1F", "", "RRA"])
        rv.append(["DD1F", "", "RRA"])
        rv.append(["FD1F", "", "RRA"])
        rv.append(["0F", "", "RRCA"])
        rv.append(["DD0F", "", "RRCA"])
        rv.append(["FD0F", "", "RRCA"])

        # rrd, rld
        rv.append(["ED67", "", "RRD"])
        rv.append(["ED6F", "", "RLD"])

        return rv
