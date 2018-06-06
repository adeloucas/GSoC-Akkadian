__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

from unicodedata import normalize

VOWELS = 'aeiou'
tittles = {r's,': chr(0x1E63), r'sz': chr(0x0161),  r't,': chr(0x1E6D),
           r'S,': chr(0x1E62), r'SZ': chr(0x0160), r'T,': chr(0x1E6C)}

class ATFConverter(object):
    """Transliterates ATF data from CDLI into readable unicode."""
    def __init__(self, two_three=True):
        self.tittles = tittles
        self.two_three = two_three

    def __convert_consonant__(self, sign):
        """Uses dictionary to replace ATF convention for unicode characters."""
        for key in tittles:
            sign = sign.replace(key, tittles[key])
        return sign

    def __convert_number_to_subscript__(self, num):
        """Converts number into subscript"""
        subscript = ''
        for c in str(num):
            subscript += chr(0x2080 + int(c))
        return subscript

    def __get_number_from_sign__(self, sign):
        """Reads sign number in order to be converted."""
        for i, c in enumerate(sign[1:]):
            """u2, a2,"""
            if sign == 'i3':
                return (sign, int(sign[1]))
            if sign == 'e2':
                return (sign, int(sign[1]))
            if sign == 'a1':
                return (sign, int(sign[1]))
            if sign == 'a2':
                return (sign, int(sign[1]))
            if sign == 'a3':
                return (sign, int(sign[1]))
            if sign == 'u2':
                return (sign, int(sign[1]))
            if sign == 'u3':
                return (sign, int(sign[1]))
            if sign == 'u4':
                return (sign, int(sign[1]))
            """_x"""
            if sign[0] == '_':
                """_x_"""
                if sign[-1] == '_':
                    """_x2_"""
                    if sign[-2].isdigit():
                        if sign[-3:].isdigit():
                            return (sign, int(sign[-3:]))
                        return (sign, int(sign[-2]))
                    return (sign, 0)
                """_x2"""
                if sign[-1].isdigit():
                    if sign[-2:].isdigit():
                        return (sign, int(sign[-2:]))
                    return (sign, int(sign[-1]))
                return (sign, 0)
            """x_"""
            if sign[-1] =='_':
                """x2_"""
                if sign[-2].isdigit():
                    return (sign, int(sign[-2]))
                return (sign, 0)
            """determinatives"""
            if sign[0] == '{':
                """{x}"""
                if sign[-1] == '}':
                    """{x2}"""
                    if sign[-2].isdigit():
                        return (sign, int(sign[-2]))
                    return (sign, 0)
            """_\d"""
            if sign[0].isdigit():
                """2(diš)"""
                if sign[-1] == ")":
                    if sign[-2].isdigit():
                        return (sign, int(sign[-2]))
                    return (sign, 0)
                """2{kiš}"""
                if sign[-1] == "}":
                    if sign[-2].isdigit():
                        return (sign, int(sign[-2]))
                    return (sign, 0)
            if sign[1].isdigit():
                """_3(u2)"""
                if sign[-2].isdigit():
                    return (sign, int(sign[-2]))
                """_3(u)"""
                if sign[-1:] == ")":
                    return (sign, 0)
                """otherwise"""
                return (sign, 0)
            """Standard Sign"""
            if c.isdigit():
                return (sign, int(sign[i+1:]))    #issue == double decimals
        return (sign, 0)

    def __convert_num__(self, sign):
        """Converts number registered in get_number_from_sign."""
        # Check if there's a number at the end
        new_sign, num = self.__get_number_from_sign__(sign)
        if num == '-':
            return new_sign
        if num < 2:  # "ab" -> "ab"
            return new_sign.replace(str(num), self.__convert_number_to_subscript__(num))
        if num > 3:  # "buru14" -> "buru₁₄"
            return new_sign.replace(str(num), self.__convert_number_to_subscript__(num))
        if self.two_three:
            return new_sign.replace(str(num), self.__convert_number_to_subscript__(num))
        else:
            # "bad3" -> "bàd"
            for i, c in enumerate(new_sign):
                new_vowel = ''
                if c in VOWELS:
                    if num == 2:
                        new_vowel = c + chr(0x0301)
                    elif num == 3:
                        new_vowel = c + chr(0x0300)
                    break
            return new_sign[:i] + normalize('NFC', new_vowel) + new_sign[i+1:].replace(str(num), '')

    def process(self, text_string):
        """Expects a list of tokens, will return the list converted from ATF format to print-format"""
        output = []
        for token in text_string:
            output.append(self.__convert_num__(self.__convert_consonant__(token)))
        return output

    def language_reader(self, words):
        """Flags signs by language or whether it is a determintive / number, when it encounters ATF Conventions.
        Prints without ATF Conventions."""
        language = "akkadian"
        output = []
        for sign in words:
            #-
            if sign == "-":
                output.append(("hyphen", '-'))
            #
            elif sign == " ":
                output.append(("space", ' '))
            #_
            elif sign == "_":
                output.append(("underscore", '_'))
                language = "akkadian"
            #_x_
            elif sign[0] == "_" and sign[-1] == "_":
                output.append(("sumerian", sign[1:-1]))
            #_x}
            elif sign[0] == "_" and sign[-1] == "}":
                output.append(("determinative", sign[1:]))
                language = "sumerian"
            #_x)
            elif sign[0] == '_' and sign[-1] == ')':
                output.append(("number", sign[1:],))
                language = "sumerian"
            #_x
            elif sign[0] == "_":
                language = "sumerian"
                output.append((language, sign[1:]))
            #x)
            elif sign[-1] == ")":
                output.append(("number", sign))
            #x}
            elif sign[-1] == "}":
                output.append(("determinative", sign))
            #x_
            elif sign[-1] == "_":
                output.append(("sumerian", sign[:-1]))
                language = "akkadian"
            #x2
            elif sign[-1].isdigit():
                output.append((language, sign))
            #x
            else:
                output.append((language, sign))
        return output

    def sumerian_converter(self, language_reader):
        output = [[eval(str(sign).replace(sign[1], sign[1].upper())) if sign[0] == 'sumerian' else sign for sign in line] for line in language_reader]
        return output

    def reader_reconstruction(self, sign_tokenizer_space_and_hyphen_incl):
        """Using sign_tokenizer_space_and_hyphen_incl, reconstructs words that have hyphens connecting them."""
        output = []
        for line in sign_tokenizer_space_and_hyphen_incl:
            reconstruct = [sign[1] for sign in line]
            output.append(''.join(reconstruct))
        return output