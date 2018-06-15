from ATFConverter.cdli_import import Import
import os

IMPORT = Import()

file = \
    r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt"

first = IMPORT.__read_file__(file)
print(first)


