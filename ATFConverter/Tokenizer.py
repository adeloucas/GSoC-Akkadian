import os
import re
import nltk
from ATFConverter.ATFConverter import ATFConverter
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'[[\[\]\<\>\(\)\?\#\!\s\-\{\}\|^\_]|\d*\.', gaps=True)

class Tokenizer(object):
    """Creates tokens from .txt"""

    tokenizer = RegexpTokenizer(r'[[\[\]\<\>\(\)\?\#\!\s\-\{\}\|^\_]|\d*\.', gaps=True)

    def Hammurabi_tokenize_test(self, text):
        """This is obviously not a real function, but it works; don't know how to change line 16... """
        with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8") as File:
            text_string = File.read()
            test = tokenizer.tokenize(text_string[805:1005]) 
        return test