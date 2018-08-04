from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.atf_converter import ATFConverter
from PrettyPrint.pretty_print import PrettyPrint


# import a text and read it
fi = FileImport('texts/two_text_no_metadata.txt')
fi.read_file()
fi.file_catalog()
cc = CDLICorpus()
chunk = cc._chunk_text(fi.file_lines)
pnum = cc._find_cdli_number(fi.file_lines)
edition = cc._find_edition(fi.file_lines)

cc.space_texts(fi.file_lines)
chunk2 = cc._chunk_text(fi.file_lines)

indices = []
for i, elem in enumerate(fi.file_lines):
    if '&P' in elem:
        indices.append(i)
print('incidences where &P is found in cdli_corpus:', indices)
print('# of incidences where &P is found in cdli_corpus:', len(indices))

for i in sorted(indices, reverse=True):
    fi.file_lines.insert(i, '')
chunk3 = cc._chunk_text(fi.file_lines)
pnum2 = cc._find_cdli_number(fi.file_lines)


print('original number of chunk texts:', len(chunk))
print('chunk texts after index spaces are added:', len(chunk2))
print('# of pnums (for references)', len(pnum))