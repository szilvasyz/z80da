#
# Z80 instruction prefixes and control instructions
#

from da_utils import *


class prefix:

    def getinstr(self):
        rv = [

            # NOP instruction
            ["00", "", "NOP"],
            ["DD00", "", "NOP"],
            ["FD00", "", "NOP"],

            # HALT instruction
            ["76", "", "-HALT"],
            ["DD76", "", "-HALT"],
            ["FD76", "", "-HALT"],

            # set/complement carry flag
            ["37", "", "SCF"],
            ["DD37", "", "SCF"],
            ["FD37", "", "SCF"],
            ["3F", "", "CCF"],
            ["DD3F", "", "CCF"],
            ["FD3F", "", "CCF"],

            # enable/disable interrupts
            ["F3", "", "DI"],
            ["DDF3", "", "DI"],
            ["FDF3", "", "DI"],
            ["FB", "", "EI"],
            ["DDFB", "", "EI"],
            ["FDFB", "", "EI"],

            # set interrupt modes
            ["ED46", "", "IM 0"],
            ["ED66", "", "IM 0"],
            ["ED4E", "", "IM 0"],
            ["ED6E", "", "IM 0"],
            ["ED56", "", "IM 1"],
            ["ED76", "", "IM 1"],
            ["ED5E", "", "IM 1"],
            ["ED7E", "", "IM 1"]

            # prefixes
        ]

        # extended instruction table
        rv.append(["ED77", "", "NOP"])
        rv.append(["ED7F", "", "NOP"])

        for c in list(range(0x00, 0x40)) + list(range(0x80, 0xA0)) + list(range(0xC0, 0x100)):
            rv.append(["ED{:02X}".format(c), "", "NOP"])

        for c in list(range(0x04, 0x08)) + list(range(0x0c, 0x10)):
            rv.append(["ED{:02X}".format(0xA0 + c), "", "NOP"])
            rv.append(["ED{:02X}".format(0xB0 + c), "", "NOP"])

        return rv
