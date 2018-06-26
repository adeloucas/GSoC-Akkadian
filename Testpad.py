from Importer.cdli_import import FileImport
from ATFConverter.atf_converter import ATFConverter
from ATFConverter.tokenizer import Tokenizer
from ATFConverter.pretty_print import PrettyPrint

IMPORT = FileImport()
ATF = ATFConverter(two_three=False)
TOKEN = Tokenizer(preserve_metadata=False, preserve_damage=False)
PRINT = PrettyPrint()

downloaded_file = \
    r"C:\\Users\\andrew.deloucas\\GSoC-Akkadian\\texts\\ARM1Akkadian.txt"

# selecting a text
ARM01 = IMPORT.text_contents(IMPORT.read_file(downloaded_file))
TOC = IMPORT.texts_within_file(IMPORT.read_file(downloaded_file))
print()
print('Truncated Table of Contents:\n', TOC[0:183])
print()
selected_doc = IMPORT.text_print(ARM01, '&P254205 = ARM 01, 004')
print('selected document example:\n',
      '&P254205 = ARM 01, 004\n\n',
      selected_doc)

# processing the text
line_tokenized = TOKEN.string_tokenizer(selected_doc)
print('string / line tokenizer:', line_tokenized)
print()
sign_tokenized = TOKEN.print_sign_tokenizer(line_tokenized)
print('sign tokenizer:', sign_tokenized)
print()
processed_doc = [ATF.process(line) for line in sign_tokenized]
print('processed document:', processed_doc)
print()
analyzed_doc = [TOKEN.print_sign_language(line)[1:] for line in processed_doc]
print('analyzed signs:', analyzed_doc)
print()
#pretty printing
sumerian = PRINT.sumerian_converter(analyzed_doc)
underscores = PRINT.underscore_remover(sumerian)
final = PRINT.reader_reconstruction(underscores)
#print(final)
print('reconstructed text:\n\n', '\n'.join(final))
