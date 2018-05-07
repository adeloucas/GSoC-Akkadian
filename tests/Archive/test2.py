"""
Experiment 2: See if ATF Converter replaces sign numbers with special characters
"""

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import unittest
import re

class Test2(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""
    def test2(self):

        ATF = ['szi3', 'lil2', 'bi2', 't,e4', 'u3', 'aga2', 'ARAD2', 'geme2', 'sig17', 'u3 _ku3-sig17', 'ra-pi2-qi2']
        target = ['szì', 'líl', 'bí', 't,e₄', 'ù', 'ága', 'áRAD', 'géme', 'sig₁₇', 'ù _kù-sig₁₇', 'ra-pí-qí']
        goal = str(target)
        
        accents =  [(r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                    (r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                    (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'á\\1'),
                    (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'à\\1'),
                    (r'[aA]'r'([a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                    (r'[aA]'r'([a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                    (r'[aA]2', 'á'), (r'[aA]3', 'à'), (r'[aA]([a-zA-Z])2', 'á\\1'), (r'[aA]([a-zA-Z])3', 'à\\1'), 
                    (r'[aA]([sStT])([zZ,])2', 'á\\1\\2'), (r'[aA]([sStT])([zZ,])3', 'à\\1\\2'),
            
                    (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                    (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                    (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'é\\1'),
                    (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'è\\1'),
                    (r'[eE]'r'([a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                    (r'[eE]'r'([a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                    (r'[eE]2', 'é'), (r'[eE]3', 'è'), (r'[eE]([a-zA-Z])2', 'é\\1'), (r'[eE]([a-zA-Z])3', 'è\\1'),
                    (r'[eE]([sStT])([zZ,])2', 'é\\1\\2'), (r'[eE]([sStT])([zZ,])3', 'è\\1\\2'),
                    
                    (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                    (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                    (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'í\\1'),
                    (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ì\\1'),
                    (r'[iI]'r'([a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                    (r'[iI]'r'([a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                    (r'[iI]2', 'í'), (r'[iI]3', 'ì'), (r'[iI]([a-zA-Z])2', 'í\\1'), (r'[iI]([a-zA-Z])3', 'ì\\1'),
                    (r'[iI]([sStT])([zZ,])2', 'í\\1\\2'), (r'[iI]([sStT])([zZ,])3', 'ì\\1\\2'),
                    
                    (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                    (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                    (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ó\\1'),
                    (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ò\\1'),
                    (r'[oO]'r'([a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                    (r'[oO]'r'([a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                    (r'[oO]2', 'ó'), (r'[oO]3', 'ò'), (r'[oO]([a-zA-Z])2', 'ó\\1'), (r'[oO]([a-zA-Z])3', 'ò\\1'),
                    (r'[oO]([sStT])([zZ,])2', 'ó\\1\\2'), (r'[oO]([sStT])([zZ,])3', 'ò\\1\\2'),
                    
                    (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                    (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                    (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ú\\1'),
                    (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ù\\1'),
                    (r'[uU]([a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                    (r'[uU]([a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                    (r'[uU]2', 'ú'), (r'[uU]3', 'ù'), (r'[uU]([a-zA-Z])2', 'ú\\1'), (r'[uU]([a-zA-Z])3', 'ù\\1'),
                    (r'[uU]([sStT])([zZ,])2', 'ú\\1\\2'), (r'[uU]([sStT])([zZ,])3', 'ù\\1\\2'),

                    (r'([a-zA-Z])4', '\\1₄'), (r'([a-zA-Z])5', '\\1₅'), (r'([a-zA-Z])6', '\\1₆'), 
                    (r'([a-zA-Z])7', '\\1₇'), (r'([a-zA-Z])8', '\\1₈'), (r'([a-zA-Z])9', '\\1₉'), 
                    (r'([a-zA-Z])10', '\\1₁₀'), (r'([a-zA-Z])11', '\\1₁₁'), (r'([a-zA-Z])12', '\\1₁₂'), 
                    (r'([a-zA-Z])13', '\\1₁₃'), (r'([a-zA-Z])14', '\\1₁₄'), (r'([a-zA-Z])15', '\\1₁₅'), 
                    (r'([a-zA-Z])16', '\\1₁₆'),(r'([a-zA-Z])17', '\\1₁₇'), (r'([a-zA-Z])18', '\\1₁₈')]

        self.accents = \
            [(re.compile(regex), repl) for (regex, repl) in accents]
        for (pattern, repl) in self.accents:
            ATF = re.subn(pattern, repl, str(ATF))[0]
            
        self.assertEqual(ATF, goal)

if __name__ == '__main__':
    unittest.main()