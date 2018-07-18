import os
from collections import Counter
from Importer.file_importer import FileImport
from Importer.cdli_corpus import CDLICorpus
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.atf_converter import ATFConverter


fi = FileImport('texts/Akkadian.txt')
fi.read_file()
cc = CDLICorpus()
cc.ingest_text_file(fi.file_lines)
tk = Tokenizer()
atf = ATFConverter()
stopwords = ['a-na', 'u3', 'sza', '[...]', 'i-na', '=',
             'ARM', '01,', 'lang', 'akk', 'um-ma', 'la',
             'u2-ul', 'mesz_', 'asz-szum', '0.1', 'broken',
             'isz-tu', '_lu2_', 'ki-a-am', '1(disz)', 'ki-ma',
             'x', 'sza-a-ti', 'the', '_lu2', '...]', 'lu-u2',
             'sza#', 'a-na#', '_u4', 'beginning', 'of', '2(disz)',
             '[a-na', 'szum-ma', 'hi-a_', 'ana', 'a-di']

bag_of_words = []
for lines in [text['transliteration'][0] for text in cc.texts]:
    for line in lines:
        for word in tk.word_tokenizer(line):
            if word[0] not in stopwords:
                bag_of_words.append('-'.join(atf.process(word[0].split('-'))))
frequency_analysis = Counter(bag_of_words).most_common(11)
print(frequency_analysis)
