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
cc.ingest_text_file(fi.file_lines)
cc.table_of_contents()

text = cc.call_text('&P254203')
tk = Tokenizer(preserve_damage=False)
atf = ATFConverter(two_three=False)
text = tk.string_tokenizer('\n '.join(text), include_blanks=False)
for line in text:
    word = tk.word_tokenizer(line)
    print(word)
    for signs in word:
        sign = tk.sign_tokenizer(signs)
        print(atf.process(x[0] for x in sign))

p_p = PrettyPrint()
destination = os.path.join('Testpad_html.html')
p_p.html_print_single_text(cc.texts, '&P254203', destination)
