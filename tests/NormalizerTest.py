import unittest
from CLTK.normalizerfeeder import NaiveDecliner as AkkadianNaiveDecliner
from CLTK.stem import Stemmer as AkkadianStemmer

class test3(unittest.TestCase):  # pylint: disable=R0904

    def test_stemmer(self):
        decliner = AkkadianNaiveDecliner()
        stemmer = AkkadianStemmer()
        word = "iltum"
        declension = decliner.decline_noun(word, 'f')
        stem = stemmer.get_stem(word, 'f')
        target = ('ilt', ['iltum', 'iltam', 'iltim', 'iltān', 'iltīn', 'ilātum', 'ilātim'])

        self.assertEquals((stem, declension), target)

if __name__ == '__main__':
    unittest.main()
