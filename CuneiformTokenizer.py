import os
import re
import nltk
from unicodedata import normalize
from ATFConverter.ATFConverter import ATFConverter
from nltk.tokenize import RegexpTokenizer

with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8") as File:
    original = File.read()
    great = ATFConverter()
    tokenizer = RegexpTokenizer(r'[[\[\]\<\>\(\)\?\#\!\s\-\{\}\|^\_]|\d*\.', gaps=True)
    test = tokenizer.tokenize(original[805:1005])   
    test2 = tokenizer.tokenize(original[8305:8505]) #note: 'u₂', 'a', 'ra₂', '', 'u', '₂', 'disz'...
    tested = great.process(test)
    tested2 = great.process(test2)

    print(tested)
    print()
    print(tested2)
