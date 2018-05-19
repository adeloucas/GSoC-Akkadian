import unittest

from Normalizer.Willis_Akkadian.bound_form import BoundForm as AkkadianBoundForm
from Normalizer.Willis_Akkadian.cv_pattern import CVPattern as AkkadianCVPattern
from Normalizer.Willis_Akkadian.declension import NaiveDecliner as AkkadianNaiveDecliner
from Normalizer.Willis_Akkadian.stem import Stemmer as AkkadianStemmer
from Normalizer.Willis_Akkadian.syllabifier import Syllabifier as AkkadianSyllabifier

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_akkadian_bound_form(self):
        """Test Akkadian bound form method"""
        bound_former = AkkadianBoundForm()
        word = "awīlum"
        bound_form = bound_former.get_bound_form(word, 'm')
        target = "awīl"
        self.assertEquals(bound_form, target)

    def test_akkadian_cv_pattern(self):
        """Test Akkadian CV pattern method"""
        cv_patterner = AkkadianCVPattern()
        word = "iparras"
        cv_pattern = cv_patterner.get_cv_pattern(word, pprint=True)
        target = "V₁C₁V₂C₂C₂V₂C₃"
        self.assertEquals(cv_pattern, target)

    def test_akkadian_declension(self):
        """Test Akkadian noun declension"""
        decliner = AkkadianNaiveDecliner()
        word = "iltum"
        declension = decliner.decline_noun(word, 'f')
        target = [('iltim', {'case': 'genitive', 'number': 'singular'}),
                  ('iltum', {'case': 'nominative', 'number': 'singular'}),
                  ('iltam', {'case': 'accusative', 'number': 'singular'}),
                  ('iltīn', {'case': 'oblique', 'number': 'dual'}),
                  ('iltān', {'case': 'nominative', 'number': 'dual'}),
                  ('ilātim', {'case': 'oblique', 'number': 'plural'}),
                  ('ilātum', {'case': 'nominative', 'number': 'plural'})]
        self.assertEquals(sorted(declension), sorted(target))

    def test_akkadian_stemmer(self):
        """Test Akkadian stemmer"""
        stemmer = AkkadianStemmer()
        word = "šarrū"
        stem = stemmer.get_stem(word, 'm')
        target = "šarr"
        self.assertEquals(stem, target)

    def test_akkadian_syllabifier(self):
        """Test Akkadian syllabifier"""
        syllabifier = AkkadianSyllabifier()
        word = "epištašu"
        syllables = syllabifier.syllabify(word)
        target = ['e','piš','ta','šu']
        self.assertEqual(syllables, target)

if __name__ == '__main__':
    unittest.main()