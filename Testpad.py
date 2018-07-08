import os
from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus


path = os.path.join('texts', 'two_text.txt')
f_i = FileImport(path)
f_i.read_file()
text_file = f_i.file_lines
cdli = CDLICorpus()
cdli.ingest_text_file(text_file)
output = cdli.texts
print(output)
print()
for toc in cdli.texts:
    edition = toc['text edition']
    num = toc['cdli number']
    metadata = toc['metadata'][0][0].startswith('Primary')
    text = '{} {}{} {} {}{} {} {}'.format('edition:', edition, ';',
                                         'cdli number:', num, ';',
                                      'metadata:', metadata)
    print(text)
print()


def print_text(edition_or_cdli_number):
    for _ in cdli.texts:
        if edition_or_cdli_number in _['text edition'] or \
                _['cdli number']:
            return _['metadata']


print(print_text('&P254203'))
