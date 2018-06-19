"""
This module is for taking CDLI downloads files and creating disparate texts
out of CDLI's "download all text" option:
(https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text
(Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions:
(ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01)

The goal of this feature is to be able to use meta data available in the
atf_converter to separate out text files on a 'case-by-case' standard; this
feature sets up the ability to work with cuneiform text(s) one-on-one whether
or not it is Code of Hammurabi, a collection of texts such as ARM01, or
whatever your search function desires.
"""

import os
import re
from cltk.corpus.utils.importer import CorpusImporter
corpus_importer = CorpusImporter('akkadian')
corpus_importer.import_corpus('cdli_corpus')

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class FileImport(object):
    """
    The goal of this class is to take a file downloaded from CDLI's website
    (https://cdli.ucla.edu/search/download_data_new.php?data_type=all)
    and prepare it for text-by-text analysis. It separates out from a file
    instances of disparate texts, should the file contain several texts within
    one file (e.g. ARM1Akkadian.txt has 139 unique tablets within its one file,
    whereas Akkadian.txt contains only one "tablet").
    """

    @staticmethod
    def read_file(file):
        """
        Grabs the downloaded text file and enables it to be read.
        :param file: This is the text file that you downloaded from CDLI.
        """
        line_output = []

        with open(file, mode='r+', encoding='utf8') as text:
            for line in text:
                line_output.append(line.strip())
            return line_output

    @staticmethod
    def __discern_texts__(read_file):
        """
        Using the read_file function, this process recognizes tablets
        based off of metadata in the file.
        :param read_file: This is the text file that you downloaded from
        CDLI.
        :return: List that notes disparate texts in the downloaded file.
        """
        output = [line for line in read_file if line.startswith('&')]
        return output

    @staticmethod
    def __split_texts__(read_file):
        """
        Using read_file, this process separates out tablets based off of
        metadata in the file.
        :param read_file: This is the text file that you downloaded from
        CDLI.
        :return: List that separates out disparate texts into lists of strings.
        """
        output = []
        for line in read_file:
            if line.startswith('Primary'):
                yield output
                output = []
            output.append(line)
        yield output    # issue: prints "[[]" before list

    def texts_within_file(self, read_file):
        """
        Using the read_file function, this process utilizes discern_texts
        and split_texts in order to create a dictionary of texts from the file.

        i.e. either "ARM 01, 001" or "&P254202" for key; the text for value.

        :param read_file: This is the text file that you downloaded from
        CDLI.
        :return: Dictionary of separated texts in a file with either the
        CDLI number or published name of text as key & said text as its value.
        """

        titles = self.__discern_texts__(read_file)
        return "\n".join(titles)

    def text_contents(self, read_file):
        """
        Using the read_file function, this process utilizes discern_texts
        and split_texts in order to create a dictionary of texts from the file.

        i.e. either "ARM 01, 001" or "&P254202" for key; the text for value.

        :param read_file: This is the text file that you downloaded from
        CDLI.
        :return: Dictionary of separated texts in a file with either the
        CDLI number or published name of text as key & said text as its value.
        """
        key = self.__discern_texts__(read_file)
        value = list(self.__split_texts__(read_file))
        texts = zip(key, value[1:])
        text_dict = dict(texts)

        return text_dict

    @staticmethod
    def text_print(text_contents, key):
        """
        Using text_contents, select the respective key you wish to print for
        tokenization or pretty printing. To find the keys (i.e. texts) in the
        file:
        "\n".join(FileImport().text_contents(FileImport().read_file(file)).keys()).

        :param text_contents:
        :param value:
        :return:
        """

        return '\n'.join(text_contents[key])


class CDLIImport(object):
    """
    The goal of this class is to take find the CDLI_number of a text and update
    to its most recent iteration found in the CDLI github repository
    (https://github.com/cdli-gh/data), or otherwise be able to pull any one
    text from CDLI with the CDLI_number.
    """
    def __init__(self):
        """
        :param: empty.
        """
        self.import_text(cdli_number) = import_text(cdli_number)
        self.__search_file__(text, cdli_number) = \
            __search_file__(text, cdli_number)

    @staticmethod
    def __search_cdli__(cdli_number):
        """
        Takes cdli_number from __text_select__ and captures match in
        unblocked.atf file.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: text of file
        """
        line_output = []
        with open(cldi_corpus, mode='r+', encoding='utf8') as text:
            for line in text:
                if re.match(cdli_number):
                    line_output.append(line)
        # continuing appending line for line until struck with an '&' or break

    @staticmethod
    def __search_file__(text, cdli_number):
        """
        Takes cdli_number from __text_select__ and captures match in
        your friendly neighborhood text file.
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return: text of file
        """
        line_output = []
        file = os.path.join('texts', text)  # account for many locations?
        with open(file, mode='r+', encoding='utf8') as text:
            for line in text:
                if re.match(cdli_number):
                    line_output.append(line)
                return line_output
        # continuing appending line for line until struck with an empty line
    # this is due to metadata existing where it doesn't exist in cdli_corpus(?)

    def import_text(self, cdli_number):
        """
        Using the cdli_number of a text as a call number, selects text that
        matches the cdli_number.
        :param source: either CDLI or File
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return:
        """
        output = [self.__search_cdli__(cdli_number)]
        return output

    def update_text(self, text_file, cdli_number):
        """
        Matches __search_file__ and replaces text with __search_cdli__
        :param text_file: downloaded file from CDLI
        :param cdli_number: the pnumber, e.g. P254202 or &P254202
        :return:
        """
        cdli_text = self.import_text(cdli_number)
        file_text = self.__search_file__(text_file, cdli_number)
        file = os.path.join('texts', text_file)  # account for many locations?
        with open(file, mode='r+', encoding='utf8') as text:
            for file_text in text:
                file_text.replace(file_text, cdli_text)
            return "Text has been updated!"