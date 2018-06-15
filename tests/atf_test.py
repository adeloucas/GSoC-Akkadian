"""
This file tests methods in atf_converter.py.
"""

import unittest
from ATFConverter.atf_converter import ATFConverter # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_convert_consonant(self):
        """
        Tests convert_consonant.
        """
        atf = ATFConverter()
        signs = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ']
        target = ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ']
        output = [atf.__convert_consonant__(s) for s in signs]
        self.assertEqual(output, target)

    def test_get_number_from_sign(self):
        """
        Tests get_number_from_sign.
        """
        atf = ATFConverter()
        signs = ["a", "a1", "be2", "bad3", "buru14"]
        target = [0, 1, 2, 3, 14]
        output = [atf.__get_number_from_sign__(s)[1] for s in signs]
        self.assertEqual(output, target)

    def test_single_sign(self):
        """
        Tests process with two_three as active.
        """
        atf = ATFConverter(two_three=True)
        signs = ["a", "a1", "a2", "a3", "be2", "be3", "bad2", "bad3"]
        target = ["a", "a₁", "a₂", "a₃", "be₂", "be₃", "bad₂", "bad₃"]
        output = atf.process(signs)
        self.assertEqual(output, target)

    def test_accents(self):
        """
        Tests process with two_three as inactive.
        """
        atf = ATFConverter(two_three=False)
        signs = ["a", "a2", "a3", "be2", "bad3", "buru14"]
        target = ["a", "á", "à", "bé", "bàd", "buru₁₄"]
        output = atf.process(signs)
        self.assertEqual(output, target)

    def test_unknown_token(self):
        """
        Tests process with unrecognizable tokens.
        """
        atf = ATFConverter(two_three=True)
        signs = ["a2", "☉", "be3"]
        target = ["a₂", "☉", "be₃"]
        output = atf.process(signs)
        self.assertEqual(output, target)


if __name__ == '__main__':
    unittest.main()
