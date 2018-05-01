"""
Experiment 3: to see if ATF Converter re-writes determinatives
"""

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import unittest
import re

class Test3(unittest.TestCase):  # pylint: disable=R0904
    """Class for unittest"""

    def x(self):
        ATF =  ['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{lu2}', '{i7}', '{i7}'
                '{munus}', '{še}', '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'\(u\)', r'\(diš\)', r'\(disz\)']
        
        determinatives =  [(r'{d}', 'ᵈ'), (r'{diš}', '𒁹'),(r'{disz}', '𒁹'), (r'{geš}', 'ᵍᵉˢᶻ'), (r'{gesz}', 'ᵍᵉˢᶻ'),
                           (r'{i7}', 'ⁱ7'), (r'{I7}', 'ⁱ7'), (r'{iri}', 'ⁱʳⁱ'), (r'{ki}', 'ᵏⁱ'), (r'{kuš}', 'ᵏᶸˢᶻ'), 
                           (r'{lu2}', 'ˡᶸ2'), (r'{lú}', 'ˡᶸ2'), (r'{munus}', 'ᵐᶸⁿᶸˢ'), (r'{še}', 'ˢᶻᵉ'), (r'{uzu}', 'ᶸᶻᶸ'),
                           (r'\(u\)', '(𒌋)'), (r'\(diš\)', '(𒁹)'),(r'\(disz\)', '(𒁹)'), (r'{sze}', 'ˢᶻᵉ'), (r'{kusz}', 'ᵏᶸˢᶻ')]
        target = ['ᵈ', 'ⁱʳⁱ', 'ˡᶸ2', 'ˡᶸ2', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ⁱ7', 'ⁱ7'
                  'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ', 'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)']
        self.determinatives = \
            [(re.compile(regex), repl) for (regex, repl) in determinatives]  
        for (pattern, repl) in self.determinatives:
            ATF = re.subn(pattern, repl, str(ATF))[0]
            
        self.assertEqual(ATF, target)

if __name__ == '__main__':
    unittest.main