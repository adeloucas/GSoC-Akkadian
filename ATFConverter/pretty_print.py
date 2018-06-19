"""
This module is for printing ATF data in a aesthetically pleasing way based
off standard print publication of tablets. Currently, this feature utilizes
print_sign_tokenizer within the tokenizer feature of this project.

The goal is to create a class that takes the ATF converter and utilizes the
ability to print damaged characters as well as metadata in such a way that ATF
data can be presented in an easy-to-print manner ready for teaching or article
publication.
"""

import re

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class PrettyPrint(object):
    """
    This class takes print_sign_language and makes changes to the text so that
    the text will print in a recognizable way.
    """
    def __init__(self):
        """
        :param: empty for now.
        """

    @staticmethod
    def underscore_remover(print_sign_language):
        """
        Removes underscore from print_sign_language.

        input: [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                 ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                 ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                 ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                 ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                 ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                 ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]
        output: [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                 ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                 ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                 ('underscore', ''), ('space', ' '), ('akkadian', 'i'),
                 ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                 ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                 ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]

        :param print_sign_language: list of tuples
        :return: list of tuples
        """
        output = [[(sign[0], sign[1].replace(sign[1], '')) if
                   sign[0] == 'underscore' else
                   sign for sign in line] for line in print_sign_language]
        return output

    @staticmethod
    def sumerian_converter(print_sign_language):
        """
        Capitalizes Sumerian words in print_sign_language.

        input: [[('sumerian', 'u₄'), ('space', ' '), ('number', '2(diš)'),
                ('hyphen', '-'), ('sumerian', 'kam'), ('space', ' '),
                ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'kam'),
                ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                ('sumerian', 'é'), ('hyphen', '-'), ('sumerian', 'hi'),
                ('hyphen', '-'), ('sumerian', 'a'), ('hyphen', '-'),
                ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]
        output: [[('sumerian', 'U₄'), ('space', ' '), ('number', '2(diš)'),
                 ('hyphen', '-'), ('sumerian', 'KAM'), ('space', ' '),
                 ('number', '3(diš)'), ('hyphen', '-'), ('sumerian', 'KAM'),
                 ('underscore', '_'), ('space', ' '), ('akkadian', 'i'),
                 ('hyphen', '-'), ('akkadian', 'na'), ('space', ' '),
                 ('sumerian', 'É'), ('hyphen', '-'), ('sumerian', 'HI'),
                 ('hyphen', '-'), ('sumerian', 'A'), ('hyphen', '-'),
                 ('akkadian', 'šu'), ('hyphen', '-'), ('akkadian', 'nu')]]


        :param print_sign_language: list of tuples
        :return: list of tuples
        """
        output = [[(sign[0], sign[1].upper()) if sign[0] == 'sumerian' else
                   sign for sign in line] for line in print_sign_language]
        return output

    @staticmethod
    def reader_reconstruction(print_sign_tokenizer):
        """
        Using print_sign_tokenizer, reconstructs words that
        have hyphens connecting them.

        input: [('sumerian', 'a'), ('hyphen', '-'), ('sumerian', 'šà'),
                ('hyphen', '-'), ('sumerian', 'hi'), ('hyphen', '-'),
                ('sumerian', 'a'), ('space', ' '), ('akkadian', 'ša'),
                ('space', ' '), ('akkadian', 'a'), ('hyphen', '-'),
                ('akkadian', 'ah'), ('space', ' '), ('determinative', '{d}'),
                ('akkadian', 'buranun'), ('hyphen', '-'), ('akkadian', 'na'),
                ('space', ' '), ('akkadian', 'a'), ('hyphen', '-'),
                ('akkadian', 'na'), ('space', ' '), ('akkadian', 'za'),
                ('hyphen', '-'), ('akkadian', 'zi'), ('hyphen', '-'),
                ('akkadian', 'im')]
        output: ['a-šà-hi-a ša a-ah {d}buranun-na a-na za-zi-im']

        :param print_sign_tokenizer: Does not work for
        sign_tokenizer.
        :return: list of lines as strings
        """
        output = [''.join([sign[1] for sign in line])
                  for line in print_sign_tokenizer]
        return output
