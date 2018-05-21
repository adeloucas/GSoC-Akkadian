from ATFConverter.ATFConverter_attempt_to_condense import ATFConverter

File = open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8")
original = File.read()
normalize = ATFConverter()
normalized = normalize.sumerianization(original)
print(normalized[0:10000])
File.close()
