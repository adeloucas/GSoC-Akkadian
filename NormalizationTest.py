from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
f1 = FileImport('./texts/ARM1Akkadian.txt')
f1.read_file()
c = CDLICorpus()
c.parse_file(f1.file_lines)
text = c.catalog['P254316']
lines = zip(text['transliteration'], text['normalization'], text['translation'])
for i, line in enumerate(lines):
    for x in range(3):
        print(f"{i}: {line[x]}")
    print()