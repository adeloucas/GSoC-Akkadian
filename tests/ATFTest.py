__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.ATFConverter import ATFConverter
from ATFConverter.Tokenizer import Tokenizer

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_convert_tittles(self):
        ATF = ATFConverter()
        signs = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ']
        target = ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ']
        output = [ATF.convert_consonant(s) for s in signs]
        self.assertEqual(output, target)

    def test_get_number_from_sign(self):
        ATF = ATFConverter()
        signs = ["a", "a1", "be2", "bad3", "buru14"]
        target = [0, 1, 2, 3, 14]

        output = [ATF.get_number_from_sign(s)[1] for s in signs]
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

    def test_determinatives(self):
        ATF = ATFConverter()
        text = ['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{munus}', '{še}',
                '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'(u)', r'(diš)', r'(disz)', r'{i7}', r'{I7}']
        target = ['ᵈ', 'ⁱʳⁱ', 'ˡᶸ²', 'ˡᶸ²', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ',
                      'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)','ⁱ⁷', 'ⁱ⁷']

        output = ATF.convert_determinatives(text)
        self.maxDiff = None
        self.assertEqual(output, target)

    def test_sumerian(self):
        ATF = ATFConverter()
        text = ['1(disz) lu2', 'lu2#-mesz dumu-mesz', '1(u)# gu2# ku3-sig17', 'dumu#-mesz', 'tug2', 'u4 1(disz)-kam', 'iti', 'iti', 'u4 3(u)-kam ba-zal', 'nar', 'lu2', 'dumu e2']
        target = ['1(DISZ) LU2', 'LU2#.MESZ DUMU.MESZ', '1(U)# GU2# KU3.SIG17', 'DUMU#.MESZ', 'TUG2', 'U4 1(DISZ).KAM', 'ITI', 'ITI', 'U4 3(U).KAM BA.ZAL', 'NAR', 'LU2', 'DUMU E2']

        output = ATF.convert_sumerian(text)
        self.assertEqual(output, target)

    def test_cdli_language_breakdown(self):
        ATF = ATFConverter(two_three=False)
        text = [['_u4', '5(disz)', 'kam_', 'i', 'na', 'ra', 'pi2', 'qi2', 'im', '{ki}'], ['um', 'ma', '_{d}', 'utu_', 'szi', '_{d}', 'iszkur_', 'a', 'bu', 'ka', 'a', 'ma'],
                ['_{lu2}', 'muhaldim', 'mesz_', 'ap', 'qi2', 'id', 'ma'],
                ['_3(u)', 'ansze', 'sze', 'gesz', 'i_', 'a', 'na', '_i3', 'ba_']]
        target = [[('u4', 'sumerian'), ('5(disz)', 'number'), ('kam', 'sumerian'), ('i', 'akkadian'),
                   ('na', 'akkadian'), ('ra', 'akkadian'), ('pi2', 'akkadian'), ('qi2', 'akkadian'), ('im', 'akkadian'),
                   ('{ki}', 'determinative')], [('um', 'akkadian'), ('ma', 'akkadian'), ('{d}', 'determinative'),
                   ('utu', 'sumerian'), ('szi', 'akkadian'), ('{d}', 'determinative'), ('iszkur', 'sumerian'),
                   ('a', 'akkadian'), ('bu', 'akkadian'), ('ka', 'akkadian'), ('a', 'akkadian'), ('ma', 'akkadian')],
                  [('{lu2}', 'determinative'), ('muhaldim', 'sumerian'), ('mesz', 'sumerian'), ('ap', 'akkadian'),
                   ('qi2', 'akkadian'), ('id', 'akkadian'), ('ma', 'akkadian')],
                  [('3(u)', 'number'), ('ansze', 'sumerian'), ('sze', 'sumerian'), ('gesz', 'sumerian'),
                   ('i', 'sumerian'), ('a', 'akkadian'), ('na', 'akkadian'), ('i3', 'sumerian'), ('ba', 'sumerian')]]

        output = [ATF.cdli_language_breakdown(line) for line in text]
        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()