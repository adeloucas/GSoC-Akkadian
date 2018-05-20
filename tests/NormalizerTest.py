__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.ATFConverter import ATFConverter
from CLTK.declension import NaiveDecliner

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test1(self):
        ATF = ATFConverter()
        text = [(r's,')]
        target = str(['ṣ'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()
