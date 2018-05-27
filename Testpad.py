from ATFConverter.Tokenizer import Tokenizer
from ATFConverter.ATFConverter import ATFConverter

Tokenizer = Tokenizer()



text = r'C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\Akkadian.txt'

with open(text, mode='r+', encoding='utf8') as File:
    source = File.read()
lines = Tokenizer.line_tokenizer(text)
sample = lines[1049:1057]
words = Tokenizer.word_tokenizer(sample)
signs = Tokenizer.sign_tokenizer(sample)
determinatives = Tokenizer.determinatives_tokenizer(sample)
sumerian = Tokenizer.sumerian_tokenizer(sample)
#print(source[24304:24547])
#print()
print(lines[1049:1057])
print()
print(words)
print()
print(determinatives)
print()
print(sumerian)
