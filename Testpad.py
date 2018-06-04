from ATFConverter.Tokenizer import Tokenizer
from ATFConverter.ATFConverter import ATFConverter
import re

Tokenizer = Tokenizer()
ATFConverter = ATFConverter(two_three=False)

"""Text feeders"""
text = r'C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt'
s = "10. _e2_ qa-t,u2-na-nim#{ki2} _gege3_ \n"
string = Tokenizer.string_tokenizer(s)
sample = Tokenizer.line_tokenizer(text)
"""Deconstructs text"""
lines = sample[0:20]
words = Tokenizer.words(lines)
signs = Tokenizer.signs(lines)
word_process = [ATFConverter.process(line) for line in signs]
breakdown = [ATFConverter.cdli_language_breakdown(line) for line in word_process]
""""Readers or Converters"""
determinatives = Tokenizer.determinatives(lines)
determinatives = ATFConverter.convert_determinatives(determinatives)
numbers = Tokenizer.numbers(lines)
sumerian = Tokenizer.sumerian(lines)
sumerian = ATFConverter.convert_sumerian(sumerian)
sumerian_words = Tokenizer.sumerian_words(sumerian)
sumerian_signs = Tokenizer.sumerian_signs(sumerian)

"""reviewer"""
output = []
for line in breakdown:
    sign = [sign[0] for sign in line]
    language = [language[1] for language in line]
    output.append(sign)
list1 = list(zip(lines, words, output, breakdown))
checker = '\n\n'.join('\n'.join(str(line) for line in x) for x in list1)
print(checker)


#print(signs)
#print(words)
#print(signs)
#print(determinatives)
#print(numbers)
#print(sumerian)
#print(sumerian_words)
#print(sumerian_signs)
#print(word_process)