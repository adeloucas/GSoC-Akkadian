import os
import re
import nltk
from unicodedata import normalize
from nltk.tokenize import RegexpTokenizer
#s = "10. szum-ma a-wi-lum \n 11. _a-sza3_ a-na _{gesz}kiri6_ [za]-qa2-pi2-im \n 12. [a]-na# _nu-{gesz}kiri6_ id-di-in  \n 13. _nu-{gesz}kiri6_ \n 14. _{gesz}kiri6_ iz-qu2-up \n 15. _mu 4(disz)-kam_ \n 16. _{gesz}kiri6_ u2-ra-ab-ba \n 17. i-na ha-mu-usz-tim "
#tokenizer = RegexpTokenizer(r'[\[\]\<\>\(\)\?\#\!\s\-\{\}|^\_]', gaps=True)
#tokenizer.tokenize(s)
#print(tokenizer.tokenize(s))

with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8") as File:
    original = File.read()
    tokenizer = RegexpTokenizer(r'[\[\]\<\>\(\)\?\#\!\s\-\{\}|^\_]', gaps=True)
    #tokenizer = RegexpTokenizer(r'[^\d*\.$]', gaps=True)
    #tokenizer = RegexpTokenizer(r'[\d]+[\.]', gaps=True)
    tokenizer.tokenize(original)
    print(tokenizer.tokenize(original[805:1805]))
    #print(original[805:1805])

#10. szum-ma a-wi-lum 
#11. _a-sza3_ a-na _{gesz}kiri6_ [za]-qa2-pi2-im 
#12. [a]-na# _nu-{gesz}kiri6_ id-di-in  
#13. _nu-{gesz}kiri6_ 
#14. _{gesz}kiri6_ iz-qu2-up 
#15. _mu 4(disz)-kam_ 
#16. _{gesz}kiri6_ u2-ra-ab-ba 
#17. i-na ha-mu-usz-tim
