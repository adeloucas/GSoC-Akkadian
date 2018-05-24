from ATFConverter.ATFConverter import Tokenizer
from ATFConverter.ATFConverter import ATFConverter

sign_conversion = Tokenizer()
convert = ATFConverter()

with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\Akkadian.txt","r+", encoding = "utf8") as File:

    text2 = File.readlines()
    text_selection2 = text2[40:42]
    tokenized2 = sign_conversion.tokenizer(text_selection2)
    conversion = convert.process(text_selection2)

    print(text_selection2)
    print()
    print(tokenized2)
    print()
    print(text_selection2)