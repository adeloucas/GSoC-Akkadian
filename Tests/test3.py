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
    def test3(self):

        ATF =  ['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{i7}', '{i7}',
                '{munus}', '{še}', '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'(u)', r'(diš)', r'(disz)']
        target = ['ᵈ', 'ⁱʳⁱ', 'ˡᶸ²', 'ˡᶸ²', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ⁱ⁷', 'ⁱ⁷',
                  'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ', 'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)']
        goal = str(target)

        determinatives =  [(r'{d}', 'ᵈ'), (r'{diš}', '𒁹'),(r'{disz}', '𒁹'), (r'{geš}', 'ᵍᵉˢᶻ'), (r'{gesz}', 'ᵍᵉˢᶻ'),
                           (r'{i7}', 'ⁱ⁷'), (r'{I7}', 'ⁱ⁷'), (r'{iri}', 'ⁱʳⁱ'), (r'{ki}', 'ᵏⁱ'), (r'{kuš}', 'ᵏᶸˢᶻ'), 
                           (r'{lu2}', 'ˡᶸ²'), (r'{lú}', 'ˡᶸ²'), (r'{munus}', 'ᵐᶸⁿᶸˢ'), (r'{še}', 'ˢᶻᵉ'), (r'{uzu}', 'ᶸᶻᶸ'),
                           (r'\(u\)', '(𒌋)'), (r'\(diš\)', '(𒁹)'),(r'\(disz\)', '(𒁹)'), (r'{sze}', 'ˢᶻᵉ'), 
                           (r'{kusz}', 'ᵏᶸˢᶻ'),  (r'{ansze}', 'ᵃⁿˢᶻᵉ'),  (r'{esz2}', 'ᵉˢᶻ²'),  (r'{gi}', 'ᵍⁱ'),
                            (r'{is}', 'ⁱˢ'),  (r'{nisi}', 'ⁿⁱˢⁱ'),  (r'{uruda}', 'ᵘʳᵘᵈᵃ')]

        self.determinatives = \
            [(re.compile(regex), repl) for (regex, repl) in determinatives]  
        for (pattern, repl) in self.determinatives:
            ATF = re.subn(pattern, repl, str(ATF))[0]
            
        self.assertEqual(ATF, goal)

if __name__ == '__main__':
    unittest.main()