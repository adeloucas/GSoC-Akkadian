from ATFConverter.Tokenizer import Tokenizer

sign_conversion = Tokenizer()

with open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt","r+", encoding = "utf8") as File:

    text = File.readlines()
    text_selection = text[3042:3054]
    text_selection2 = text[3013:3026]
    tokenized = sign_conversion.linetokenizer(text_selection2)
    print(text_selection)
    print()
    print(tokenized)