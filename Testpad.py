from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.atf_converter import ATFConverter
from PrettyPrint.pretty_print import PrettyPrint

fi = FileImport('texts/single_text.txt')
fi.read_file()
cc = CDLICorpus()
cc.ingest_text_file(fi.file_lines)
tk = Tokenizer()
atf = ATFConverter(two_three=False)
pp = PrettyPrint()

print(cc.table_of_contents())

fin = []
for lines in [text['transliteration'][0] for text in cc.texts]:
    fin.append(atf.process(lines[4:]))

print('\n'.join(fin[0]))

print(cc.texts)