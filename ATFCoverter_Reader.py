from ATFConverter.ATFConverter import ATFConverter

File = open(r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\Akkadian.txt","r", encoding = "utf8")
original = File.read()
normalize = ATFConverter()
normalized = normalize.consonants(original)
print(normalized[0:10000])
File.close()
