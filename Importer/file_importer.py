"""
This module is for importing text files out of CDLI's "download all text"
option: (https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text (e.g. Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions (e.g. ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01).

This feature sets up the ability to work with cuneiform text(s) one-on-one,
whether it is the Code of Hammurabi, a collection of texts such as ARM01, or
whatever your research desires.
"""

import re
import os

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class FileImport(object):
    """
    Takes a text file and prepares it for text-by-text analysis; this method
    finds texts via CDLI_number and either imports from a downloaded text file,
    or imports and updates from the most recent iteration found in the CDLI
    backup repository (https://github.com/cdli-gh/data), downloaded via CLTK:
    http://docs.cltk.org/en/latest/importing_corpora.html.
    """
    def __init__(self, filename):
        """
        :param cdli_corpus: This is downloaded through CLTK. The file is
        saved as "cdli_atfunblocked.atf"; see README for more info. This
        function uses the filename "cdli_corpus.txt" for this same file.
        :param filename: name of any downloaded file from CDLI.
        """
        self.filename = filename
        self.file_lines = self.read_file()

    def read_file(self):
        """
        Grabs downloaded text file and enables it to be read.
        """
        with open(self.filename, mode='r+', encoding='utf8') as text_file:
            self.raw_file = text_file.read()
        file_lines = [x.rstrip() for x in self.raw_file.splitlines()]
        return file_lines

    def import_text(self, cdli_number):
        """
        Takes cdli_number and captures match in your text file.
        :param cdli_number: the p-number, e.g. P254202 or &P254202
        :return: strings line by line in list form
        """
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

    def __discern_texts__(self):
        """
        Recognizes tablets based off of metadata in the file. Used to create a
        key of each title.
        :return: List of disparate text titles in the downloaded file.
        """
        output = []
        for lines in self.file_lines:
            if re.match(r'^&P\d.*$', lines):
                output.append(lines)
            elif re.match(r'^P\d.*$', lines):
                output.append(lines)
        return output

    def __split_texts__(self):
        """
        Separates out texts based off of metadata in the file. Used to create
        a value of each body of text.
        :return: List that separates out disparate texts into lists of strings.
        """
        texts, text = [], []
        for line in self.file_lines:
            if line.strip() == '':
                if len(text) > 0:   # pylint: disable =len-as-condition
                    texts.append(text)
                text = []
            else:
                text.append(line.rstrip())
        texts.append(text)
        return texts

    def __call_names__(self):
        """
        Takes key made in __discern_texts__ and separates out cdli_number and
        its edition.
        :return: List containing CDLI Number and text edition name.
        """
        output = []
        header = self.__discern_texts__()
        for string in header:
            if len(string) > 1:
                splitstring = string.split('=')
                pnum = splitstring[0].rstrip()
                edition = splitstring[1].lstrip()
                output.append(pnum), output.append(edition)  # pylint: disable =expression-not-assigned
            elif len(string) > 1 and not re.match('=', string):
                pnum = header[0].rstrip()
                output.append(pnum)
            else:
                output.append('No header information in text!'.format())
        return output

    def update_text(self, cdli_number):  # works, but not as I want it to.
        """
        Replaces single text in file with import_text method.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: xxx
        """
        # corpus you wish to use for replacement;
        cdli = os.path.join('..', 'texts', 'two_text.txt')
        cdli_corpus = FileImport(cdli).import_text(cdli_number)
        # text you want to replace
        text_in_question = FileImport(self.filename).import_text(cdli_number)

        with open(self.filename, 'r+') as f:    # use self.raw_file
            filedata2 = str(text_in_question)
            update = filedata2.replace(filedata2, str('\n'.join(cdli_corpus)))
            f.write(update)   # FileInput for line-for-line replacement?


