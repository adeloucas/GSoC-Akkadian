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

    def test_underscore_remover(self):
        """
        Tests underscore_remover.
        """
        atf = ATFConverter()
        signs = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                  ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                  ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                  ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                  ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                  ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                  ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                  ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        target = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                   ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                   ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                   ('underscore', ''), ('space', ' '), ('akkadian', 'i'),
                   ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                   ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                   ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                   ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        output = atf.underscore_remover(signs)
        self.assertEqual(output, target)

    def test_sumerian_converter(self):
        """
        Test sumerian_converter
        """
        atf = ATFConverter()
        signs = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                  ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                  ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                  ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                  ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                  ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                  ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                  ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        target = [[('sumerian', 'U₄'), ('space', ' '), ('number', '2(diš)'),
                   ('hyphen', '-'), ('sumerian', 'KAM'), ('space', ' '),
                   ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'KAM'),
                   ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                   ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                   ('sumerian', 'É'), ('hyphen', '-'), ('sumerian', 'HI'),
                   ('hyphen', '-'), ('sumerian', 'A'), ('hyphen', '-'),
                   ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        output = atf.sumerian_converter(signs)
        self.assertEqual(output, target)

    def test_reconstruction(self):
        """
        Test reader_reconstruction.
        """
        atf = ATFConverter(two_three=False)
        text = [[('sumerian', 'a'), ('sumerian', 'šà'), ('sumerian', 'hi'),
                 ('sumerian', 'a'), ('akkadian', 'ša'), ('akkadian', 'a'),
                 ('akkadian', 'ah'), ('determinative', '{d}'),
                 ('akkadian', 'buranun'), ('akkadian', 'na'),
                 ('akkadian', 'a'), ('akkadian', 'na'), ('akkadian', 'za'),
                 ('akkadian', 'zi'), ('akkadian', 'im')],
                [('sumerian', 'a'), ('hyphen', '-'), ('sumerian', 'šà'),
                 ('hyphen', '-'), ('sumerian', 'hi'), ('hyphen', '-'),
                 ('sumerian', 'a'), ('space', ' '), ('akkadian', 'ša'),
                 ('space', ' '), ('akkadian', 'a'), ('hyphen', '-'),
                 ('akkadian', 'ah'), ('space', ' '), ('determinative', '{d}'),
                 ('akkadian', 'buranun'), ('hyphen', '-'), ('akkadian', 'na'),
                 ('space', ' '), ('akkadian', 'a'), ('hyphen', '-'),
                 ('akkadian', 'na'), ('space', ' '), ('akkadian', 'za'),
                 ('hyphen', '-'), ('akkadian', 'zi'), ('hyphen', '-'),
                 ('akkadian', 'im')]]
        target = ['ašàhiašaaah{d}buranunnaanazaziim',
                  'a-šà-hi-a ša a-ah {d}buranun-na a-na za-zi-im']
        output = atf.reader_reconstruction(text)
        self.assertEqual(output, target)


if __name__ == '__main__':
    unittest.main()
