from ATFConverter.cdli_import import Import

IMPORT = Import()

file = \
    r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt"

first = IMPORT.__read_file__(file)
print(first[0:59])
print(IMPORT.__discern_texts__(first[0:90]))
print(list(IMPORT.__split_texts__(first[0:90])))
print(IMPORT.text_contents(first[0:127]))


