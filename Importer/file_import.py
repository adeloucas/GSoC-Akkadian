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

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class FileImport(object):
    """
    The goal of this class is to take a file downloaded from CDLI's website
    (https://cdli.ucla.edu/search/download_data_new.php?data_type=all)
    and prepare it for text-by-text analysis. It separates out from a file
    instances into disparate texts, should the file contain several texts
    within one file (e.g. ARM1Akkadian.txt has 139 unique tablets within its
    one file, whereas Akkadian.txt contains only one "tablet").
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
    def __discern_texts__(file):    # Issue: Not all texts have the ampersand
        """
        Using the read_file function, this process recognizes tablets
        based off of metadata in the file. Used to create a key of each title.
        :param file: This is the text file that you downloaded from
        CDLI.
        :return: List that titles of disparate texts in the downloaded file.
        """
        output = [line for line in file if line.startswith('&P')]
        return output

    @staticmethod
    def __split_texts__(file):
        """
        Using read_file, this process separates out tablets based off of
        metadata in the file. Used to create a value of each text body.
        :param file: This is the text file that you downloaded from
        CDLI.
        :return: List that separates out disparate texts into lists of strings.
        """
        texts, text = [], []
        for line in file:
            if line.strip() == '':
                if len(text) > 0:   # pylint: disable =len-as-condition
                    texts.append(text)
                text = []
            else:
                text.append(line.strip())
        texts.append(text)
        return texts

    def texts_within_file(self, file):
        """
        Using the read_file function, this process utilizes discern_texts
        in order to create a table of contents from the file.

        :param file: This is the text file that you downloaded from
        CDLI.
        :return: List of disparate texts in toto from read_file
        """

        titles = self.__discern_texts__(file)
        return titles

    def __text_contents__(self, file):
        """
        Using the read_file function, this process utilizes __discern_texts__
        and __split_texts__ in order to create a dictionary of texts from
        the file.

        i.e. discern_texts for key; split_texts for value:
        {'&P254203 = ARM 01, 002': ["&P254203 = ARM 01, 002",
                                    "#atf: lang akk",
                                    "@tablet"
                                    "etc."]}

        :param file: This is the text file that you downloaded from
        CDLI.
        :return: Dictionary of disparate texts in a file with line containing a
        CDLI number and published name of text as key & said text as its value.
        """

        key = self.__discern_texts__(file)
        value = list(self.__split_texts__(file))   # split doesn't work
        texts = zip(key, value)
        text_dict = dict(texts)

        return text_dict

    @staticmethod
    def text_print(file, key):
        """
        Using text_contents, select the respective key you wish to print for
        tokenization or pretty printing.

        i.e.:
        texts = file_import.__text_contents__(file)
        text_print(texts, '&P254203 = ARM 01, 002')

        :param file: This is the text file that you downloaded from
        CDLI.
        :param key: This is any string provided by texts_within_file method.
        :return:
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', file)
        text = cdli.read_file(file)
        output = cdli.__text_contents__(text)
        return output.get(key, '')
