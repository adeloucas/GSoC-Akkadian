__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.ATFConverter import ATFConverter

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_convert_tittles(self):
        ATF = ATFConverter()
        signs = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ']
        target = ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ']
        output = [ATF.__convert_consonant__(s) for s in signs]
        self.assertEqual(output, target)

    def test_get_number_from_sign(self):
        ATF = ATFConverter()
        signs = ["a", "a1", "be2", "bad3", "buru14"]
        target = [0, 1, 2, 3, 14]
        output = [ATF.__get_number_from_sign__(s)[1] for s in signs]
        self.assertEqual(output, target)

    def test_single_sign(self):
        ATF = ATFConverter(two_three=True)
        signs = ["a", "a1", "a2", "a3", "be2", "be3", "bad2", "bad3"]
        target = ["a", "a₁", "a₂", "a₃", "be₂", "be₃", "bad₂", "bad₃"]
        output = ATF.process(signs)
        self.assertEqual(output, target)

    def test_accents(self):
        ATF = ATFConverter(two_three=False)
        signs = ["a", "a2", "a3", "be2", "bad3", "buru14"]
        target = ["a", "á", "à", "bé", "bàd", "buru₁₄"]
        output = ATF.process(signs)
        self.assertEqual(output, target)

    def test_unknown_token(self):
        ATF = ATFConverter(two_three=True)
        signs = ["a2", "☉", "be3"]
        target = ["a₂", "☉", "be₃"]
        output = ATF.process(signs)
        self.assertEqual(output, target)

    def test_language_reader(self):
        ATF = ATFConverter(two_three=False)
        text = [['_u4', '5(disz)', 'kam_', 'i', 'na', 'ra', 'pi2', 'qi2', 'im', '{ki}'], ['um', 'ma', '_{d}', 'utu_',
                 'szi', '_{d}', 'iszkur_', 'a', 'bu', 'ka', 'a', 'ma'],
                ['_{lu2}', 'muhaldim', 'mesz_', 'ap', 'qi2', 'id', 'ma'],
                ['_3(u)', 'ansze', 'sze', 'gesz', 'i_', 'a', 'na', '_i3', 'ba_']]
        target = [[('sumerian', 'u4'), ('number', '5(disz)'), ('sumerian', 'kam'), ('akkadian', 'i'),
                   ('akkadian', 'na'), ('akkadian', 'ra'), ('akkadian', 'pi2'), ('akkadian', 'qi2'), ('akkadian', 'im'),
                   ('determinative', '{ki}')], [('akkadian', 'um'), ('akkadian', 'ma'), ('determinative', '{d}'),
                   ('sumerian', 'utu'), ('akkadian', 'szi'), ('determinative', '{d}'), ('sumerian', 'iszkur'),
                   ('akkadian', 'a'), ('akkadian', 'bu'), ('akkadian', 'ka'), ('akkadian', 'a'), ('akkadian', 'ma')],
                  [('determinative', '{lu2}'), ('sumerian', 'muhaldim'), ('sumerian', 'mesz'), ('akkadian', 'ap'),
                   ('akkadian', 'qi2'), ('akkadian', 'id'), ('akkadian', 'ma')], [('number', '3(u)'),
                   ('sumerian', 'ansze'), ('sumerian', 'sze'), ('sumerian', 'gesz'), ('sumerian', 'i'),
                   ('akkadian', 'a'), ('akkadian', 'na'), ('sumerian', 'i3'), ('sumerian', 'ba')]]
        output = [ATF.language_reader(line) for line in text]
        self.assertEqual(output, target)

    def test_underscore_remover(self):
        ATF = ATFConverter()
        signs = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                 ('space', ' '), ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'), ('underscore', '_'),
                 ('space', ' '), ('akkadian', 'i'), ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'), ('hyphen', '-'), ('sumerian', 'a'),
                 ('hyphen', '-'), ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        target = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                 ('space', ' '), ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'), ('underscore', ''),
                 ('space', ' '), ('akkadian', 'i'), ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'), ('hyphen', '-'), ('sumerian', 'a'),
                 ('hyphen', '-'), ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        output = ATF.underscore_remover(signs)
        self.assertEqual(output, target)

    def test_sumerian_converter(self):
        ATF = ATFConverter()
        signs = [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                 ('space', ' '), ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'), ('underscore', '_'),
                 ('space', ' '), ('akkadian', 'i'), ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'), ('hyphen', '-'), ('sumerian', 'a'),
                 ('hyphen', '-'), ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        target = [[('sumerian', 'U₄'), ('space', ' '), ('number', '2(diš)'), ('hyphen', '-'), ('sumerian', 'KAM'),
                 ('space', ' '), ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'KAM'), ('underscore', '_'),
                 ('space', ' '), ('akkadian', 'i'), ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'É'), ('hyphen', '-'), ('sumerian', 'HI'), ('hyphen', '-'), ('sumerian', 'A'),
                 ('hyphen', '-'), ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        output = ATF.sumerian_converter(signs)
        self.assertEqual(output, target)

    def test_reconstruction(self):
        ATF = ATFConverter(two_three=False)
        text = [[('sumerian', 'a'), ('sumerian', 'šà'), ('sumerian', 'hi'), ('sumerian', 'a'), ('akkadian', 'ša'),
                 ('akkadian', 'a'), ('akkadian', 'ah'), ('determinative', '{d}'), ('akkadian', 'buranun'),
                 ('akkadian', 'na'), ('akkadian', 'a'), ('akkadian', 'na'), ('akkadian', 'za'), ('akkadian', 'zi'),
                 ('akkadian', 'im')],
                [('sumerian', 'a'), ('hyphen', '-'), ('sumerian', 'šà'), ('hyphen', '-'), ('sumerian', 'hi'),
                 ('hyphen', '-'), ('sumerian', 'a'), ('space', ' '), ('akkadian', 'ša'), ('space', ' '),
                 ('akkadian', 'a'), ('hyphen', '-'), ('akkadian', 'ah'), ('space', ' '), ('determinative', '{d}'),
                 ('akkadian', 'buranun'), ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '), ('akkadian', 'a'),
                 ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '), ('akkadian', 'za'), ('hyphen', '-'),
                 ('akkadian', 'zi'), ('hyphen', '-'), ('akkadian', 'im')]]
        target = ['ašàhiašaaah{d}buranunnaanazaziim', 'a-šà-hi-a ša a-ah {d}buranun-na a-na za-zi-im']
        output = ATF.reader_reconstruction(text)
        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()