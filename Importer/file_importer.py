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

    def read_file(self):
        """
        Grabs downloaded text file and enables it to be read.
        """
        with open(self.filename, mode='r+', encoding='utf8') as text_file:
            self.raw_file = text_file.read()  # pylint: disable= attribute-defined-outside-init
        self.file_lines = [x.rstrip() for x in self.raw_file.splitlines()]  # pylint: disable= attribute-defined-outside-init


    def file_catalog(self):
        """
        xxx
        """
        ex = os.path.split(self.filename)
        os.listdir(ex[0])
