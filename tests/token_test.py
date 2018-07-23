"""
This file tests methods in tokenizer.py.
"""

import unittest
import os
from ATFConverter.tokenizer import Tokenizer    # pylint: disable=import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'
TOKENIZER = Tokenizer(preserve_damage=False)


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_string_tokenizer(self):
        """
        Tests string_tokenizer.
        """
        text = '20. u2-sza-bi-la-kum\n1. a-na ia-as2-ma-ah-{d}iszkur#\n' \
               '2. qi2-bi2-ma\n3. um-ma {d}utu-szi-{d}iszkur\n' \
               '4. a-bu-ka-a-ma\n5. t,up-pa-[ka] sza#-[tu]-sza-bi-lam esz-me' \
               '\n' '6. asz-szum t,e4#-em# {d}utu-illat-su2\n'\
               '7. u3 ia#-szu-ub-dingir sza a-na la i-[zu]-zi-im\n'
        output = TOKENIZER.string_tokenizer(text, include_blanks=False)
        goal = ['20. u2-sza-bi-la-kum',
                '1. a-na ia-as2-ma-ah-{d}iszkur',
                '2. qi2-bi2-ma',
                '3. um-ma {d}utu-szi-{d}iszkur',
                '4. a-bu-ka-a-ma',
                '5. t,up-pa-ka sza-tu-sza-bi-lam esz-me',
                '6. asz-szum t,e4-em {d}utu-illat-su2',
                '7. u3 ia-szu-ub-dingir sza a-na la i-zu-zi-im']
        self.assertEqual(output, goal)

    def test_line_tokenizer(self):
        """
        Tests line_tokenizer.
        """
        text_file = os.path.join('..', 'texts', 'Akkadian.txt')
        output = TOKENIZER.line_tokenizer(text_file)
        goal = ['24. _{gesz}ma2_ dan-na-tam',
                '25. a-na be-el _{gesz}ma2_',
                '26. i-na-ad-di-in',
                '@law 236',
                '27. szum-ma a-wi-lum',
                '28. _{gesz}ma2_-szu',
                '29. a-na _ma2-lah5_',
                '30. a-na ig-ri-im',
                '31. id-di-in-ma',
                '32. _ma2-lah5_ i-gi-ma',
                '33. _{gesz}ma2_ ut,-t,e4-bi',
                '34. u3 lu uh2-ta-al-li-iq']
        self.assertEqual(output[3042:3054], goal)

    def test_word_tokenizer(self):
        """
        Tests word_tokenizer.
        """
        line = '21. u2-wa-a-ru at-ta e2-kal2-la-ka _e2_-ka wu-e-er'
        output = TOKENIZER.word_tokenizer(line)
        goal = [('u2-wa-a-ru', 'akkadian'), ('at-ta', 'akkadian'),
                ('e2-kal2-la-ka', 'akkadian'),
                ('_e2_-ka', 'sumerian'), ('wu-e-er', 'akkadian')]
        self.assertEqual(output, goal)

    def test_sign_tokenizer(self):
        """
        Tests sign_tokenizer.
        """
        word = ("{gisz}isz-pur-ram", "akkadian")
        output = TOKENIZER.sign_tokenizer(word)
        goal = [("gisz", "determinative"), ("isz", "akkadian"),
                ("pur", "akkadian"), ("ram", "akkadian")]
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
