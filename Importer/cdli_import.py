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

import os
from Importer.file_import import FileImport

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class CDLIImport(object):
    """
    The goal of CDLIImport is to find texts by their CDLI_number of a text and
    either update to or import the most recent iteration found in the CDLI
    github backup repository (https://github.com/cdli-gh/data).
    """
    def __init__(self):
        """
        :param cdli_corpus: This can be downloaded through CLTK. The file is
        saved as "cdli_atfunblocked.atf" and can be renamed locally
        as a .txt with usable with no other changes; see README for more info.
        """

    @staticmethod
    def __file_pull__(text, cdli_number):
        """
        Takes cdli_number and captures match in your friendly neighborhood text
        file.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: strings of text by line in list form
        """
        output = []
        f_i = FileImport()
        file = f_i.read_file(os.path.join('..', 'texts', text))
        content = f_i.text_contents(file)

        for line in file:
            if cdli_number in line:
                output.append(f_i.text_print(content, line))
        return output[0]

    @staticmethod
    def import_text(cdli_number):
        """
        Takes cdli_number and captures match in unblocked.atf file.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: strings of text by line in list form
        """
        output = []     # fails on actual cdli_corpus, so not right solution...
        f_i = FileImport()
        file = f_i.read_file(os.path.join('..', 'texts', 'cdli_text.txt'))
        content = f_i.text_contents(file)
        for line in file:
            if cdli_number in line:
                output.append(f_i.text_print(content, line))
        return output[0]

    @staticmethod
    def update_text(text_file, cdli_number):
        """
        Matches __file_pull__ and replaces text with import_text
        :param text_file: downloaded file from CDLI
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return:
        """
        output = []         # not the actual method, just placeholder
        file = os.path.join('..', 'texts', text_file)
        with open(file, mode='w', encoding='utf8') as text:
            if cdli_number in text:
                output.append(cdli_number)
            return output

## Found This--- To Test Out
#with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    #for line in file:
        #print(line.replace(text_to_search, replacement_text), end='')
