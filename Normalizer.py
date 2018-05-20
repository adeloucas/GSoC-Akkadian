from CLTK.declension import NaiveDecliner as AkkadianNaiveDecliner

decliner = AkkadianNaiveDecliner()
word = "ṣīrum"
declension = decliner.decline_noun(word, 'f')

File = open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\Lookback.txt","w+", encoding = "utf8")
File.write(str(declension))
File.write('\n')
File.close()