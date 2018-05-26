__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
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
tittles =  {r's,': 'ṣ',  r'S,': 'Ṣ', r't,': 'ṭ', r'T,': 'Ṭ', r'sz': 'š', r'SZ': 'Š'}

class ATFConverter(object):
    """Transliterates ATF data from CDLI into readable unicode"""
    def __init__(self, two_three=True):
        self.two_three = two_three
        self.determinatives = determinatives
        self.tittles = tittles
   
    def convert_number_to_subscript(self, num):
        subscript = ''
        for c in str(num):
            subscript += chr(0x2080 + int(c))
        return subscript

    def get_number_from_sign(self, sign):
        for i, c in enumerate(sign):
            if c.isdigit():
                return (sign[:i], int(sign[i:]))
        return (sign, 0)

    def convert_num(self, sign):
        # Check if there's a number at the end
        new_sign, num = self.get_number_from_sign(sign)
        if num < 2:  # "ab" -> "ab"
            return new_sign
        if num > 3:  # "buru14" -> "buru₁₄"
            return new_sign + self.convert_number_to_subscript(num)

        if self.two_three:
            return new_sign + self.convert_number_to_subscript(num)
        else:
            # "bad3" -> "bàd"
            for i, c in enumerate(new_sign):
                if c in VOWELS:
                    new_vowel = ''
                    if num == 2:
                        new_vowel = c + chr(0x0301)
                    elif num == 3:
                        new_vowel = c + chr(0x0300)
                    break
            return new_sign[:i] + normalize('NFC', new_vowel) + new_sign[i+1:]

    def determination(self, sign):
        for key in determinatives:
            sign = sign.replace(key, determinatives[key])
        return sign

    def convert_consonant(self, sign):
        for key in tittles:
            sign = sign.replace(key, tittles[key])
        return sign

    def process(self, text_string):
        """
        Expects a list of tokens, will return the list converted from
        ATF format to print-format
        """

        output = []

        for token in text_string:
            output.append(self.convert_num(self.convert_consonant(token)))
        return output