"""
This module is for working on disparate texts out of CDLI's "download all text"
option: (https://cdli.ucla.edu/search/download_data_new.php?data_type=all).

At current, one can produce either one text (e.g. Code of Hammurabi:
https://cdli.ucla.edu/search/search_results.php?ObjectID=P249253)
or a variety of texts via search functions (e.g. ARM 01 publication:
https://cdli.ucla.edu/search/search_results.php?PrimaryPublication=ARM+01).

This feature enables one to work with individual cuneiform texts, whether it is
the Code of Hammurabi, a collection of texts such as ARM01, or whatever your
research desires.
"""

from Importer.file_importer import FileImport

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class CDLIText(object):
    """
    This method makes practical use out of FileImport; it creates the ability
    to search through a text file, select and print individual texts, and
    prepares text to be put through the ATFConverter, Tokenizer, Lemmatizer,
    and PrettyPrinter.
    """
    def __init__(self, filename):
        """
        :param cdli_corpus: This file is downloaded through CLTK. The file is
        saved as "cdli_atfunblocked.atf" and can be renamed locally as a usable
        .txt file; see README for more info.
        """
        self.filename = filename

    def table_of_contents(self):
        """
        Takes key made in __discern_texts__ and separates out cdli_number and
        its edition.
        :return: List containing text file's text edition and CDLI number.
        """
        output = []
        header = FileImport(self.filename).__discern_texts__()
        for string in header:
            if len(string) > 1:
                splitstring = string.split('=')
                pnum = splitstring[0].rstrip()
                edition = splitstring[1].lstrip()
                output.append(f'{edition}: {pnum}')
            elif len(string) == 1:
                pnum = header[0].rstrip()
                output.append(pnum)
            else:
                output.append('No header information in text!'.format())
        return output

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
        key = FileImport.__call_names__(self.filename)
        value = list(FileImport.__split_texts__(self.filename))
        double_value = [value[i//2] for i in range(len(value)*2)]
        texts = zip(key, double_value)
        text_dict = dict(texts)
        return text_dict

    def text_print(self, key):
        """
        Using FileImport's __text_contents__, selects the respective text you
        wish to print.

        :param key: This either text edition name or CDLI number found in the
        function table_of_contents, e.g: ('&P254203') or ('ARM 01, 002').
        :return: Text as string.
        """
        output = self.__text_contents__()
        return output.get(key, '')
