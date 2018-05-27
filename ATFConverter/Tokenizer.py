import os
import re
from unicodedata import normalize
import nltk
from nltk.tokenize import RegexpTokenizer

class Tokenizer(object):

    def line_tokenizer(self, text):
    
        line_output = []

        with open(text, mode = "r+", encoding = "utf8") as File:
            lines = File.readlines()
            for no_meta in lines: 
                if re.match(r'^\d*\.|\d\'\.', no_meta):
                    try:
                        line_output.append(no_meta) 
                        #no_meta = re.subn(r'\n', '', no_meta) # doesn't work.
                    except KeyError:
                        line_output.append("ERROR")
            return line_output

    def string_line_tokenizer(self: object, untokenized_string: str, include_blanks=False):
        """This is just CLTK's line tokenizer. It works just fine for ATF files"""
        assert isinstance(untokenized_string, str), 'Incoming argument must be a string.'

        if include_blanks:
            tokenized_lines = untokenized_string.splitlines()
        else:
            tokenized_lines = [line for line in untokenized_string.splitlines() if line != r'\\n']
        return tokenized_lines

    def sign_tokenizer(self, text):
        """Utilizes RegexpTokenizer to return sign breakdown of lines in text"""
        token_output = []
        every_sign = RegexpTokenizer(r'[\s\-\_\#\!\?\[\]\{\}\(\)]|^\d*\.|\d\'\.', gaps=True)

        for line in text: 
            if re.match(r'^\d*\.|\d\'\.', line): 
                try:
                    token_output.append(every_sign.tokenize(line))
                except KeyError:
                    print("No conversion rule for: {}".format(line))
                    token_output.append("ERROR: ({})".format(line))
        return token_output            

#def determinatives_tokenizer(self, text): #works, but I question if this is what I should be making
#        determinatives_output = []
#        determinatives = re.compile(r'\{\w*\}')
#        for sign in determinatives.finditer(str(text)): 
#            if re.match(r'^\d*\.|\d\'\.', line):
#                determinatives_output.append(sign.group())


#def numbers_and_number_signs_tokenizer(self, text):
#        number_signs = r'\(\w*\)'
#        numbers = r'\s\d[^\.]'

#def Sumerian_tokenizer(self, text):
#        sumerian = r'\_.*\_'
#        akkadian_caught_in_sumerian = '\_\s.*\s\_'

#process: #hmmm
#        final_output = []
#        final_output.append('Determinatives:')
#        final_output.append(determinatives_output)
#        final_output.append('lines:')
#        final_output.append(token_output)
#        return final_output
