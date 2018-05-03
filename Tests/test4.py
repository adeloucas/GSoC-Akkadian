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

        ATF = [r'_test_']
        goal = [r'_TEST_']
        Sumerian = [(r'[\_]\w*[\_]')]#,
                    #(r'[\_]\w*[\s-]\w*[\_]'),
                    #(r'[\_]\w*[\s-]\w*[\s-]\w*[\_]'),
                    #(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                    #(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                    #(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                    #(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]')]
                    
        target = str(Sumerian)
        string = str(ATF)
        
        for target in re.finditer(target, string):
            ATF = re.sub(target, target.upper(), string)
            self.assertEqual(ATF, goal)

    if __name__ == '__main__':
        unittest.main()