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
    def __file_pull__(read_file, pnumber):
        """
        Takes cdli_number and captures match in your friendly neighborhood text
        file.
        :param read_file: This is the text file that you downloaded from
        CDLI.
        :param pnumber: the pnumber, e.g. P254202 or &P254202
        :return: strings of text by line in list form
        """
        output = []
        f_i = FileImport()
        file = os.path.join('..', 'texts', read_file)
        text = f_i.read_file(file)
        contents = False
        for line in text:
            if line.rstrip().startswith(pnumber):
                contents = True
            elif len(line) == 0:
                contents = False
            if contents:
                output.append(line)
        return output

    def import_text(self, pnumber):
        """
        Takes cdli_number and captures match in your friendly neighborhood text
        file.
        :param pnumber: the pnumber, e.g. P254202 or &P254202
        :return: strings of text by line in list form
        """
        output = []
        f_i = FileImport()
        file = os.path.join('..', 'texts', 'cdli_corpus.txt')
        text = f_i.read_file(file)
        contents = False
        for line in text:
            if line.rstrip().startswith(pnumber):
                contents = True
            elif len(line) == 0:
                contents = False
            if contents:
                output.append(line)
        return output

    @staticmethod           # not the actual method, just placeholder
    def update_text(text_file, cdli_number):
        """
        Matches __file_pull__ and replaces text with import_text
        :param text_file: downloaded file from CDLI
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return:
        """
        output = []
        file = os.path.join('..', 'texts', text_file)
        with open(file, mode='w', encoding='utf8') as text:
            if cdli_number in text:
                output.append(cdli_number)
            return output

    ## Found This--- To Test Out
    #with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        #for line in file:
            #print(line.replace(__file_pull__, import_text), end='')
