__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.Tokenizer import Tokenizer


Tokenizer = Tokenizer()
class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_line_tokenizer(self):

        text = r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt"
        output = Tokenizer.line_tokenizer(text)
        goal = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', 
        '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', 
        '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', 
        '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', 
        '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        self.maxDiff = None
        self.assertEqual(output[3042:3054], goal)

    def test_string_tokenizer(self):
        text = '20. u2-sza-bi-la-kum\n1. a-na ia-as2-ma-ah-{d}iszkur#\n2. qi2-bi2-ma\n3. um-ma {d}utu-szi-{d}iszkur\n4. a-bu-ka-a-ma\n5. t,up-pa-[ka] sza#-[tu]-sza-bi-lam esz-me\n6. asz-szum t,e4#-em# {d}utu-illat-su2\n7. u3 ia#-szu-ub-dingir sza a-na la i-[zu]-zi-im\n'
        output = Tokenizer.string_tokenizer(text)
        goal = ['20. u2-sza-bi-la-kum', '1. a-na ia-as2-ma-ah-{d}iszkur#', '2. qi2-bi2-ma', 
        '3. um-ma {d}utu-szi-{d}iszkur', '4. a-bu-ka-a-ma', '5. t,up-pa-[ka] sza#-[tu]-sza-bi-lam esz-me', 
        '6. asz-szum t,e4#-em# {d}utu-illat-su2', '7. u3 ia#-szu-ub-dingir sza a-na la i-[zu]-zi-im']
        self.maxDiff = None
        self.assertEqual(output, goal)

    def test_words(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        output = Tokenizer.words(lines)
        goal = [['[u2?-wa?-a?-ru?]', 'at-ta', 'e2-[kal2-la-ka', '_e2_-ka', 'wu?-e?-er?]'],
                ['[...]', 'u2-ul#', 'szi#?-[...]'], ['[...]', 'x', '[...]'], ['[...]', 'x', '[...]'],
                ['u3#', 'ta-szi-ma-at#', '[...]'], ['x-x-tim', 'gesztin?', 'x', '[...]'], ['a-na', 'a-ad-da-a'],
                ['qi2-bi2-ma#'], ['um-ma', 'ia-as2-ma-ah-{d}iszkur'], ['_dumu_-ka-a-ma'],
                ['an-nu-um-ma', 'ki-ma', 'na-asz-pa-ar-ti'], ['a-[ad]-da-a', '4(u)', '_lu2', 'szu-ku6', 'mesz_']]
        self.maxDiff = None
        self.assertEqual(output, goal)

    def test_signs(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        output = Tokenizer.signs(lines)
        goal = [['u2', 'wa', 'a', 'ru', 'at', 'ta', 'e2', 'kal2', 'la', 'ka', '_e2_', 'ka', 'wu', 'e', 'er'],
                ['...', 'u2', 'ul', 'szi', '...'], ['...', 'x', '...'], ['...', 'x', '...'], ['u3', 'ta', 'szi', 'ma', 'at', '...'],
                ['x', 'x', 'tim', 'gesztin', 'x', '...'], ['a', 'na', 'a', 'ad', 'da', 'a'], ['qi2', 'bi2', 'ma'],
                ['um', 'ma', 'ia', 'as2', 'ma', 'ah', '{d}', 'iszkur'], ['_dumu_', 'ka', 'a', 'ma'],
                ['an', 'nu', 'um', 'ma', 'ki', 'ma', 'na', 'asz', 'pa', 'ar', 'ti'],
                ['a', 'ad', 'da', 'a', '4(u)', '_lu2', 'szu', 'ku6', 'mesz_']]
        self.maxDiff = None
        self.assertEqual(output, goal)

    def test_determinatives(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        output = Tokenizer.determinatives(lines)
        goal = ['{d}']
        self.maxDiff = None
        self.assertEqual(output, goal)

    def test_numbers(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        output = Tokenizer.numbers(lines)
        goal = [('4', '(u)')]
        self.maxDiff = None
        self.assertEqual(output, goal)

    def test_sumerian(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        output = Tokenizer.sumerian(lines)
        goal = ['e2', 'dumu', 'lu2 szu-ku6 mesz']
        self.assertEqual(output, goal)

    def test_sumerian_words(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        sumerian = Tokenizer.sumerian(lines)
        output = Tokenizer.sumerian_words(sumerian)
        goal = [['E2'], ['DUMU'], ['LU2', 'SZU.KU6', 'MESZ']]
        self.assertEqual(output, goal)

    def test_sumerian_signs(self):
        lines = ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n', '22. [...] u2-ul# szi#?-[...]\n', '23. [...] x [...]\n', '1. [...] x [...]\n', '2. u3# ta-szi-ma-at# [...]\n', '3. x-x-tim gesztin? x [...]\n', '1. a-na a-ad-da-a \n', '2. qi2-bi2-ma# \n', '3. um-ma ia-as2-ma-ah-{d}iszkur \n', '4. _dumu_-ka-a-ma \n', '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti \n', '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_ \n']
        sumerian = Tokenizer.sumerian(lines)
        output = Tokenizer.sumerian_signs(sumerian)
        goal = [['E2'], ['DUMU'], ['LU2', 'SZU', 'KU6', 'MESZ']]
        self.assertEqual(output, goal)

if __name__ == '__main__':
    unittest.main()