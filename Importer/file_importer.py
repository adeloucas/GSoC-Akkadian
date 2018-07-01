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
import fileinput

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
        self.file_lines = FileImport.read_file(self)    # This works, but not below (?)
        self.texts = FileImport.__discern_texts__(self)
        #self.raw_file = None
        #self.file_lines = None

    def read_file(self):
        """
        Grabs downloaded text file and enables it to be read.
        """
        line_output = []
        with open(self.filename, mode='r+', encoding='utf8') as f:  # pylint: disable= invalid-name
            #self.raw_file = f.read()
            for line in f:
                line_output.append(line.rstrip())
                #self.file_lines = self.raw_file.splitlines()
            return line_output

    def import_text(self, cdli_number):
        """
        Takes cdli_number and captures match in your text file.
        :param cdli_number: the p-number, e.g. P254202 or &P254202
        :return: strings of text by line in list form
        """
        output = []
        text = self.file_lines
        contents = False
        for line in text:
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
        text = self.file_lines
        for lines in text:
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
        text_file = self.file_lines
        for line in text_file:
            if line.strip() == '':
                if len(text) > 0:   # pylint: disable =len-as-condition
                    texts.append(text)
                text = []
            else:
                text.append(line.rstrip())
        texts.append(text)
        return texts

    def __text_call_names__(self):
        """
        Takes key made in __discern_texts__ and separates out cdli_number and
        its edition.
        :return: List containing CDLI Number and text edition name.
        """
        output = []
        header = self.texts
        for string in header:
            if len(string) > 1:
                splitstring = string.split('=')
                pnum = splitstring[0].rstrip()
                edition = splitstring[1].lstrip()
                output.append(pnum), output.append(edition)  # pylint: disable =expression-not-assigned
            elif len(string) == 1:
                pnum = header[0].rstrip()
                output.append(pnum)
            else:
                output.append('No header information in text!'.format())
        return output

    # not the actual method, just placeholder
    def update_text(self, cdli_number):
        """
        Replaces single text in file with import_text method.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return:
        """
        output = []
        text = self.file_lines
        if cdli_number in text:
            output.append(cdli_number)
        return output
    """
    Found this -- To Test Out
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
    print(line.replace(__file_pull__, import_text), end='')
    """  # pylint: disable =pointless-string-statement
