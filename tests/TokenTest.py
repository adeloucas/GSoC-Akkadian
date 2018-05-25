__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.ATFConverter import ATFConverter
from ATFConverter.Tokenizer import Tokenizer

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_tokenizer(self):
        tokenize = Tokenizer()
        with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt","r+", encoding = "utf8") as File:
            text = File.readlines()
            text_selection = text[3042:3054]
            text_selection2 = text[3013:3026]
        goal = [
        ['tu', 'uk', 'ki', 'a', 'la', 'ki', 'ia', 'i', 'na', 'ma', 'ri{ki}'], 
        ['sze', 'mi', 'an', 'ni', 'tam', 'ta', 'asz', 'pu', 'ra', 'am'], 
        ['asz', 'szum', 'sza', 'ta', 'asz', 'pu', 'ra', 'am', 'dam', 'qa', '...'], 
        ['...', 'i', 'na', 'ma', 'ri{ki', '}'], 
        ['...', 'i', 'na', 'su2', 'ub', 'ri', 'im{ki}'], 
        ['...', 'i', 'na', 'sa', 'ga', 'ra', 'tim{ki}'], 
        ['...', 'an', 'nu', 'tim'], 
        #['@reverse'], 
        ['...', 'na'], 
        ['iti', 'a', 'ia', 'ri', '...', 'u4', '4(disz)', 'kam'], 
        ['u4', '5(disz)', 'kam', 'pa', 'ha', 'ar', 's,a', 'bi', 'im'], 
        ['u3', 'u4', '5(disz)', 'kam', 'a', 'la', 'ak', 'ma']
        ]
        goal2 = [
        #['Translation: \n', 
        #'UCLA Library ARK: 21198/zz001rvdz9\n', 
        #'Composite no.: \n', 
        #'Seal no.: \n', 
        #'CDLI no.: P254244\n', 
        #'Transliteration:\n', 
        #'&P254244 = ARM 01, 043\n', 
        #'#version: 0.1\n', 
        #'#atf: lang akk\n', 
        #'@tablet\n', 
        #'@obverse\n', 
        ['a', 'na', 'ia', 'as2', 'ma', 'ah', '{d}iszkur', 'qi2', 'bi2', 'ma'], 
        ['um', 'ma', '{d}utu', 'szi', '{d}iszkur', 'a', 'bu', 'ka', 'a', 'ma']
        ]
        output = tokenize.linetokenizer(text_selection)
        output2 = tokenize.linetokenizer(text_selection2)
        self.maxDiff = None
        self.assertEqual(output, goal)
        self.assertEqual(output2, goal2)
