from ATFConverter.ATFConverter import ATFConverter

File = open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8")
original = File.read()
normalize = ATFConverter()
normalized = normalize.convert(original)
print(normalized)
File.close()
