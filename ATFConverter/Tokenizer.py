import os
import re
from unicodedata import normalize
import nltk
from nltk.tokenize import RegexpTokenizer

class Tokenizer(object):

    def line_tokenizer(self, text):
        """
        Takes .txt file, reads it, separates lines, and prints only line numbered lines as list of strings (ignores metadata).
        Text must be a string.
        """
        line_output = []

        with open(text, mode='r+', encoding='utf8') as File:
            lines = File.readlines()
            assert isinstance(text, str), 'Incoming argument must be a string.'
            for no_metadata in lines:
                if re.match(r'^\d*\.|\d\'\.', no_metadata):
                    line_output.append(no_metadata)
            return line_output

    def string_tokenizer(self: object, untokenized_string: str, include_blanks=False):
        """This is CLTK's line tokenizer. It works just fine for strings."""
        assert isinstance(untokenized_string, str), 'Incoming argument must be a string.'
        if include_blanks:
            tokenized_lines = untokenized_string.splitlines()
        else:
            tokenized_lines = [line for line in untokenized_string.splitlines() if line != r'\\n']
        return tokenized_lines

    def word_tokenizer(self, line_tokenizer):
        """Looks at strings in list and breaks down lines by words, includes all special characters"""
        word_output = []
        word_tokenizer = RegexpTokenizer(r'[\s]|^\d*\.|\d\'\.', gaps=True)

        for words in line_tokenizer:
            word_output.append(word_tokenizer.tokenize(words))
        return word_output

    def sign_tokenizer(self, line_tokenizer):
        """Utilizes RegexpTokenizer to return sign breakdown of lines in text"""
        sign_output = []
        sign_tokenizer = RegexpTokenizer(r'[\s\-\_\#\!\?\[\]\{\}\(\)]|^\d*\.|\d\'\.', gaps=True)
        for signs in line_tokenizer:
            sign_output.append(sign_tokenizer.tokenize(str(signs)))
        return sign_output

    def determinatives_tokenizer(self, line_tokenizer):
        """Returns determinatives"""
        determinatives_output = []
        determinatives = re.compile(r'{\w*}')
        for sign in determinatives.finditer(str(line_tokenizer)):
            determinatives_output.append(sign.group())
        return determinatives_output

    def numbers_and_number_signs_tokenizer(self, line_tokenizer):
        """Returns numbers and number signs affiliated with said numbers"""
        numbers_output = []
        number_signs_output = []
        zipped_output = []
        number_signs = re.compile(r'\(\w*\)')
        numbers = re.compile(r'\d\/\d|\d\(|\d\s\(')
        for sign in numbers.finditer(str(line_tokenizer)):
            numbers_output.append(sign.group())
            numbers_output = map(lambda each: each.strip(r'\('), numbers_output)
        for sign in number_signs.finditer(str(line_tokenizer)):
            number_signs_output.append(sign.group())
        zipped_output = list(zip(numbers_output, number_signs_output))
        return zipped_output

    def sumerian_tokenizer(self, line_tokenizer):
        """Captures Sumerian in lines"""
        sumerian_output = []
        sumerian = re.compile(r'(?<=\_).*?(?=\_)')
        akkadian = re.compile(r'(?<=[^\s]\_).*?(?=\_)')
        for sign in sumerian.finditer(str(line_tokenizer)):
            sumerian_output.append(sign.group())
        for sign in akkadian.finditer(str(line_tokenizer)):
            sumerian_output.remove(sign.group())
        #sumerian_output = str(sumerian_output).upper() #to go in ATFConverter
        #sumerian_output = re.subn('-', '.', str(sumerian_output)) #to go in ATFConverter
        return sumerian_output

    #def process(self, text):
    #    """
    #    Expects a list of tokens, will return the list converted from
    #    ATF format to print-format
    #    """

    #    output = []

    #    for tokens in text:
    #       ###f-string compiling tokenizer functions
    #    return output
