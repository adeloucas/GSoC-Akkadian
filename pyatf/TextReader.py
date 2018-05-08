from pyatf.ATFConverter import ATFConverter

file = ARM1Akkadian.txt
ATF = open(file, 'r', encoding="utf8")
original = ATF.read()
normalize = ATFConverter()
normalized = normalize.convert(original)
print(normalized)
