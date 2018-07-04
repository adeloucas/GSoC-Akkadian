"""
This module is for working on disparate texts out of CDLI's "download all text"
option: (https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text (e.g. Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions (e.g. ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01).

This feature enables one to work with individual cuneiform texts, whether it is
the Code of Hammurabi, a collection of texts such as ARM01, or whatever your
research desires.
"""

import re

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class CDLICorpus(object):
    """
    This method makes practical use out of FileImport; it creates the ability
    to search through a text file, select and print individual texts, and
    prepares text to be put through the ATFConverter, Tokenizer, Lemmatizer,
    and PrettyPrinter.
    """
    def __init__(self, file_lines):
        """
        :param file_lines: FileImport(text_path).read_file();
                           file_lines = FileImport.file_lines
        """
        self.file_lines = file_lines

    def chunk_text(self):
        """
        xxx
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

    def find_pnum(self):
        """
        xxx
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
                pnum = splitstring[0].rstrip()
                output.append(pnum)  # pylint: disable =expression-not-assigned
            elif len(string) > 1 and not re.match('=', string):
                pnum = header[0].rstrip()
                output.append(pnum)
            else:
                output.append('No cdli number information in text!'.format())
        return output

    def find_edition(self):
        """
        xxx
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

    def find_metadata(self):    # make this
        """
        xxx
        """
        text, lines = [], []
        metadata = True
        for line in self.file_lines:
            if line.startswith('Primary publication:'):
                metadata = True
            if line.startswith('Transliteration:'):
                metadata = False
            if metadata:
                lines.append(line)
        text.append(lines)
        return lines

    def find_text_lines(self):
        """
        xxx
        """
        text, lines = [], []
        transliteration = False
        for line in self.file_lines:
            if re.match(r'^&P\d.*$', line) or re.match(r'^P\d.*$', line):
                transliteration = True
            if line.startswith('Primary publication:'):
                transliteration = False
            if transliteration:
                lines.append(line)
        text.append(lines)
        return lines

    def ingest(self):
        """
        xxx
        """
        pnum = self.find_pnum()
        edition = self.find_edition()
        metadata = self.find_metadata()
        text_lines = self.find_text_lines()
        new_text = {'pnum': pnum, 'edition': edition,
                    'metadata': metadata, 'text_lines': text_lines}
        self.text = new_text  # pylint: disable= attribute-defined-outside-init
        return self.text

    """
    def return_text_by_pnum(self, pnum):
        return [text.lines for text in self.texts if text['pnum'] == pnum][0]

    def print_toc(self):
        print([text['pnum'] for text in self.texts])

    def import_text(self, cdli_number):  # to turn into return_text_by_pnum
        #
        Takes cdli_number and captures match in your text file.
        :param cdli_number: the p-number, e.g. P254202 or &P254202
        :return: strings line by line in list form
        #
        output = []
        contents = False
        for line in self.file_lines:
            if line.rstrip().startswith(cdli_number):
                contents = True
            elif len(line) == 0:    # pylint: disable =len-as-condition
                contents = False
            if contents:
                output.append(line)
        return output

    def update_text(self, cdli_number):  # works, but not as I want it to.
        #
        Replaces single text in file with import_text method.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: xxx
        #
        # corpus you wish to use for replacement;
        cdli = os.path.join('..', 'texts', 'two_text.txt')
        cdli_corpus = FileImport(cdli).import_text(cdli_number)
        # text you want to replace
        text_in_question = FileImport(self.filename).import_text(cdli_number)

        with open(self.filename, 'r+') as f:    # use self.raw_file
            filedata2 = str(text_in_question)
            update = filedata2.replace(filedata2, str('\n'.join(cdli_corpus)))
            f.write(update)   # FileInput for line-for-line replacement?

    def __text_contents__(self):
        #
        Using the read_file function, this process utilizes __discern_texts__
        and __split_texts__ in order to create a dictionary of texts from
        the text_file.

        i.e. discern_texts for key; split_texts for value:
        {'&P254203 = ARM 01, 002': ["&P254203 = ARM 01, 002",
                                    "#atf: lang akk",
                                    "@tablet"
                                    "etc."]}

        :return: Dictionary of disparate texts in a file with line containing a
        CDLI number and published name of text as key & said text as its value.
        #
        key = self.__call_names__()
        value = list(self.__split_texts__())
        double_value = [value[i//2] for i in range(len(value)*2)]
        texts = zip(key, double_value)
        text_dict = dict(texts)
        return text_dict

    def text_print(self, key):
        #
        Using FileImport's __text_contents__, selects the respective text you
        wish to print.

        :param key: This either text edition name or CDLI number found in the
        function table_of_contents, e.g: ('&P254203') or ('ARM 01, 002').
        :return: Text as string.
        #
        output = self.__text_contents__()
        return output.get(key, '')
    """  # pylint: disable= pointless-string-statement
