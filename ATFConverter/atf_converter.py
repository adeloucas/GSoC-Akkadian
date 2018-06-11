"""
This module is for converting tokens made from CDLI's ATF-formatted text into a
standard unicode format.

The atf_converter depends upon the word and sign tokenizer outputs. There are
two sets of functions:
1) __convert_consonant__ through process: this function set is for both
   Tokenizer sets.
2) language reader through reader reconstruction: for Tokenizer2 functions
   only.
"""

import re
from unicodedata import normalize

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

VOWELS = 'aeiouAEIOU'
TITTLES = {r's,': chr(0x1E63), r'sz': chr(0x0161), r't,': chr(0x1E6D),
           r"'": chr(0x02BE), r'S,': chr(0x1E62), r'SZ': chr(0x0160),
           r'T,': chr(0x1E6C)}


# noinspection PyUnboundLocalVariable
class ATFConverter(object):
    """
    Transliterates ATF data from CDLI into readable unicode.
        sz = š
        s, = ṣ
        t, = ṭ
        ' = ʾ
        Sign values for 2-3 take accent aigu and accent grave standards,
        otherwise signs are printed as subscript.

    For in depth reading on ATF-formatting for CDLI and ORACC:
        Oracc ATF Primer = http://oracc.museum.upenn.edu/doc/help/editinginatf/
        primer/index.html
        ATF Structure = http://oracc.museum.upenn.edu/doc/help/editinginatf/
        primer/structuretutorial/index.html
        ATF Inline = http://oracc.museum.upenn.edu/doc/help/editinginatf/
        primer/inlinetutorial/index.html
    """
    def __init__(self, two_three=True):
        """
        :param two_three: turns on or off accent marking.
        """
        self.tittles = TITTLES
        self.two_three = two_three

    @staticmethod
    def __convert_consonant__(sign):
        """
        Uses dictionary to replace ATF convention for unicode characters.

        input = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ']
        output = ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ']

        :param sign: string
        :return: string
        """
        for key in TITTLES:
            sign = sign.replace(key, TITTLES[key])
        return sign

    @staticmethod
    def __convert_number_to_subscript__(num):
        """
        Converts number into subscript

        input = ["a", "a1", "a2", "a3", "be2", "be3", "bad2", "bad3"]
        output = ["a", "a₁", "a₂", "a₃", "be₂", "be₃", "bad₂", "bad₃"]

        :param num: number called after sign
        :return: number in subscript
        """
        subscript = ''
        for character in str(num):
            subscript += chr(0x2080 + int(character))
        return subscript

    @staticmethod
    def __get_number_from_sign__(sign):
        """
        Captures numbers after sign for __convert_num__.

        input = ["a", "a1", "be2", "bad3", "buru14"]
        output = [0, 1, 2, 3, 14]

        :param sign: string
        :return: string, integer
        """
        match = re.search(r'\d{1,3}$', sign)
        if match is None:
            number = 0
        else:
            number = match[0]
        return sign, int(number)

    @staticmethod
    def __get_number_from_sign2__(sign):
        """
        Captures numbers after sign for __convert_num__. Alternative method.

        input = ["a", "a1", "be2", "bad3", "buru14"]
        output = [0, 1, 2, 3, 14]

        :param sign: string
        :return: integer
        """
        for i, character in enumerate(sign[1:]):
            # single vowel specifics
            if sign == 'i3':
                return sign, int(sign[1])
            if sign == 'e2':
                return sign, int(sign[1])
            if sign == 'a1':
                return sign, int(sign[1])
            if sign == 'a2':
                return sign, int(sign[1])
            if sign == 'a3':
                return sign, int(sign[1])
            if sign == 'u2':
                return sign, int(sign[1])
            if sign == 'u3':
                return sign, int(sign[1])
            if sign == 'u4':
                return sign, int(sign[1])
            # _x
            if sign[0] == '_':
                # _x_
                if sign[-1] == '_':
                    # _x2_
                    if sign[-2].isdigit():
                        if sign[-3].isdigit():
                            return sign, int(sign[-3:])
                        return sign, int(sign[-2])
                    return sign, 0
                # _x2
                if sign[-1].isdigit():
                    if sign[-2:].isdigit():
                        if sign[-3].isdigit():
                            return sign, int(sign[-3:])
                        return sign, int(sign[-2:])
                    return sign, int(sign[-1])
                return sign, 0
            # x_
            if sign[-1] == '_':
                # x2_
                if sign[-2].isdigit():
                    if sign[-3].isdigit():
                        return sign, int(sign[-3:-1])
                    return sign, int(sign[-2])
                return sign, 0
            # determinatives
            if sign[0] == '{':
                # {x}
                if sign[-1] == '}':
                    # {x2}
                    if sign[-2].isdigit():
                        if sign[-3].isdigit():
                            return sign, int(sign[-3:-2])
                        return sign, int(sign[-2])
                    return sign, 0
            # _0-9
            if sign[0].isdigit():
                # 2(diš)
                if sign[-1] == ")":
                    if sign[-2].isdigit():
                        if sign[-3].isdigit():
                            return sign, int(sign[-3:-2])
                        return sign, int(sign[-2])
                    return sign, 0
                # 2{kiš}
                if sign[-1] == "}":
                    if sign[-2].isdigit():
                        if sign[-3].isdigit():
                            return sign, int(sign[-3:-2])
                        return sign, int(sign[-2])
                    return sign, 0
            if sign[1].isdigit():
                # _3(u2)
                if sign[-2].isdigit():
                    if sign[-3].isdigit():
                        return sign, int(sign[-3:-2])
                    return sign, int(sign[-2])
                # _3(u)
                if sign[-1:] == ")":
                    return sign, 0
                # otherwise
                return sign, 0
            # Standard Sign
            if character.isdigit():
                return sign, int(sign[i+1:])
        return sign, 0

    # noinspection PyUnusedLocal,PyUnboundLocalVariable
    def __convert_num__(self, sign):
        """
        Converts number registered in get_number_from_sign.

        input = ["a2", "☉", "be3"]
        output = ["a₂", "☉", "be₃"]

        :param sign: string
        :return sign: string
        """
        # Check if there's a number at the end
        new_sign, num = self.__get_number_from_sign__(sign)
        if num == '-':
            return new_sign
        if num < 2:  # "ab" -> "ab"
            return new_sign.replace(str(num),
                                    self.__convert_number_to_subscript__(num))
        if num > 3:  # "buru14" -> "buru₁₄"
            return new_sign.replace(str(num),
                                    self.__convert_number_to_subscript__(num))
        if self.two_three:
            return new_sign.replace(str(num),
                                    self.__convert_number_to_subscript__(num))
        else:
            # "bad3" -> "bàd"
            for i, character in enumerate(new_sign):
                new_vowel = ''
                if character in VOWELS:
                    if num == 2:
                        # noinspection PyUnusedLocal
                        new_vowel = character + chr(0x0301)
                    elif num == 3:
                        new_vowel = character + chr(0x0300)
                    break
            return new_sign[:i] + normalize('NFC', new_vowel) + \
                new_sign[i+1:].replace(str(num), '')

    def process(self, text_string):
        """
        Expects a list of tokens, will return the list converted from ATF
        format to print-format.

        input = ["a", "a2", "a3", "geme2", "bad3", "buru14"]
        output = ["a", "á", "à", "géme", "bàd", "buru₁₄"]

        :param text_string: string
        :return: text_string
        """
        output = [self.__convert_num__(self.__convert_consonant__(token)) for
                  token in text_string]
        return output

    @staticmethod
    def language_reader(line):
        """
        Flags signs by language or whether it is a determinative / number, when
        it encounters ATF Conventions. Prints without ATF Conventions.

        input: ['um', 'ma', '_{d}', 'utu_', 'szi', '_{d}', 'iszkur_', 'a',
                'bu', 'ka', 'a', 'ma']
        output: [('akkadian', 'um'), ('akkadian', 'ma'),
                 ('determinative', '{d}'), ('sumerian', 'utu'),
                 ('akkadian', 'szi'), ('determinative', '{d}'),
                 ('sumerian', 'iszkur'), ('akkadian', 'a'),
                 ('akkadian', 'bu'), ('akkadian', 'ka'),
                 ('akkadian', 'a'), ('akkadian', 'ma')]

        :param line: list of signs in line, string
        :return: list of tuples akin to sign_tokenizer (sign, function or
        language)
        """
        language = "akkadian"
        output = []
        for sign in line:
            # -
            if sign == "-":
                output.append(("hyphen", '-'))
            #
            elif sign == " ":
                output.append(("space", ' '))
            # _
            elif sign == "_":
                output.append(("underscore", '_'))
                language = "akkadian"
            # _x_
            elif sign[0] == "_" and sign[-1] == "_":
                output.append(("sumerian", sign[1:-1]))
            # _x}
            elif sign[0] == "_" and sign[-1] == "}":
                output.append(("determinative", sign[1:]))
                language = "sumerian"
            # _x)
            elif sign[0] == '_' and sign[-1] == ')':
                output.append(("number", sign[1:],))
                language = "sumerian"
            # _x
            elif sign[0] == "_":
                language = "sumerian"
                output.append((language, sign[1:]))
            # x)
            elif sign[-1] == ")":
                output.append(("number", sign))
            # x}
            elif sign[-1] == "}":
                output.append(("determinative", sign))
            # x_
            elif sign[-1] == "_":
                output.append(("sumerian", sign[:-1]))
                language = "akkadian"
            # x2
            elif sign[-1].isdigit():
                output.append((language, sign))
            # x
            else:
                output.append((language, sign))
        return output

    @staticmethod
    def underscore_remover(language_reader):
        """
        Removes underscore from the language_reader.

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

        :param language_reader: list of tuples
        :return: list of tuples
        """
        output = [[eval(str(sign).replace(sign[1], '')) if
                   sign[0] == 'underscore' else sign for sign in line] for line
                  in language_reader]
        return output

    @staticmethod
    def sumerian_converter(language_reader):
        """
        Capitalizes Sumerian words in language_reader.

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


        :param language_reader: list of tuples
        :return: list of tuples
        """
        output = [[eval(str(sign).replace(sign[1], sign[1].upper())) if
                   sign[0] == 'sumerian' else sign for sign in line]
                  for line in language_reader]
        return output

    @staticmethod
    def reader_reconstruction(sign_tokenizer_space_and_hyphen):
        """
        Using sign_tokenizer_space_and_hyphen, reconstructs words that
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

        :param sign_tokenizer_space_and_hyphen: Does not work for
        sign_tokenizer2.
        :return: list of lines as strings
        """
        output = [''.join([sign[1] for sign in line])
                  for line in sign_tokenizer_space_and_hyphen]
        return output
