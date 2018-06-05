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
lines = sample[198:200]
words = Tokenizer.words(lines)
signs = Tokenizer.signs_for_breakdown(lines)
##input this into the function##
word_process = [ATFConverter.process(line) for line in signs]
breakdown = [ATFConverter.cdli_language_breakdown(line[1:-2]) for line in word_process]

reconstruct = ATFConverter.word_reconstruction(breakdown)
reconstructed_words = Tokenizer.words(reconstruct)

sumerian_test = ATFConverter.sumerian_reconstruct(breakdown)

""""Readers or Converters"""
determinatives = Tokenizer.determinatives(lines)
determinatives = ATFConverter.convert_determinatives(determinatives)
numbers = Tokenizer.numbers(lines)
sumerian = Tokenizer.sumerian(lines)
sumerian = ATFConverter.convert_sumerian(sumerian)
sumerian_words = Tokenizer.sumerian_words(sumerian)
sumerian_signs = Tokenizer.sumerian_signs(sumerian)
checker = ATFConverter.breakdown_reviewer(lines, breakdown, reconstructed_words, words)

print(sumerian_test)
print()
print(checker)

#print('\n'.join(reconstruct))


#print(signs)
#print(words)
#print(signs)
#print(determinatives)
#print(numbers)
#print(sumerian)
#print(sumerian_words)
#print(sumerian_signs)
#print(word_process)