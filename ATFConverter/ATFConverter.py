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
sumword =  r'[\w\d\[\]\<\>\(\)\?\#\!\|\{\}.]+'
sumspace = r'[\[\]\<\>\(\)\?\#\!\|\s\-]'
akkspace = r'[\[\]\<\>\(\)\?\#\!\s\-]'
akkword = r'[\w\d\[\]\<\>\(\)\?\#\!.]+'
sumerian = [#_w_
            (r'([\_]'+sumword+r'[\_])', '\\1'),
            #_w w_
            (r'([\_]'+sumword+sumspace+sumword+r'[\_])', '\\1'),
            #_w w w_
            (r'([\_]'+sumword+sumspace+sumword+sumspace+sumword+r'[\_])', '\\1'),
            #_w w w w_
            (r'([\_]'+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+r'[\_])', '\\1'),
            #_w w w w w_
            (r'([\_]'+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+r'[\_])', '\\1'),
            #_w w w w w w_
            (r'([\_]'+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+sumspace+sumword+r'[\_])', '\\1')]                     
akkadian = [#_ w _
            (r'([\_]'+akkspace+akkword+akkspace+r'[\_])', '\\1'),
            #_ w w _
            (r'([\_]'+akkspace+akkword+akkspace+akkword+akkspace+r'[\_])', '\\1'),
            #_ w w w _
            (r'([\_]'+akkspace+akkword+akkspace+akkword+akkspace+akkword+akkspace+r'[\_])', '\\1'),
            #_ w [_ (ex: 40. _GU₄_ KI-MA [_GU₄_])
            (r'([\_][\s]'+akkword+r'[\s][\[][\_])', '\\1'),
            #_] w w [_ (ex: 37. šum-ma# [_GU₄_] Ù LU [_UDU)
            (r'([\_][\]][\s]'+akkword+r'[\s]'+akkword+r'[\s][\[][\_])', '\\1')] 

class ATFConverter(object):
    """Transliterates ATF data from CDLI into readable unicode"""
    def __init__(self, two_three=True):
        self.two_three = two_three
        self.determinatives = determinatives
        self.tittles = tittles
        self.sumerian = \
                [(re.compile(regex), lambda sumerian: sumerian.group(0).upper()) for (regex, repl) in sumerian]
        self.akkadian = \
                [(re.compile(regex), lambda akkadian: akkadian.group(0).lower()) for (regex, repl) in akkadian]
        
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
        #this doesn't work:
        #   if c.isdigit() not in ignore    # -> r'[\d]+[\.]' (e.g. lines 1., 2., not sza3, arad2)

    def convert_sign(self, sign):
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

    def process(self, text_string):
        """
        Expects a list of tokens, will return the list converted from
        ATF format to print-format
        """
        output = []

        for token in text_string:
            try:
                output.append(self.convert_sign(token))
            except KeyError:
                print("No conversion rule for: {}".format(token))
                output.append("ERROR: ({})".format(token))
        return output

    def determination(self, text):
        for key in determinatives:
            text = text.replace(key, determinatives[key])
        return text

    def consonants(self, text):
        for key in tittles:
            text = text.replace(key, tittles[key])
        return text 

    def sumerianization(self, text):
        
        for (pattern, repl) in self.sumerian:
            text = re.subn(pattern, repl, str(text))[0]   
        for (pattern, repl) in self.akkadian:
            text = re.subn(pattern, repl, str(text))[0]

        return text 
