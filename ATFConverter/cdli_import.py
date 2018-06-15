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


class Import(object):
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
    def discern_tablets(__read_file__):
        """
        Using the __read_file__ function, this process separates out tablets
        based off of metadata in the file.
        :param __read_file__: List of strings made up of individual lines of
        file downloaded from CDLI.
        :return: list that separates out disparate texts into lists of strings
        made up of individual lines of file downloaded from CDLI.
        """
