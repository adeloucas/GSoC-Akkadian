"""
This file tests methods in cdli_import.py.
"""

import os
import unittest
from ATFConverter.cdli_import import FileImport # pylint: disable =import-error


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
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'Akkadian.txt')
        output = cdli.__read_file__(file)
        final = output[3042:3054]
        goal = ['24. _{gesz}ma2_ dan-na-tam',
                '25. a-na be-el _{gesz}ma2_',
                '26. i-na-ad-di-in',
                '@law 236',
                '27. szum-ma a-wi-lum',
                '28. _{gesz}ma2_-szu',
                '29. a-na _ma2-lah5_',
                '30. a-na ig-ri-im',
                '31. id-di-in-ma',
                '32. _ma2-lah5_ i-gi-ma',
                '33. _{gesz}ma2_ ut,-t,e4-bi',
                '34. u3 lu uh2-ta-al-li-iq']
        self.assertEqual(final, goal)

    def test_discern_texts(self):
        cdli = FileImport()
        text = \
            ["Primary publication: ARM 01, 001",
             "Author(s): Dossin, Georges",
             "&P254202 = ARM 01, 001",
             "#atf: lang akk",
             "@tablet",
             "@obverse",
             "1. a-na ia-ah-du-li-[im]",
             "2. qi2-bi2-[ma]",
             "3. um-ma a-bi-sa-mar#-[ma]",
             "Primary publication: ARM 01, 002",
             "Author(s): Dossin, Georges",
             "&P254203 = ARM 01, 002"]
        output = cdli.__discern_texts__(text)
        goal = ["&P254202 = ARM 01, 001", "&P254203 = ARM 01, 002"]
        self.assertEqual(output, goal)

    def test_split_texts(self):
        cdli = FileImport()
        text = \
            ["Primary publication: ARM 01, 001",
             "Author(s): Dossin, Georges",
             "&P254202 = ARM 01, 001",
             "#atf: lang akk",
             "@tablet",
             "@obverse",
             "1. a-na ia-ah-du-li-[im]",
             "2. qi2-bi2-[ma]",
             "3. um-ma a-bi-sa-mar#-[ma]",
             "Primary publication: ARM 01, 002",
             "Author(s): Dossin, Georges",
             "&P254203 = ARM 01, 002"]
        output = cdli.__split_texts__(text)
        goal = [[], ["Primary publication: ARM 01, 001",
                "Author(s): Dossin, Georges",
                "&P254202 = ARM 01, 001",
                "#atf: lang akk",
                "@tablet",
                "@obverse",
                "1. a-na ia-ah-du-li-[im]",
                "2. qi2-bi2-[ma]",
                "3. um-ma a-bi-sa-mar#-[ma]"],
                ["Primary publication: ARM 01, 002",
                "Author(s): Dossin, Georges",
                "&P254203 = ARM 01, 002"]]
        self.assertEqual(list(output), goal)

    def text_text_contents(self):
        cdli = FileImport()
        text = \
            ["Primary publication: ARM 01, 001",
             "Author(s): Dossin, Georges",
             "&P254202 = ARM 01, 001",
             "#atf: lang akk",
             "@tablet",
             "@obverse",
             "1. a-na ia-ah-du-li-[im]",
             "2. qi2-bi2-[ma]",
             "3. um-ma a-bi-sa-mar#-[ma]",
             "Primary publication: ARM 01, 002",
             "Author(s): Dossin, Georges",
             "&P254203 = ARM 01, 002"]
        output = cdli.text_contents(text)
        goal = {'&P254202 = ARM 01, 001':
                    ["Primary publication: ARM 01, 001",
                     "Author(s): Dossin, Georges",
                     "&P254202 = ARM 01, 001",
                     "#atf: lang akk",
                     "@tablet",
                     "@obverse",
                     "1. a-na ia-ah-du-li-[im]",
                     "2. qi2-bi2-[ma]",
                     "3. um-ma a-bi-sa-mar#-[ma]"],
                '&P254203 = ARM 01, 002':
                    ["Primary publication: ARM 01, 002",
                     "Author(s): Dossin, Georges",
                     "&P254203 = ARM 01, 002"]}
        self.assertEqual(output, goal)

if __name__ == '__main__':
    unittest.main()
