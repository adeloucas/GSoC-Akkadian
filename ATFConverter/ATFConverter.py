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
                        return (sign, int(sign[-2]))
                    return (sign, 0)
                """_x2"""
                if sign[-1].isdigit():
                    return (sign, int(sign[-1]))
                return (sign, 0)
            """x_"""
            if sign[-1] =='_':
                """x2_"""
                if sign[-2].isdigit():
                    return (sign, int(sign[-2]))
                return (sign, 0)
            """u2, a2,"""
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
            #"""_"""
            if sign == "_":
                output.append(('_', "CDLI marker"))
                language = "akkadian"
            #"""_x_"""
            elif sign[0] == "_" and sign[-1] == "_":
                output.append((sign[1:-1], "sumerian"))
            #"""_x}"""
            elif sign[0] == "_" and sign[-1] == "}":
                output.append((sign[1:], "determinative"))
                language = "sumerian"
            #"""_x)"""
            elif sign[0] == '_' and sign[-1] == ')':
                output.append((sign[1:], "number"))
                language = "sumerian"
            #"""_x"""
            elif sign[0] == "_":
                language = "sumerian"
                output.append((sign[1:],language))
            #"""x)"""
            elif sign[-1] == ")":
                output.append((sign,"number"))
            #"""x}"""
            elif sign[-1] == "}":
                output.append((sign,"determinative"))
            #"""x_"""
            elif sign[-1] == "_":
                output.append((sign[:-1], "sumerian"))
                language = "akkadian"
            #"""x2"""
            elif sign[-1].isdigit():
                output.append((sign, language))
            #"""x"""
            else:
                output.append((sign,language))
        return output

    def word_reconstruction(self, words, breakdown):
        """takes the newly created tuples from cdli_language_breadown and inserts sign"""
        #from Tokenizer.words, creates and uses a list to switch signs with breakdown