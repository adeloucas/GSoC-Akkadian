from CLTK.normalizerfeeder import NaiveDecliner as AkkadianNaiveDecliner
from CLTK.stem import Stemmer as AkkadianStemmer

decliner = AkkadianNaiveDecliner()
stemmer = AkkadianStemmer()

word = "ṣīrum"
declension = decliner.decline_noun(word, 'm')
stem = stemmer.get_stem(word, 'm')

word1 = "erṣetim"
declension1 = decliner.decline_noun(word1, 'f')
stem1 = stemmer.get_stem(word1, 'f')

File = open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\Lookback.txt","w+", encoding = "utf8")
File.write('Stem [singular: nom, acc, gen; dual: nom, obl; plur: nom, obl]' + '\n')
File.write(str(stem) + r' ' + str(declension) + '\n')
File.write(str(stem1) + r' ' + str(declension1) + '\n')
File.close()