from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.atf_converter import ATFConverter
from PrettyPrint.pretty_print import PrettyPrint
import os

# import a text and read it
fi = FileImport('texts/cdli_corpus.txt')
fi.read_file()
fi.file_catalog()
cc = CDLICorpus()
chunk = cc._chunk_text(fi.file_lines)
pnum = cc._find_cdli_number(fi.file_lines)
edition = cc._find_edition(fi.file_lines)
print(len(chunk))
print(len(pnum))
print(len(edition))