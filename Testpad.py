from ATFConverter.Tokenizer import Tokenizer
from ATFConverter.ATFConverter import ATFConverter

text = r'C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt'
s = """28. a-na _1(asz) sze gur-e 5(disz) sila3 sze_\n29. _a2_ na-asz-pa-ki-im"""
Tokenizer = Tokenizer()
ATFConverter = ATFConverter()
string = Tokenizer.string_tokenizer(s)
sample = Tokenizer.line_tokenizer(text)
line = sample[304:404]
convert = ATFConverter.convert_consonant(line)

word = Tokenizer.words(convert)
sign = Tokenizer.signs(string)
number = Tokenizer.numbers(string)
determinatives = Tokenizer.determinatives(line)
sumerian = Tokenizer.sumerian(line)
sumerian_words = Tokenizer.sumerian_words(sumerian)
sumerian_sign = Tokenizer.signs(sumerian)

test = ATFConverter.convert_determinatives(determinatives)

print(line)
print(word)
print(test)

