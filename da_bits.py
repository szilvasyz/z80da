#
# Z80 bit manipulations
#


from da_utils import *


class bits:

    def getinstr(self):
        rv = []

        # rlcr, rrcr, rlr, rrr
        # slar, srar, sllr, srlr
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            s = "{:02X}".format(0x00 | r1)
            rv.append(["CB" + s, "", "RLC " + r])
            s = "{:02X}".format(0x08 | r1)
            rv.append(["CB" + s, "", "RRC " + r])
            s = "{:02X}".format(0x10 | r1)
            rv.append(["CB" + s, "", "RL " + r])
            s = "{:02X}".format(0x18 | r1)
            rv.append(["CB" + s, "", "RR " + r])
            s = "{:02X}".format(0x20 | r1)
            rv.append(["CB" + s, "", "SLA " + r])
            s = "{:02X}".format(0x28 | r1)
            rv.append(["CB" + s, "", "SRA " + r])
            s = "{:02X}".format(0x30 | r1)
            rv.append(["CB" + s, "", "SLL " + r])
            s = "{:02X}".format(0x38 | r1)
            rv.append(["CB" + s, "", "SRL " + r])

        # rlcm, rrcm, rlm, rrm
        # slam, sram, sllm, srlm
        rv.append(["CB06", "", "RLC (HL)"])
        rv.append(["CB0E", "", "RRC (HL)"])
        rv.append(["CB16", "", "RL (HL)"])
        rv.append(["CB1E", "", "RR (HL)"])
        rv.append(["CB26", "", "SLA (HL)"])
        rv.append(["CB2E", "", "SRA (HL)"])
        rv.append(["CB36", "", "SLL (HL)"])
        rv.append(["CB3E", "", "SRL (HL)"])

        # bitnr, bitnm, resnr, resnm, setnr, setnm
        for r0 in range(8):
            for r1 in [0, 1, 2, 3, 4, 5, 7]:
                r = rname[r1]
                rb = "{:d}".format(r0)
                s = "{:02X}".format(0x40 | (r0 << 3) | r1)
                rv.append(["CB" + s, "", "BIT " + rb + "," + r])
                s = "{:02X}".format(0x80 | (r0 << 3) | r1)
                rv.append(["CB" + s, "", "RES " + rb + "," + r])
                s = "{:02X}".format(0xC0 | (r0 << 3) | r1)
                rv.append(["CB" + s, "", "SET " + rb + "," + r])

            s = "{:02X}".format(0x46 | (r0 << 3))
            rv.append(["CB" + s, "", "BIT " + rb + ",(HL)"])
            s = "{:02X}".format(0x86 | (r0 << 3))
            rv.append(["CB" + s, "", "RES " + rb + ",(HL)"])
            s = "{:02X}".format(0xC6 | (r0 << 3))
            rv.append(["CB" + s, "", "SET " + rb + ",(HL)"])

        # rlcmxr, rrcmxr, rlmxr, rrmxr
        # slamxr, sramxr, sllmxr, srlmxr
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            r = rname[r1]
            s = "{:02X}".format(0x00 | r1)
            rv.append(["DDCB(..)" + s, "D", "RLC (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "RLC (IY+{0})," + r])
            s = "{:02X}".format(0x08 | r1)
            rv.append(["DDCB(..)" + s, "D", "RRC (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "RRC (IY+{0})," + r])
            s = "{:02X}".format(0x10 | r1)
            rv.append(["DDCB(..)" + s, "D", "RL (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "RL (IY+{0})," + r])
            s = "{:02X}".format(0x18 | r1)
            rv.append(["DDCB(..)" + s, "D", "RR (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "RR (IY+{0})," + r])
            s = "{:02X}".format(0x20 | r1)
            rv.append(["DDCB(..)" + s, "D", "SLA (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "SLA (IY+{0})," + r])
            s = "{:02X}".format(0x28 | r1)
            rv.append(["DDCB(..)" + s, "D", "SRA (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "SRA (IY+{0})," + r])
            s = "{:02X}".format(0x30 | r1)
            rv.append(["DDCB(..)" + s, "D", "SLL (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "SLL (IY+{0})," + r])
            s = "{:02X}".format(0x38 | r1)
            rv.append(["DDCB(..)" + s, "D", "SRL (IX+{0})," + r])
            rv.append(["FDCB(..)" + s, "D", "SRL (IY+{0})," + r])

        # rlcmx, rlcmy, rrcmx, rrcmy, rlmx, rlmy, rrmx, rrmy
        # slamx, slamy, sramx, sramy, sllmx, sllmy, srlmx, srlmy
        rv.append(["DDCB(..)06", "D", "RLC (IX+{0})"])
        rv.append(["FDCB(..)06", "D", "RLC (IY+{0})"])
        rv.append(["DDCB(..)0E", "D", "RRC (IX+{0})"])
        rv.append(["FDCB(..)0E", "D", "RRC (IY+{0})"])
        rv.append(["DDCB(..)16", "D", "RL (IX+{0})"])
        rv.append(["FDCB(..)16", "D", "RL (IY+{0})"])
        rv.append(["DDCB(..)1E", "D", "RR (IX+{0})"])
        rv.append(["FDCB(..)1E", "D", "RR (IY+{0})"])
        rv.append(["DDCB(..)26", "D", "SLA (IX+{0})"])
        rv.append(["FDCB(..)26", "D", "SLA (IY+{0})"])
        rv.append(["DDCB(..)2E", "D", "SRA (IX+{0})"])
        rv.append(["FDCB(..)2E", "D", "SRA (IY+{0})"])
        rv.append(["DDCB(..)36", "D", "SLL (IX+{0})"])
        rv.append(["FDCB(..)36", "D", "SLL (IY+{0})"])
        rv.append(["DDCB(..)3E", "D", "SRL (IX+{0})"])
        rv.append(["FDCB(..)3E", "D", "SRL (IY+{0})"])

        # bitnmx, bitnmy, resnxr, resnmyr,
        # resnmx, resnmy, setnmxr, setnmyr, setnmx, setnmy
        for r0 in range(8):
            for r1 in [0, 1, 2, 3, 4, 5, 7]:
                r = rname[r1]
                rb = "{:d}".format(r0)
                s = "{:02X}".format(0x40 | (r0 << 3) | r1)
                rv.append(["DDCB(..)" + s, "D", "BIT " + rb + ",(IX+{0})," + r])
                rv.append(["FDCB(..)" + s, "D", "BIT " + rb + ",(IY+{0})," + r])
                s = "{:02X}".format(0x80 | (r0 << 3) | r1)
                rv.append(["DDCB(..)" + s, "D", "RES " + rb + ",(IX+{0})," + r])
                rv.append(["FDCB(..)" + s, "D", "RES " + rb + ",(IY+{0})," + r])
                s = "{:02X}".format(0xC0 | (r0 << 3) | r1)
                rv.append(["DDCB(..)" + s, "D", "SET " + rb + ",(IX+{0})," + r])
                rv.append(["FDCB(..)" + s, "D", "SET " + rb + ",(IY+{0})," + r])

            s = "{:02X}".format(0x46 | (r0 << 3))
            rv.append(["DDCB(..)" + s, "D", "BIT " + rb + ",(IX+{0})"])
            rv.append(["FDCB(..)" + s, "D", "BIT " + rb + ",(IY+{0})"])
            s = "{:02X}".format(0x86 | (r0 << 3))
            rv.append(["DDCB(..)" + s, "D", "RES " + rb + ",(IX+{0})"])
            rv.append(["FDCB(..)" + s, "D", "RES " + rb + ",(IY+{0})"])
            s = "{:02X}".format(0xC6 | (r0 << 3))
            rv.append(["DDCB(..)" + s, "D", "SET " + rb + ",(IX+{0})"])
            rv.append(["FDCB(..)" + s, "D", "SET " + rb + ",(IY+{0})"])

        return rv
