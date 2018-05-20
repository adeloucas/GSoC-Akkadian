__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import re

class ATFConverter(object):
    """Transliterates ATF data from CDLI into readable unicode"""
    def __init__(self):
        """Initialization for ATFConverter, reads replacement tuple"""
        tittles =  [(r's,', 'ṣ'),  (r'S,', 'Ṣ'), (r't,', 'ṭ'), (r'T,', 'Ṭ'), (r'sz', 'š'), (r'SZ', 'Š')]
        
        accents =  [(r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                        (r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'á\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'à\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                        (r'[aA]2', 'á'), (r'[aA]3', 'à'), (r'[aA]([a-zA-Z])2', 'á\\1'), (r'[aA]([a-zA-Z])3', 'à\\1'), 
                        (r'[aA]([ṣṢṭṬšŠ])2', 'á\\1'), (r'[aA]([ṣṢṭṬšŠ])3', 'à\\1'),
                
                        (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                        (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'é\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'è\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                        (r'[eE]2', 'é'), (r'[eE]3', 'è'), (r'[eE]([a-zA-Z])2', 'é\\1'), (r'[eE]([a-zA-Z])3', 'è\\1'),
                        (r'[eE]([ṣṢṭṬšŠ])2', 'é\\1'), (r'[eE]([ṣṢṭṬšŠ])3', 'è\\1'),
                        
                        (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                        (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'í\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ì\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                        (r'[iI]2', 'í'), (r'[iI]3', 'ì'), (r'[iI]([a-zA-Z])2', 'í\\1'), (r'[iI]([a-zA-Z])3', 'ì\\1'),
                        (r'[iI]([ṣṢṭṬšŠ])2', 'í\\1'), (r'[iI]([ṣṢṭṬšŠ])3', 'ì\\1'),
                        
                        (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                        (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ó\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ò\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                        (r'[oO]2', 'ó'), (r'[oO]3', 'ò'), (r'[oO]([a-zA-Z])2', 'ó\\1'), (r'[oO]([a-zA-Z])3', 'ò\\1'),
                        (r'[oO]([ṣṢṭṬšŠ])2', 'ó\\1'), (r'[oO]([ṣṢṭṬšŠ])3', 'ò\\1'),
                        
                        (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                        (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                        (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ú\\1'),
                        (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ù\\1'),
                        (r'[uU]([a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                        (r'[uU]([a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                        (r'[uU]2', 'ú'), (r'[uU]3', 'ù'), (r'[uU]([a-zA-Z])2', 'ú\\1'), (r'[uU]([a-zA-Z])3', 'ù\\1'),
                        (r'[uU]([ṣṢṭṬšŠ])2', 'ú\\1'), (r'[uU]([ṣṢṭṬšŠ])3', 'ù\\1'),

                        (r'([a-zA-ZṣṢṭṬšŠ])4', '\\1₄'), (r'([a-zA-ZṣṢṭṬšŠ])5', '\\1₅'), (r'([a-zA-ZṣṢṭṬšŠ])6', '\\1₆'), 
                        (r'([a-zA-ZṣṢṭṬšŠ])7', '\\1₇'), (r'([a-zA-ZṣṢṭṬšŠ])8', '\\1₈'), (r'([a-zA-ZṣṢṭṬšŠ])9', '\\1₉'), 
                        (r'([a-zA-ZṣṢṭṬšŠ])10', '\\1₁₀'), (r'([a-zA-ZṣṢṭṬšŠ])11', '\\1₁₁'), (r'([a-zA-ZṣṢṭṬšŠ])12', '\\1₁₂'), 
                        (r'([a-zA-ZṣṢṭṬšŠ])13', '\\1₁₃'), (r'([a-zA-ZṣṢṭṬšŠ])14', '\\1₁₄'), (r'([a-zA-ZṣṢṭṬšŠ])15', '\\1₁₅'), 
                        (r'([a-zA-ZṣṢṭṬšŠ])16', '\\1₁₆'),(r'([a-zA-ZṣṢṭṬšŠ])17', '\\1₁₇'), (r'([a-zA-ZṣṢṭṬšŠ])18', '\\1₁₈')]
        
        determinatives = [(r'{d}', 'ᵈ'), (r'{diš}', '𒁹'), (r'{disz}', '𒁹'), (r'{geš}', 'ᵍᵉˢᶻ'), (r'{gesz}', 'ᵍᵉˢᶻ'),
                          (r'{iri}', 'ⁱʳⁱ'), (r'{ki}', 'ᵏⁱ'), (r'{kuš}', 'ᵏᶸˢᶻ'), (r'{nisi}', 'ⁿⁱˢⁱ'), (r'{uruda}', 'ᵘʳᵘᵈᵃ'),
                          (r'{lu2}', 'ˡᶸ²'), (r'{lú}', 'ˡᶸ²'), (r'{munus}', 'ᵐᶸⁿᶸˢ'), (r'{še}', 'ˢᶻᵉ'), (r'{uzu}', 'ᶸᶻᶸ'),
                          (r'\(u\)', '(𒌋)'), (r'\(diš\)', '(𒁹)'), (r'\(disz\)', '(𒁹)'), (r'{sze}', 'ˢᶻᵉ'), (r'{lú#}', 'ˡᶸ²#'),
                          (r'{kusz}', 'ᵏᶸˢᶻ'), (r'{ansze}', 'ᵃⁿˢᶻᵉ'), (r'{esz2}', 'ᵉˢᶻ²'), (r'{gi}', 'ᵍⁱ'),
                          (r'{is}', 'ⁱˢ'), (r'{i₇}', 'ⁱ⁷'), (r'{I₇}', 'ⁱ⁷'), (r'{geš#}', 'ᵍᵉˢᶻ#'), (r'\(aš\)', '(𒀸)'),
                          (r'\(bùr\)', '(𒌋)'), (r'\(bán\)', '(𒑏)'), (r'\(barig\)', '(𒁀𒌷𒂵)'), (r'\(géš\)', '(𒁹)')]

        sumerian = [#_w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    #_w w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    #_w w w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    #_w w w w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    #_w w w w w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    #_w w w w w w_
                    (r'([\_][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\[\]\<\>\(\)\?\#\!\|\s\-][\w\d\[\]\<\>\(\)\?\#\!\|.]+[\_])', '\\1'),
                    ]
                        
        akkadian = [#_ w _
                    (r'([\_][\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\[\]\<\>\(\)\?\#\!\s\-][\_])', '\\1'),
                    #_ w w _
                    (r'([\_][\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\[\]\<\>\(\)\?\#\!\s\-][\_])', '\\1'),
                    #_ w w w _
                    (r'([\_][\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-[^_].]+[\[\]\<\>\(\)\?\#\!\s\-][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\[\]\<\>\(\)\?\#\!\s\-][\_])', '\\1'),
                    #_ w [_ (ex: 40. _GU₄_ KI-MA [_GU₄_])
                    (r'([\_][\s][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\s][\[][\_])', '\\1'),
                    #_] w w [_ (ex: 37. šum-ma# [_GU₄_] Ù LU [_UDU)
                    (r'([\_][\]][\s][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\s][\w\d\[\]\<\>\(\)\?\#\!\-.]+[\s][\[][\_])', '\\1'),
                    ]
                    
        self.tittles = \
                [(re.compile(regex), repl) for (regex, repl) in tittles]
        
        self.accents = \
                [(re.compile(regex), repl) for (regex, repl) in accents]

        self.determinatives = \
                [(re.compile(regex), repl) for (regex, repl) in determinatives]
        
        self.sumerian = \
                [(re.compile(regex), lambda sumerian: sumerian.group(0).upper()) for (regex, repl) in sumerian]

        self.akkadian = \
                [(re.compile(regex), lambda akkadian: akkadian.group(0).lower()) for (regex, repl) in akkadian] 

    def convert(self, text):
        """Converts characters into unicode"""   
        for (pattern, repl) in self.tittles:
            text = re.subn(pattern, repl, str(text))[0]

        for (pattern, repl) in self.accents:
            text = re.subn(pattern, repl, str(text))[0]

        for (pattern, repl) in self.determinatives:
            text = re.subn(pattern, repl, str(text))[0]    

        for (pattern, repl) in self.sumerian:
            text = re.subn(pattern, repl, str(text))[0]   

        for (pattern, repl) in self.akkadian:
            text = re.subn(pattern, repl, str(text))[0]
        
        return text 