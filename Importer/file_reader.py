"""
This module is for creating disparate texts out of CDLI's "download all text"
option: (https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text (e.g. Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions (e.g. ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01).

The goal of this feature is to be able to separate out text files on a
'case-by-case' standard; this feature sets up the ability to work with
cuneiform text(s) one-on-one whether it is Code of Hammurabi, a collection of
texts such as ARM01, or whatever your search function desires.
"""

from Importer.file_importer import FileImport

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class FileReader(object):
    """
    The goal of this class is to take a file downloaded from CDLI's website
    (https://cdli.ucla.edu/search/download_data_new.php?data_type=all)
    and prepare it for text-by-text analysis. It separates out from a file
    instances into disparate texts, should the file contain several texts
    within one file (e.g. ARM1Akkadian.txt has 139 unique tablets within its
    one file, whereas Akkadian.txt contains only one "tablet").
    """
    def __init__(self, filename):
        """
        :param cdli_corpus: This can be downloaded through CLTK. The file is
        saved as "cdli_atfunblocked.atf" and can be renamed locally
        as a .txt with usable with no other changes; see README for more info.
        """
        self.filename = filename

    def table_of_contents(self):
        """
        Uses
        :param text_file: This is the text file that you downloaded from
        CDLI.
        :return: list of lists containing CDLI Number and text edition name.
        """
        output = []
        try:
            header = FileImport(self.filename).__discern_texts__()
            for string in header:
                if len(string) > 1:
                    splitstring = string.split('=')
                    pnum = splitstring[0].rstrip()
                    edition = splitstring[1].lstrip()
                    output.append([string, pnum, edition])  # pylint: disable =expression-not-assigned
                else:
                    pnum = header[0].rstrip()
                    output.append(pnum)
            return output
        except IndexError:
            print("No header information in text: {}".format(
                self), repr(self))

    def __text_contents__(self):
        """
        Using the read_file function, this process utilizes __discern_texts__
        and __split_texts__ in order to create a dictionary of texts from
        the text_file.

        i.e. discern_texts for key; split_texts for value:
        {'&P254203 = ARM 01, 002': ["&P254203 = ARM 01, 002",
                                    "#atf: lang akk",
                                    "@tablet"
                                    "etc."]}

        :return: Dictionary of disparate texts in a file with line containing a
        CDLI number and published name of text as key & said text as its value.
        """
        key = FileImport.__text_call_names__(self.filename)
        value = list(FileImport.__split_texts__(self.filename))
        double_value = [value[i//2] for i in range(len(value)*2)]
        texts = zip(key, double_value)
        text_dict = dict(texts)
        return text_dict

    def text_print(self, key):
        """
        Using text_contents, select the respective key you wish to print for
        tokenization or pretty printing.

        i.e.:
        texts = file_import.__text_contents__(text_file)
        text_print(texts, '&P254203 = ARM 01, 002')

        :param text_file: This is the text text_file that you downloaded from
        CDLI.
        :param key: This either text edition name or CDLI number found in
        __text_call_names__
        :return:
        """
        output = self.__text_contents__()
        return output.get(key, '')
