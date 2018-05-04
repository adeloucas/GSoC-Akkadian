"""
Experiment 1: See if ATF Converter replaces particular instances with special characters (ṣṢšŠṭṬ)
"""

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import unittest
import re

class Test1(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def test1(self):
        ATF = [(r's,'), (r'S,'), (r't,'), (r'T,'), (r'sz'), (r'SZ'), (r's,a'), (r'as,-bat')]
        tittles =  [(r's,', 'ṣ'),  (r'S,', 'Ṣ'), (r't,', 'ṭ'), (r'T,', 'Ṭ'), (r'sz', 'š'), (r'SZ', 'Š')]
        target = [r'ṣ', r'Ṣ', r'ṭ', r'Ṭ', r'š', r'Š', r'ṣa', r'aṣ-bat']
        goal = str(target)

        self.tittles = \
            [(re.compile(regex), repl) for (regex, repl) in tittles]
        for (pattern, repl) in self.tittles:
            ATF = re.subn(pattern, repl, str(ATF))[0]  
        
        self.assertEqual(ATF, goal)

if __name__ == '__main__':
    unittest.main()