__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from tests.logic import ATFConverter

class shts(unittest.TestCase):  # pylint: disable=R0904

    def test1(self):
        ATF = ATFConverter()
        text = [(r's,'), (r'S,'), (r't,'), (r'T,'), (r'sz'), (r'SZ'), (r's,a'), (r'as,-bat')]
        target = str(['ṣ', 'Ṣ', 'ṭ', 'Ṭ', 'š', 'Š', 'ṣa', 'aṣ-bat'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class signs(unittest.TestCase):  # pylint: disable=R0904

    def test2(self):
        ATF = ATFConverter()
        text = ['szi3', 'lil2', 'bi2', 't,e4', 'u3', 'aga2', 'ARAD2', 'geme2', 'sig17', 'u3 _ku3-sig17', 'ra-pi2-qi2']
        target = str(['šì', 'líl', 'bí', 'ṭe₄', 'ù', 'ága', 'áRAD', 'géme', 'sig₁₇', 'ù _kù-sig₁₇', 'ra-pí-qí'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class determinatives(unittest.TestCase):  # pylint: disable=R0904

    def test3(self):
        ATF = ATFConverter()
        text = ['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{munus}', '{še}', 
                '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'(u)', r'(diš)', r'(disz)', r'{i7}', r'{I7}']
        target = str(['ᵈ', 'ⁱʳⁱ', 'ˡᶸ²', 'ˡᶸ²', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ',
                      'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)','ⁱ⁷', 'ⁱ⁷'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class sumerian(unittest.TestCase):  # pylint: disable=R0904

    def test4(self):
        ATF = ATFConverter()
        text = [r'_a-sza3 u8 udu hi-a_', r'_sze siki i3-gesz zu2-lum_', r'_ i-yu-ti-in _', r'_ sza szu-ba-at-_', 
                r'_ szu-a-ti i-na _', r'_a-sza3 sze-gesz-i3_', r'_sipa u8 udu hi-a_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                r'_ it-ti _',r'_ma-na ku3-babbar_']
        target = str([r'_A-ŠÀ U₈ UDU HI-A_', r'_ŠE SIKI Ì-GEŠ ZÚ-LUM_', r'_ i-yu-ti-in _', r'_ ša šu-ba-at-_', 
                      r'_ šu-a-ti i-na _', r'_A-ŠÀ ŠE-GEŠ-Ì_', r'_SIPA U₈ UDU HI-A_', r'_A-ŠÀ_ be-el _', r'_ITI_ x x x _'
                      r'_ it-ti _', r'_MA-NA KÙ-BABBAR_'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()
