from ATFConverter.ATFConverter import Tokenizer
from ATFConverter.ATFConverter import ATFConverter

sign_conversion = Tokenizer()

with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\Akkadian.txt","r+", encoding = "utf8") as File:

    text2 = File.readlines()
    text_selection2 = text2[32:42]
    tokenized2 = sign_conversion.tokenizer(text_selection2)

    print(tokenized2)