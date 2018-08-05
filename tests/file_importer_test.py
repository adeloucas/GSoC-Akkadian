"""
This file tests methods in file_import.py.
"""

import unittest
import os
from Importer.file_importer import FileImport  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests FileImport class.
    """
    def test_read_file(self):
        """
        Tests read_file.
        """
        text = os.path.join('..', 'texts', 'Akkadian.txt')
        cdli = FileImport(text)
        cdli.read_file()
        final = cdli.file_lines[3042:3054]
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

    def test_file_catalog(self):
        """
        Tests file_catalog.
        """
        text = os.path.join('..', 'texts', 'two_text_no_metadata.txt')
        cdli = FileImport(text)
        cdli.file_catalog()
        final = cdli.catalog
        goal = sorted(['ARM1Akkadian.txt', 'Akkadian.txt',
                       'cdli_corpus.txt', 'single_text.txt',
                       'two_text.txt', 'two_text_abnormalities.txt',
                       'two_text_no_metadata.txt'])
        self.assertEqual(final, goal)


if __name__ == '__main__':
    unittest.main()
