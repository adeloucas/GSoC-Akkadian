import unittest
from tests.logic import ATFConverter

class Sumeriandependent(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""
    def test1(self):
        ATF = ATFConverter()
        text = [r'_a-sza3 u8 udu hi-a_', r'_sze siki i3-gesz zu2-lum_', r'_ i-yu-ti-in _', r'_ sza szu-ba-at-_', 
                r'_ szu-a-ti i-na _', r'_a-sza3 sze-gesz-i3_', r'_sipa u8 udu hi-a_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                r'_ it-ti _',r'_ma-na ku3-babbar_']
        target = str([r'_A-šà U₈ UDU HI-A_', r'_šE SIKI ì-GEš Zú-LUM_', r'_ i-yu-ti-in _', r'_ šA šU-BA-AT-_', 
                      r'_ šu-a-ti i-na _', r'_A-šà šE-GEš-ì_', r'_SIPA U₈ UDU HI-A_', r'_a-šà_ be-el _', r'_iti_ x x x _'
                      r'_ it-ti _', r'_MA-NA Kù-BABBAR_'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()

#        CatchSumerian = [(r'[\_]\w*[\_]'),
#                         (r'[\_]\w*[\s-]\w*[\_]'),
#                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\_]'),
#                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
#                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
#                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),   
#                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]')]
#        Sumerian = str(CatchSumerian)
#        CatchAkkadian = [(r'[\_][\s-]\w*[\s-][\_]'),
#                         (r'[\_][\s-]\w*[\s-]\w*[\s-][\_]'),
#                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
#                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
#                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]'),
#                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]')]
#        Akkadian = str(CatchAkkadian)
#        string = str(ATFreal)
        
#        for Sumerian in re.finditer(Sumerian, string):
#            ATFreal = re.sub(Sumerian, Sumerian.upper(), string)
#            ATFreal = re.sub(Akkadian, Akkadian.lower(), string)
#            self.assertEqual(ATFreal, goal)
