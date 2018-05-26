from ATFConverter.Tokenizer import Tokenizer
from ATFConverter.ATFConverter import ATFConverter

Tokenizer = Tokenizer()

text = r'C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\Akkadian.txt'
lines = Tokenizer.line_tokenizer(text)
sample = lines[1049:1060]
signs = Tokenizer.sign_tokenizer(sample)
print(sample)
print()
print(signs)