#
# Z80 block instructions
#


from da_utils import *


class block:

    def getinstr(self):
        rv = []

        # ldi, ldir, ldd, lddr
        # cpi, cpir, cpd, cpdr
        rv.append(["EDA0", "", "LDI"])
        rv.append(["EDA8", "", "LDD"])
        rv.append(["EDA1", "", "CPI"])
        rv.append(["EDA9", "", "CPD"])
        rv.append(["EDB0", "", "LDIR"])
        rv.append(["EDB8", "", "LDDR"])
        rv.append(["EDB1", "", "CPIR"])
        rv.append(["EDB9", "", "CPDR"])

        # ini, inir, ind, indr
        # outi, otir, outd, otdr
        rv.append(["EDA2", "", "INI"])
        rv.append(["EDAA", "", "IND"])
        rv.append(["EDA3", "", "OUTI"])
        rv.append(["EDAB", "", "OUTD"])
        rv.append(["EDB2", "", "INIR"])
        rv.append(["EDBA", "", "INDR"])
        rv.append(["EDB3", "", "OTIR"])
        rv.append(["EDBB", "", "OTDR"])

        return rv
