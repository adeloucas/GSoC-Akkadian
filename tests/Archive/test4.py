import unittest
from tests.logic import ATFConverter
class Sumeriandependent(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""
    def test1(self):
        ATF = ATFConverter()
        text = ['_a-sza3 u8 udu hi-a_', r'_sze siki i3-gesz zu2-lum_', (r'_ i-yu-ti-in _'), ('_ sza szu-ba-at-_'), 
                r'_ szu-a-ti i-na _', r'_a-sza3 sze-gesz-i3_', r'_sipa u8 udu hi-a_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                r'_ it-ti _',r'_ma-na ku3-babbar_', r'_text_']
        target = str([r'_A-ŠÀ U₈ UDU HI-A_', r'_ŠE SIKI Ì-GEŠ ZÚ-LUM_', r'_ i-yu-ti-in _', r'_ ša šu-ba-at-_', 
                      r'_ šu-a-ti i-na _', r'_A-ŠÀ ŠE-GEŠ-Ì_', r'_SIPA U₈ UDU HI-A_', r'_A-ŠÀ_ be-el _', r'_ITI_ x x x _'
                      r'_ it-ti _', r'_MA-NA KÙ-BABBAR_', r'_TEXT_'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()

