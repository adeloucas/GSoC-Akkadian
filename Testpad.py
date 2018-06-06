from ATFConverter.Tokenizer import Tokenizer
from ATFConverter.ATFConverter import ATFConverter
Tokenizer = Tokenizer()
ATFConverter = ATFConverter(two_three=False)

#Text Feeders
"""Captures text samples"""
text = r'C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\Akkadian.txt'
s = "8. _a-sza3-hi-a_ sza a-ah {d}buranun-na a-na za-zi-im \n 9. u3 a-na su2-nu-qi2-im u2-ul i-re-ed-de-e \n " \
    "10. _a-sza3-hi-a_ szi-na-ti ta-za-az tu-sa3-na-aq-ma \n"
#Line Tokenizer
"""Deconstructs Text"""
string = Tokenizer.string_tokenizer(s)
sample = Tokenizer.line_tokenizer(text)
lines = sample[0:1000]
#Word Tokenizer
"""Deconstructs Text"""
words = Tokenizer.word_tokenizer(lines)
#Sign Tokenizer
"""Deconstructs Text"""
failed_test_signs = Tokenizer.sign_tokenizer(lines)
successful_test_signs = Tokenizer.sign_tokenizer_space_and_hyphen_incl(lines)
#ATF Converter
"""Converts Text"""
failed_test_sign_process = [ATFConverter.process(line) for line in failed_test_signs]
successful_test_sign_process = [ATFConverter.process(line) for line in successful_test_signs]
#Language Reader
"""Analyzes Text"""
solo_signs = [ATFConverter.language_reader(line) for line in failed_test_sign_process]
signs_and_markers = [ATFConverter.language_reader(line[1:-2]) for line in successful_test_sign_process]
#Reader Reconstruction
"""Reconstructs Text"""
failed_test_reconstructed_lines = ATFConverter.reader_reconstruction(solo_signs)
successful_test_reconstructed_lines = ATFConverter.reader_reconstruction(signs_and_markers)
#Output
"""Tokenizes Reconstructed Text"""
reconstructed_words = Tokenizer.word_tokenizer(successful_test_reconstructed_lines)
reconstructed_signs = Tokenizer.sign_tokenizer(successful_test_reconstructed_lines)

print(lines)
print("***")
print(words)
print(failed_test_signs)
print(failed_test_sign_process)
print(solo_signs)
print(failed_test_reconstructed_lines)
print("***")
print(words)
print(successful_test_signs)
print(successful_test_sign_process)
print(signs_and_markers)
print(successful_test_reconstructed_lines)
#print(reconstructed_words)
#print(reconstructed_signs)

"""
*** Manual Input ***
sample = Tokenizer.line_tokenizer(text)
lines = sample[245:251]
*** Program ***
words = Tokenizer.word_tokenizer(lines)
signs = Tokenizer.sign_tokenizer_space_and_hyphen_incl(words)
process = [ATFConverter.process(line, line) for line in signs]
analysis = [ATFConverter.language_reader(line[1:-2]) for line in process]
lines = ATFConverter.reader_reconstruction(analysis)
words = Tokenizer.word_tokenizer(lines)
return words
"""