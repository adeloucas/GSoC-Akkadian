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
        output = ATF.convert_consonant(signs)
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
        target = ["a", "a", "a₂", "a₃", "be₂", "be₃", "bad₂", "bad₃"]

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

if __name__ == '__main__':
    unittest.main()