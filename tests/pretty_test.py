"""
This file tests methods in pretty_print.py.
"""

import unittest
from ATFConverter.pretty_print import PrettyPrint  # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_underscore_remover(self):
        """
        Tests underscore_remover.
        """
        p_p = PrettyPrint()
        signs = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                  ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                  ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                  ('underscore', '_'), ('space', ' '), ('akkadian', 'i')]]
        target = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                   ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                   ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                   ('underscore', ''), ('space', ' '), ('akkadian', 'i')]]
        output = p_p.underscore_remover(signs)
        self.assertEqual(output, target)

    def test_sumerian_converter(self):
        """
        Test sumerian_converter
        """
        p_p = PrettyPrint()
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
        output = p_p.sumerian_converter(signs)
        self.assertEqual(output, target)

    def test_reconstruction(self):
        """
        Test reader_reconstruction.
        """
        p_p = PrettyPrint()
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
        output = p_p.reader_reconstruction(text)
        self.assertEqual(output, target)


if __name__ == '__main__':
    unittest.main()
