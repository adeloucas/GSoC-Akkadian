__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import re
from unicodedata import normalize

VOWELS = 'aeiou'
determinatives = {r'{d}': 'ᵈ', r'{diš}': '𒁹', r'{disz}': '𒁹', r'{geš}': 'ᵍᵉˢᶻ', r'{gesz}': 'ᵍᵉˢᶻ',
                  r'{iri}': 'ⁱʳⁱ', r'{ki}': 'ᵏⁱ', r'{kuš}': 'ᵏᶸˢᶻ', r'{nisi}': 'ⁿⁱˢⁱ', r'{uruda}': 'ᵘʳᵘᵈᵃ',
                  r'{lu2}': 'ˡᶸ²', r'{lú}': 'ˡᶸ²', r'{munus}': 'ᵐᶸⁿᶸˢ', r'{še}': 'ˢᶻᵉ', r'{uzu}': 'ᶸᶻᶸ',
                  r'(u)': '(𒌋)', r'(diš)': '(𒁹)', r'(disz)': '(𒁹)', r'{sze}': 'ˢᶻᵉ', r'{lú#}': 'ˡᶸ²#',
                  r'{kusz}': 'ᵏᶸˢᶻ', r'{ansze}': 'ᵃⁿˢᶻᵉ', r'{esz2}': 'ᵉˢᶻ²', r'{gi}': 'ᵍⁱ',
                  r'{is}': 'ⁱˢ', r'{i7}': 'ⁱ⁷', r'{I7}': 'ⁱ⁷', r'{geš#}': 'ᵍᵉˢᶻ#', r'(aš)': '(𒀸)',
                  r'(bùr)': '(𒌋)', r'(bán)': '(𒑏)', r'(barig)': '(𒁀𒌷𒂵)', r'(géš)': '(𒁹)'}
tittles = {r's,': chr(0x1E63), r'sz': chr(0x0161),  r't,': chr(0x1E6D),
           r'S,': chr(0x1E62), r'SZ': chr(0x0160), r'T,': chr(0x1E6C)}

class ATFConverter(object):
    """Transliterates ATF data from CDLI into readable unicode."""
    def __init__(self, two_three=True):
        self.tittles = tittles
        self.determinatives = determinatives
        self.two_three = two_three

    def convert_consonant(self, sign):
        """Uses dictionary to replace ATF convention for unicode characters."""
        for key in tittles:
            sign = sign.replace(key, tittles[key])
        return sign

    def convert_determinatives(self, sign):
        """Uses dictionary to reformat determinatives."""
        for key in determinatives:
            sign = [d.replace(key, determinatives[key]) for d in sign]
        return sign

    def convert_sumerian(self, sumerian):   #Change to "when language = sumerian..."
        """Takes Sumerian from Tokenizer, uppercases it, and replaces hyphens for periods."""
        output = []
        for line in sumerian:
            output.append(re.subn('-', '.', line.upper())[0])
        return output

    def convert_number_to_subscript(self, num):
        """Converts number into subscript"""
        subscript = ''
        for c in str(num):
            subscript += chr(0x2080 + int(c))
        return subscript

    def get_number_from_sign(self, sign):
        """Reads sign number in order to be converted."""
        for i, c in enumerate(sign[1:]):
            """_x"""
            if sign[0] == '_':
                """_x_"""
                if sign[-1] == '_':
                    """_x2_"""
                    if sign[-2].isdigit():
                        if sign[-3:].isdigit():             #for _buru14_ (not working)
                            return (sign, int(sign[-3:]))
                        return (sign, int(sign[-2]))
                    return (sign, 0)
                """_x2"""
                if sign[-1].isdigit():
                    if sign[-2:].isdigit():             ##Should be implemented on every level -- for double digits! ('_sa10')
                        return (sign, int(sign[-2:]))
                    return (sign, int(sign[-1]))
                return (sign, 0)
            """x_"""
            if sign[-1] =='_':
                """x2_"""
                if sign[-2].isdigit():
                    return (sign, int(sign[-2]))
                return (sign, 0)
            """u2, a2,"""
            #if sign[0].isalpha and sign[-1].isdigit and sign[0] == sign[-2]:
            #    return (sign, int(sign[1]))
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

    def convert_num(self, sign):
        """Converts number registered in get_number_from_sign."""
        # Check if there's a number at the end
        new_sign, num = self.get_number_from_sign(sign)
        if num == '-':
            return new_sign
        if num < 2:  # "ab" -> "ab"
            return new_sign.replace(str(num), self.convert_number_to_subscript(num))
        if num > 3:  # "buru14" -> "buru₁₄"
            return new_sign.replace(str(num), self.convert_number_to_subscript(num))
        if self.two_three:
            #return new_sign + self.convert_number_to_subscript(num)
            return new_sign.replace(str(num), self.convert_number_to_subscript(num))
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
            output.append(self.convert_num(self.convert_consonant(token)))
        return output

    def cdli_language_breakdown(self, words):
        """Flags signs by language, or whether it is a determintive or number, when it encounters ATF Conventions.
        Deletes ATF Conventions."""
        language = "akkadian"
        output = []
        for sign in words:
            #"""-"""
            if sign == "-":
                output.append(("hyphen", '-'))
            #""" """
            elif sign == " ":
                output.append(("space", ' '))
            #"""_"""
            elif sign == "_":
                output.append(("underscore", '_'))
                language = "akkadian"
            #"""_x_"""
            elif sign[0] == "_" and sign[-1] == "_":
                output.append(("sumerian", sign[1:-1]))
            #"""_x}"""
            elif sign[0] == "_" and sign[-1] == "}":
                output.append(("determinative", sign[1:]))
                language = "sumerian"
            #"""_x)"""
            elif sign[0] == '_' and sign[-1] == ')':
                output.append(("number", sign[1:],))
                language = "sumerian"
            #"""_x"""
            elif sign[0] == "_":
                language = "sumerian"
                output.append((language, sign[1:]))
            #"""x)"""
            elif sign[-1] == ")":
                output.append(("number", sign))
            #"""x}"""
            elif sign[-1] == "}":
                output.append(("determinative", sign))
            #"""x_"""
            elif sign[-1] == "_":
                output.append(("sumerian", sign[:-1]))
                language = "akkadian"
            #"""x2"""
            elif sign[-1].isdigit():
                output.append((language, sign))
            #"""x"""
            else:
                output.append((language, sign))
        return output

    def sumerian_reconstruct(self, breakdown):   #Change to "when language = sumerian..."
        """Takes Sumerian from breakdown, uppercases it, and replaces hyphens for periods."""
        output = []
        for line in breakdown:
            reconstruct = [sign[0] for sign in line]
            d = dict(line)
            for key in d.keys():
                if key == 'sumerian':
                    output.append(str(d.get('sumerian')).upper())
                else:
                    output.append(key)
        return output

    def word_reconstruction(self, breakdown):
        """Using signs_for_breakdown for breakdown, reconstructs words that have hyphens connecting them."""
        output = []
        for line in breakdown:
            reconstruct = [sign[1] for sign in line] #changed!
            output.append(''.join(reconstruct))
        return output

    def breakdown_reviewer(self, lines, words, reconstruct, breakdown):
        output = list(zip(lines, words, reconstruct, breakdown))
        checker = '\n\n'.join('\n'.join(str(line) for line in x) for x in output)
        return checker