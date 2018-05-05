
__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from tests.logic import ATFConverter

class shtsconvert(unittest.TestCase):  # pylint: disable=R0904

    def test1(self):
        ATF = ATFConverter()
        text = [(r's,'), (r'S,'), (r't,'), (r'T,'), (r'sz'), (r'SZ'), (r's,a'), (r'as,-bat')]
        target = str(['ṣ', 'Ṣ', 'ṭ', 'Ṭ', 'š', 'Š', 'ṣa', 'aṣ-bat'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class signsconvert(unittest.TestCase):  # pylint: disable=R0904

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

if __name__ == '__main__':
    unittest.main()
