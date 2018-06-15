"""
This file tests methods in cdli_import.py.
"""

import os
import unittest
from ATFConverter.cdli_import import Import  # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_read_file(self):
        """
        Tests __read_file__.
        """
        cdli = Import()
        #file = os.path.join('texts', 'Akkadian.txt')    # broken - errno 2...
        file = \
            r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt"
        output = cdli.__read_file__(file)
        goal = ['19. [tu]-uk#-ki# a-la-ki-ia i-na ma#-[ri{ki}]',
                '20. [sze?]-mi an-ni-tam ta-asz-[pu-ra-am]',
                '21. [asz-szum sza] ta#-asz-pu-ra-am dam-qa#-[...]',
                '22. [...] i-na ma-ri{ki#}',
                '23. [...] i#-na su2-ub#-ri-im{ki}',
                '24. [... i-na sa]-ga-ra-tim{ki}',
                '25. [...] an-nu-tim',
                '@reverse',
                "1'. [...]-na",
                "2'. [_iti_] a#-ia#-ri# [...] _u4# 4(disz)#-kam_",
                "3'. _u4# 5(disz)-kam_ pa-ha#-[ar] s,a-bi#-im",
                "4'. u3 _u4 5(disz)-kam_ a-la-ak-ma"]
        self.assertEqual(output[3042:3054], goal)


if __name__ == '__main__':
    unittest.main()
