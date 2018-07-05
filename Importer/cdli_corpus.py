"""
The Importer feature sets up the ability to work with cuneiform text(s)
one-on-one, whether it is the Code of Hammurabi, a collection of texts such as
ARM01, or whatever your research desires.

This cdli_corpus module is for working with text files having already been read
by file_importer. The file_lines required by CDLICorpus are taken from prior
use of FileImport(text_file).read_file().

e.g.:
    # FileImport takes a txt file and reads it; this becomes file_lines.
        text_path = os.path.join('texts', 'ARM01_texts.txt')
        f_i = FileImport(text_path)
        f_i.read_file()
        ARM01 = f_i.file_lines
    # CDLICorpus takes file_lines and uses it to work:
        cdli = CDLICorpus(ARM01)
        cdli.chunk_text()
        cdli.ingest()
        cdli.print_text_by_cdli_number('&P254202')

The output of CDLICorpus will be able to further utilized by the feature
ATFConverter and its subsequent classes: Tokenizer, ATFConverter, Lemmatizer,
and PPrint.
"""

import re

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class CDLICorpus(object):
    """
    Takes file_lines, prepares and organizes data.
    """
    def __init__(self, file_lines):
        """
        :param file_lines: See method docstring for capturing file_lines.
        """
        self.file_lines = file_lines

    def chunk_text(self):
        """
        Splits up a text whenever a break is found in file_lines.
        :return: Disparate texts.
        """
        chunk_text, text = [], []
        for line in self.file_lines:
            if line.strip() == '':
                if len(text) > 0:   # pylint: disable =len-as-condition
                    chunk_text.append(text)
                text = []
            else:
                text.append(line.rstrip())
        chunk_text.append(text)
        return chunk_text

    def find_cdli_number(self):
        """
        Finds CDLI Number (ex: &P254202, P254203) in file_lines & lists it.
        :return: List of CDLI Numbers found in file_lines.
        """
        header, output = [], []
        for lines in self.file_lines:
            if re.match(r'^&P\d.*$', lines):
                header.append(lines)
            elif re.match(r'^P\d.*$', lines):
                header.append(lines)
        for string in header:
            if len(string) > 1:
                splitstring = string.split('=')
                cdli_num = splitstring[0].rstrip()
                output.append(cdli_num)
            elif len(string) > 1 and not re.match('=', string):
                cdli_num = header[0].rstrip()
                output.append(cdli_num)
            else:
                output.append('No cdli number found in text!'.format())
        return output

    def find_edition(self):
        """
        Finds edition info (ex: ARM 01, 001) in file_lines and lists it.
        :return: List of editions found in file_lines.
        """
        header, output = [], []
        for lines in self.file_lines:
            if re.match(r'^&P\d.*$', lines):
                header.append(lines)
            elif re.match(r'^P\d.*$', lines):
                header.append(lines)
        for string in header:
            if len(string) > 1:
                splitstring = string.split('=')
                edition = splitstring[1].lstrip()
                output.append(edition)  # pylint: disable =expression-not-assigned
            else:
                output.append('No edition information in text!'.format())
        return output

    def find_metadata(self):    # broken
        """
        Finds metadata in file_lines and lists it.
        :return: List of metadata found in file_lines.
        """
        final, lines = [], []
        for text in self.chunk_text():
            if text[0].startswith('Primary publication:'):
                lines.append(text[0:25])
            else:
                lines.append('None found.')
        final.append(lines)
        return lines

    def find_transliteration(self):  # broken
        """
        Finds any transliteration in file_lines and lists it.
        :return: List of transliterations found in file_lines.
        """
        final, lines = [], []
        for text in self.chunk_text():
            if text[0].startswith('Primary publication:'):
                lines.append(text[26:])
            else:
                lines.append(text)
        final.append(lines)
        return lines

    def ingest(self):
        """
        Captures all listed information above and formats it in a clear, and
        disparate manner.
        :return: List of dictionaries composed of information gathered in above
        functions.
        """
        cdli_number = self.find_cdli_number()
        edition = self.find_edition()
        metadata = self.find_metadata()
        transliteration = self.find_transliteration()
        new_text = {'cdli numbers': cdli_number, 'text editions': edition,
                    'metadata': metadata, 'transliterations': transliteration}
        self.text = new_text  # pylint: disable= attribute-defined-outside-init

    # Should here on out be in new method called pretty print?

    def print_text_editions(self):
        """
        Prints text editions collected in ingest.
        :return: text editions
        """
        text = '{} {}'.format('text editions:', self.text['text editions'])
        return text

    def print_cdli_numbers(self):
        """
        Prints cdli numbers collected in ingest.
        :return: cdli numbers
        """
        cdli = '{} {}'.format('cdli numbers:', self.text['cdli numbers'])
        return cdli

    def print_text(self, edition_or_cdli_number):
        """
        Prints transliteration with either text edition or cdli number.
        :return: transliteration
        """
        if edition_or_cdli_number in self.text['text editions'] or \
                self.text['cdli numbers']:
            return self.text['transliterations']

    def print_metadata(self, edition_or_cdli_number):
        """
        Prints metadata with either text edition or cdli number.
        :return: metadata
        """
        if edition_or_cdli_number in self.text['text editions'] or \
                self.text['cdli numbers']:
            return self.text['metadata']
