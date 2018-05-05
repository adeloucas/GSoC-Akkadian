import os
import unittest
import re

class Sumeriancontained(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test1(self):           

        ATF = str([r'_a-sza3 u8 udu hi-a_', r'_sze siki i3-gesz zu2-lum_', r'_ i-yu-ti-in _', r'_ sza szu-ba-at-_', 
                   r'_ szu-a-ti i-na _', r'_a-sza3 sze-gesz-i3_', r'_sipa u8 udu hi-a_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                   r'_ it-ti _',r'_ma-na ku3-babbar_'])
        goal = [r'_A-SZA3 U8 UDU HI-A_', r'_SZE SIKI I3-GESZ ZU2-LUM_', r'_ i-yu-ti-in _', r'_ SZA SZU-BA-AT-_', 
                r'_ szu-a-ti i-na _', r'_A-SZA3 SZE-GESZ-I3_', r'_SIPA U8 UDU HI-A_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                r'_ it-ti _', r'_MA-NA KU3-BABBAR_']
        Sumerian = str([(r'[\_]\w*[\_]'),
                        (r'[\_]\w*[\s-]\w*[\_]'),
                        (r'[\_]\w*[\s-]\w*[\s-]\w*[\_]'),
                        (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                        (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                        (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),   
                        (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]')])
        # captures instances where akkadian is caught in above.
        Akkadian = str([(r'[\_][\s-]\w*[\s-][\_]'),
                        (r'[\_][\s-]\w*[\s-]\w*[\s-][\_]'),
                        (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                        (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                        (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]'),
                        (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]')])
#        Sumerian = str(CatchSumerian)
#        Akkadian = str(CatchAkkadian)
        
        for Sumerian in re.finditer(Sumerian, ATF):
            ATF = re.sub(Sumerian, Sumerian.upper(), ATF)
            ATF = re.sub(Akkadian, Akkadian.lower(), ATF)
            self.assertEqual(ATF, goal)

    if __name__ == '__main__':
        unittest.main()