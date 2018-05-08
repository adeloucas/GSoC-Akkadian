from pyatf.ATFConverter import ATFConverter

file = r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\ARM1Akkadian.txt"
ATF = open(file, 'r', encoding="utf8")
original = ATF.read()
normalize = ATFConverter()
normalized = normalize.convert(original)
print(normalized)