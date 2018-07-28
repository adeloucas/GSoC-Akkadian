from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.atf_converter import ATFConverter
from PrettyPrint.pretty_print import PrettyPrint
import os

# import a text and read it
fi = FileImport('texts/cdli_corpus.txt')
fi.read_file()
# output = fi.raw_file or fi.file_lines; for folder catalog = fi.file_catalog()

cc = CDLICorpus()
cc.ingest_text_file(fi.file_lines)
# this creates disparate sections of the text ingested (edition, metadata, etc)
transliteration = [text['transliteration'] for text in cc.texts][0]
# access the data through cc.texts (e.g. above) or initial prints (e.g. below):
# look through the file's contents
print(cc.table_of_contents())
# select a text through edition or cdli number (there's also .print_metadata):
selected_text = cc.print_text('&P254203')
# otherwise use the above 'transliteration'; same thing:
print(selected_text)
print(transliteration)

# tokenize by word or sign
#atf = ATFConverter()
#tk = Tokenizer()
#lines = [tk.string_tokenizer(text, include_blanks=False)
#         for text in atf.process(selected_text)]
#words = [tk.word_tokenizer(line[0]) for line in lines]
# taking off first four lines to focus on the text with [4:]
#print(lines[4:])
#print()
#print(words[4:])
#print()
#for word in words[4:]:
#    signs = [tk.sign_tokenizer(x) for x in word]
#    print(signs)

# pretty printing:
#pp = PrettyPrint()
#destination = os.path.join('tests', 'tutorial_html.html')
#pp.html_print_single_text(cc.texts, '&P254202', destination)

# ISSUES: When can I process the text?