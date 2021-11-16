#
# Z80 jumps and branches
#


from da_utils import *


class jump:

    def getinstr(self):
        rv = []

        # djnz, jr, jrnz, jrz, jrnc, jrc
        rv.append(["10(..)", "r", "DJNZ {0}"])
        rv.append(["DD10(..)", "r", "DJNZ {0}"])
        rv.append(["FD10(..)", "r", "DJNZ {0}"])
        rv.append(["18(..)", "r", "-JR {0}"])
        rv.append(["DD18(..)", "r", "-JR {0}"])
        rv.append(["FD18(..)", "r", "-JR {0}"])
        rv.append(["20(..)", "r", "JR NZ,{0}"])
        rv.append(["DD20(..)", "r", "JR NZ,{0}"])
        rv.append(["FD20(..)", "r", "JR NZ,{0}"])
        rv.append(["28(..)", "r", "JR Z,{0}"])
        rv.append(["DD28(..)", "r", "JR Z,{0}"])
        rv.append(["FD28(..)", "r", "JR Z,{0}"])
        rv.append(["30(..)", "r", "JR NC,{0}"])
        rv.append(["DD30(..)", "r", "JR NC,{0}"])
        rv.append(["FD30(..)", "r", "JR NC,{0}"])
        rv.append(["38(..)", "r", "JR C,{0}"])
        rv.append(["DD38(..)", "r", "JR C,{0}"])
        rv.append(["FD38(..)", "r", "JR C,{0}"])

        # jp, jphl
        rv.append(["C3(....)", "a", "-JP {0}"])
        rv.append(["DDC3(....)", "a", "-JP {0}"])
        rv.append(["FDC3(....)", "a", "-JP {0}"])
        rv.append(["E9(....)", "a", "-JP HL"])
        rv.append(["DDE9(....)", "a", "-JP HL"])
        rv.append(["FDE9(....)", "a", "-JP HL"])

        # jp, jpnz, jpz, jpnc, jpc, jppo, jppe, jpp, jpm
        rv.append(["C2(....)", "a", "JP NZ,{0}"])
        rv.append(["DDC2(....)", "a", "JP NZ,{0}"])
        rv.append(["FDC2(....)", "a", "JP NZ,{0}"])
        rv.append(["CA(....)", "a", "JP Z,{0}"])
        rv.append(["DDCA(....)", "a", "JP Z,{0}"])
        rv.append(["FDCA(....)", "a", "JP Z,{0}"])
        rv.append(["D2(....)", "a", "JP NC,{0}"])
        rv.append(["DDD2(....)", "a", "JP NC,{0}"])
        rv.append(["FDD2(....)", "a", "JP NC,{0}"])
        rv.append(["DA(....)", "a", "JP C,{0}"])
        rv.append(["DDDA(....)", "a", "JP C,{0}"])
        rv.append(["FDDA(....)", "a", "JP C,{0}"])
        rv.append(["E2(....)", "a", "JP PO,{0}"])
        rv.append(["DDE2(....)", "a", "JP PO,{0}"])
        rv.append(["FDE2(....)", "a", "JP PO,{0}"])
        rv.append(["EA(....)", "a", "JP PE,{0}"])
        rv.append(["DDEA(....)", "a", "JP PE,{0}"])
        rv.append(["FDEA(....)", "a", "JP PE,{0}"])
        rv.append(["F2(....)", "a", "JP P,{0}"])
        rv.append(["DDF2(....)", "a", "JP P,{0}"])
        rv.append(["FDF2(....)", "a", "JP P,{0}"])
        rv.append(["FA(....)", "a", "JP M,{0}"])
        rv.append(["DDFA(....)", "a", "JP M,{0}"])
        rv.append(["FDFA(....)", "a", "JP M,{0}"])

        return rv
