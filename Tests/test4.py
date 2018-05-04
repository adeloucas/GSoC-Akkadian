"""
Experiment 4: to see if ATF Converter can "recognize" sumerian 
"""

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import unittest
import re

class Test4(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test4(self):           

        ATFreal = [r'_a-sza3 u8 udu hi-a_', r'_sze siki i3-gesz zu2-lum_', r'_ i-yu-ti-in _', r'_ sza szu-ba-at-_', 
                   r'_ szu-a-ti i-na _', r'_a-sza3 sze-gesz-i3_', r'_sipa u8 udu hi-a_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                   r'_ it-ti _',r'_ma-na ku3-babbar_']
        goal = [r'_A-SZA3 U8 UDU HI-A_', r'_SZE SIKI I3-GESZ ZU2-LUM_', r'_ i-yu-ti-in _', r'_ SZA SZU-BA-AT-_', 
                r'_ szu-a-ti i-na _', r'_A-SZA3 SZE-GESZ-I3_', r'_SIPA U8 UDU HI-A_', r'_a-sza3_ be-el _', r'_iti_ x x x _'
                r'_ it-ti _', r'_MA-NA KU3-BABBAR_']
        CatchSumerian = [(r'[\_]\w*[\_]'),
                    (r'[\_]\w*[\s-]\w*[\_]'),
                    (r'[\_]\w*[\s-]\w*[\s-]\w*[\_]'),
                    (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                    (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                    (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),   
                    (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]')]
        CatchAkkadian = [(r'[\_][\s-]\w*[\s-][\_]'),
                    (r'[\_][\s-]\w*[\s-]\w*[\s-][\_]'),
                    (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                    (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                    (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]'),
                    (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]')]
        Sumerian = str(CatchSumerian)
        Akkadian = str(CatchAkkadian)
        string = str(ATFreal)
        
        for Sumerian in re.finditer(Sumerian, string):
            ATFreal = re.sub(Sumerian, Sumerian.upper(), string)
            ATFreal = re.sub(Akkadian, Akkadian.lower(), string)
            self.assertEqual(ATFreal, goal)

    if __name__ == '__main__':
        unittest.main()