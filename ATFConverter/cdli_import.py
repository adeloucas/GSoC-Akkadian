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
    #def __init__(self):
    #    """
    #    :param: empty.
    #    """

    @staticmethod
    def __read_file__(file):
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
    def __discern_texts__(__read_file__):
        """
        Using the __read_file__ function, this process recognizes tablets
        based off of metadata in the file.
        :param __read_file__: This is the text file that you downloaded from
        CDLI.
        :return: List that notes disparate texts in the downloaded file.
        """
        output = [line for line in __read_file__ if line.startswith('&')]
        return output

    @staticmethod
    def __split_texts__(__read_file__):
        """
        Using __read_file__, this process separates out tablets based off of
        metadata in the file.
        :param __read_file__: This is the text file that you downloaded from
        CDLI.
        :return: List that separates out disparate texts into lists of strings.
        """
        output = []
        for line in __read_file__:
            if line.startswith('Primary'):
                yield output
                output = []
            output.append(line)
        yield output    # issue: prints "[[]" before list

    def text_contents(self, __read_file__):
        """
        Using the __read_file__ function, this process utilizes discern_texts
        and split_texts in order to create a dictionary of texts from the file.

        i.e. either "ARM 01, 001" or "&P254202" for key; the text for value.

        :param __read_file__: This is the text file that you downloaded from
        CDLI.
        :return: Dictionary of separated texts in a file with either the
        CDLI number or published name of text as key & said text as its value.
        """

        key = self.__discern_texts__(__read_file__)
        value = list(self.__split_texts__(__read_file__))
        texts = zip(key, value[1:])
        text_dict = dict(texts)

        return text_dict

class GithubImport(object):
    """
    The goal of this class is to take documentation from CDLI's source data
    (https://github.com/cdli-gh/data) imported into the CLTK
    (https://github.com/cltk/cltk/wiki/How-to-add-a-corpus-to-the-CLTK).
    In using this, one can access the most up-to-date ATF documents without
    constantly and manually refreshing their files of said documents.

    Definitely WIP and needs more thought.
    """
    #def __init__(self):
    #    """
    #    :param: empty.
    #    """
