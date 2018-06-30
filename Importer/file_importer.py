"""
This module is for taking CDLI download files and creating disparate texts
out of CDLI's "download all text" option:
(https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text (e.g. Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions (e.g. ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01).

The goal of this feature is to be able to separate out text files on a
'case-by-case' standard; this feature sets up the ability to work with
cuneiform text(s) one-on-one whether it is Code of Hammurabi, a collection of
texts such as ARM01, or whatever your search function desires.
"""

import re

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class FileImport(object):
    """
    The goal of this class is to take a file downloaded from CDLI's website
    (https://cdli.ucla.edu/search/download_data_new.php?data_type=all)
    and prepare it for text-by-text analysis or otherwise find texts by
    their CDLI_number of a text and either update to or import the most recent
    iteration found in the CDLI github backup repository
    (https://github.com/cdli-gh/data).
    """
    def __init__(self, filename):
        """
        :param cdli_corpus: This can be downloaded through CLTK. The file is
        saved as "cdli_atfunblocked.atf" and can be renamed locally
        as a .txt with usable with no other changes; see README for more info.
        :param filename: name of downloaded file
        """
        self.filename = filename
        self.file_lines = FileImport.read_file(self)    # This works, but not below (?)
        self.texts = FileImport.__discern_texts__(self)

    def read_file(self):
        """
        Grabs downloaded text file and enables it to be read.
        """
        line_output = []
        with open(self.filename, mode='r+', encoding='utf8') as f:
            # self.raw_file = f.read()
            for line in f:
                line_output.append(line.rstrip())
                # self.file_lines = self.raw_file.splitlines()
            return line_output

    def __discern_texts__(self):
        """
        Using the read_file function, this method recognizes tablets based off
        of metadata in the file. Used to create a key of each title.
        :param text_file: This is the text file that you downloaded from
        CDLI.
        :return: List that titles of disparate texts in the downloaded file.
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
        Using read_file, this process separates out tablets based off of
        metadata in the file. Used to create a value of each text body.
        :param text_file: This is the text file that you downloaded from
        CDLI.
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
        Uses
        :return: list of lists containing CDLI Number and text edition name.
        """
        output = []
        try:
            header = self.texts
            for string in header:
                if len(string) > 1:
                    splitstring = string.split('=')
                    pnum = splitstring[0].rstrip()
                    edition = splitstring[1].lstrip()
                    output.append(pnum), output.append(edition)  # pylint: disable =expression-not-assigned
                else:
                    pnum = header[0].rstrip()
                    output.append(pnum)
            return output
        except IndexError:
            print("No header information in text: {}".format(
                self), repr(self))

    def import_text(self, cdli_number):
        """
        Takes cdli_number and captures match in your friendly neighborhood text
        file.
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

    # not the actual method, just placeholder
    def update_text(self, cdli_number):
        """
        Replaces text with import_text.
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
