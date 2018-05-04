__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import os
import unittest
import re

class ATFConverter(object): 
    def __init___(self):
        tittles =  [(r's,', 'ṣ'),  (r'S,', 'Ṣ'), (r't,', 'ṭ'), (r'T,', 'Ṭ'), (r'sz', 'š'), (r'SZ', 'Š')]
        
        accents =  [(r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                        (r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'á\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'à\\1'),
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                        (r'[aA]'r'([a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                        (r'[aA]2', 'á'), (r'[aA]3', 'à'), (r'[aA]([a-zA-Z])2', 'á\\1'), (r'[aA]([a-zA-Z])3', 'à\\1'), 
                        (r'[aA]([sStT])([zZ,])2', 'á\\1\\2'), (r'[aA]([sStT])([zZ,])3', 'à\\1\\2'),
                
                        (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                        (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'é\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'è\\1'),
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                        (r'[eE]'r'([a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                        (r'[eE]2', 'é'), (r'[eE]3', 'è'), (r'[eE]([a-zA-Z])2', 'é\\1'), (r'[eE]([a-zA-Z])3', 'è\\1'),
                        (r'[eE]([sStT])([zZ,])2', 'é\\1\\2'), (r'[eE]([sStT])([zZ,])3', 'è\\1\\2'),
                        
                        (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                        (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'í\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ì\\1'),
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                        (r'[iI]'r'([a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                        (r'[iI]2', 'í'), (r'[iI]3', 'ì'), (r'[iI]([a-zA-Z])2', 'í\\1'), (r'[iI]([a-zA-Z])3', 'ì\\1'),
                        (r'[iI]([sStT])([zZ,])2', 'í\\1\\2'), (r'[iI]([sStT])([zZ,])3', 'ì\\1\\2'),
                        
                        (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                        (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ó\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ò\\1'),
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                        (r'[oO]'r'([a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                        (r'[oO]2', 'ó'), (r'[oO]3', 'ò'), (r'[oO]([a-zA-Z])2', 'ó\\1'), (r'[oO]([a-zA-Z])3', 'ò\\1'),
                        (r'[oO]([sStT])([zZ,])2', 'ó\\1\\2'), (r'[oO]([sStT])([zZ,])3', 'ò\\1\\2'),
                        
                        (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                        (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                        (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])2', 'ú\\1'),
                        (r'[uU]'r'([a-zA-Z][aeiouAEIOU][a-zA-Z])3', 'ù\\1'),
                        (r'[uU]([a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                        (r'[uU]([a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                        (r'[uU]2', 'ú'), (r'[uU]3', 'ù'), (r'[uU]([a-zA-Z])2', 'ú\\1'), (r'[uU]([a-zA-Z])3', 'ù\\1'),
                        (r'[uU]([sStT])([zZ,])2', 'ú\\1\\2'), (r'[uU]([sStT])([zZ,])3', 'ù\\1\\2'),

                        (r'([a-zA-Z])4', '\\1₄'), (r'([a-zA-Z])5', '\\1₅'), (r'([a-zA-Z])6', '\\1₆'), 
                        (r'([a-zA-Z])7', '\\1₇'), (r'([a-zA-Z])8', '\\1₈'), (r'([a-zA-Z])9', '\\1₉'), 
                        (r'([a-zA-Z])10', '\\1₁₀'), (r'([a-zA-Z])11', '\\1₁₁'), (r'([a-zA-Z])12', '\\1₁₂'), 
                        (r'([a-zA-Z])13', '\\1₁₃'), (r'([a-zA-Z])14', '\\1₁₄'), (r'([a-zA-Z])15', '\\1₁₅'), 
                        (r'([a-zA-Z])16', '\\1₁₆'),(r'([a-zA-Z])17', '\\1₁₇'), (r'([a-zA-Z])18', '\\1₁₈')]
        
        determinatives = [(r'{d}', 'ᵈ'), (r'{diš}', '𒁹'),(r'{disz}', '𒁹'), (r'{geš}', 'ᵍᵉˢᶻ'), (r'{gesz}', 'ᵍᵉˢᶻ'),
                          (r'{i7}', 'ⁱ⁷'), (r'{I7}', 'ⁱ⁷'), (r'{iri}', 'ⁱʳⁱ'), (r'{ki}', 'ᵏⁱ'), (r'{kuš}', 'ᵏᶸˢᶻ'), 
                          (r'{lu2}', 'ˡᶸ²'), (r'{lú}', 'ˡᶸ²'), (r'{munus}', 'ᵐᶸⁿᶸˢ'), (r'{še}', 'ˢᶻᵉ'), (r'{uzu}', 'ᶸᶻᶸ'),
                          (r'\(u\)', '(𒌋)'), (r'\(diš\)', '(𒁹)'),(r'\(disz\)', '(𒁹)'), (r'{sze}', 'ˢᶻᵉ'), 
                          (r'{kusz}', 'ᵏᶸˢᶻ'),  (r'{ansze}', 'ᵃⁿˢᶻᵉ'),  (r'{esz2}', 'ᵉˢᶻ²'),  (r'{gi}', 'ᵍⁱ'),
                          (r'{is}', 'ⁱˢ'),  (r'{nisi}', 'ⁿⁱˢⁱ'),  (r'{uruda}', 'ᵘʳᵘᵈᵃ')]

        self.tittles = \
                [(re.compile(regex), repl) for (regex, repl) in tittles]
        
        self.accents = \
                [(re.compile(regex), repl) for (regex, repl) in accents]

        self.determinatives = \
                [(re.compile(regex), repl) for (regex, repl) in determinatives]

    def convert(self, text):

        for (pattern, repl) in self.tittles:
            text = re.subn(pattern, repl, text)[0]

        for (pattern, repl) in self.accents:
            text = re.subn(pattern, repl, text)[0]

        for (pattern, repl) in self.determinatives:
            text = re.subn(pattern, repl,text)[0]

        CatchSumerian = [(r'[\_]\w*[\_]'),
                         (r'[\_]\w*[\s-]\w*[\_]'),
                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\_]'),
                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),
                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]'),   
                         (r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]')]
        Sumerian = str(CatchSumerian)

        CatchAkkadian = [(r'[\_][\s-]\w*[\s-][\_]'),
                         (r'[\_][\s-]\w*[\s-]\w*[\s-][\_]'),
                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]'),
                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]'),
                         (r'[\_][\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-][\_]')]
        Akkadian = str(CatchAkkadian)    
        
        for Sumerian in re.finditer(Sumerian, text):
            text = re.sub(Sumerian, Sumerian.upper(), text)
            text = re.sub(Akkadian, Akkadian.lower(), text)
        
        return text     