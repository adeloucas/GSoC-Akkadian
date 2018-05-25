import os
import re
from unicodedata import normalize
import nltk
from nltk.tokenize import RegexpTokenizer

#tokenizer = RegexpTokenizer(r'[[\[\]\<\>\(\)\?\#\!\s\-\$\@\{\}\|^\_]|\d*\.|\d\'\.', gaps=True)
tokenizer = RegexpTokenizer(r'[\s\-\_\#\!\?\[\]]|^\d*\.|\d\'\.', gaps=True)

class Tokenizer(object):
    """Creates tokens from .txt"""

    def linetokenizer(self, text):

        token_output = []

        for token in text: 
            if re.match(r'^\d*\.|\d\'\.', token): 
                try:
                    token_output.append(tokenizer.tokenize(token))
                except KeyError:
                    print("No conversion rule for: {}".format(token))
                    token_output.append("ERROR: ({})".format(token))
        return token_output