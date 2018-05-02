## Completed Parts: 
## 1) Tittles 
## 3) Accents
## 5) Numbers 

## In progress: 
## 4) Capture logograms within the text (e.g. ku3-babbar as KU3.BABBAR)

## a) months -- e.g. law 13 line 17, 19 _iti 6(!)-kam_
## b) broken signs (#): law 28 line 30; law 30 line 51; ! -59 near the end "a-zu!"
## c) change hyphen to periods

## Additional Bugs: 

## d) 3 akkadian signs between signs 62 - LUGAL_ sha i-na _kalam
## e) line 94 -- mistype of text : _ ISZ-QU2-LU A-NA _KU3-BABBER_DAM-GAR3_
## f) law 277 line 54 and 56 -- the parenthesis messes it all up
## g) e.g. 274 - all broken up
## ISSUE: Law 15 

# next steps:

# a) months -- e.g. law 13 line 17, 19 _iti 6(sign)-kam_

#   (r'[iI][tT][iI]\s' ... ? -- I'd rather be able to just say "between ITI and -KAM, capitalize the string)

#b) broken signs (#): law 28 line 30; law 30 line 51; ! -59 near the end "a-zu!"

#   Haven't looked into a solution yet

#c) change hypen to periods

#   Issue: don't want it to affect the akkadian

## Additional Bugs: ##

# d) 3 akkadian signs between signs 62 - LUGAL_ sha i-na _kalam
# e) line 94 -- mistype of text -> shouldn't be between underscores : _ ISZ-QU2-LU A-NA _KU3-BABBER_DAM-GAR3 _
# f) law 277 line 54 and 56 -- the parenthesis messes it all up
# g) e.g. 274 - all broken up
# h) Law 15

## Up-to-date program

"""ATF Converter"""   
## Replaces Akkadian letters, marked logograms, and determinatives. 

__author__ = ['Andrew Deloucas <adeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'
                                                        
import re

class ATFConverter(object):     
    def __init__(self):
        ## Accent Converter
        ## Row one and two: accent is on first vowel (3 phonemes)
        ## Row three: accent is on first / middle vowel (2 phonemes)
        ## Row four: accent is on last vowel (standard)
        ## Row five: accent is on last vowel (considers 'sz' and 's,/t,')
        ## known issue: Arad2
        accents =  [(r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'á\\1'), 
                    (r'[aA]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                    (r'[aA]([a-zA-Z][aeiouAEIOU])2', 'á\\1'), (r'[aA]([a-zA-Z][aeiouAEIOU])3', 'à\\1'),
                    (r'[aA]2', 'á'), (r'[aA]3', 'à'), (r'[aA]([a-zA-Z])2', 'á\\1'), (r'[aA]([a-zA-Z])3', 'à\\1'), 
                    (r'[aA]([sStT])([zZ,])2', 'á\\1\\2'), (r'[aA]([sStT])([zZ,])3', 'à\\1\\2'),
            
                    (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'é\\1'), 
                    (r'[eE]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                    (r'[eE]([a-zA-Z][aeiouAEIOU])2', 'é\\1'), (r'[eE]([a-zA-Z][aeiouAEIOU])3', 'è\\1'),
                    (r'[eE]2', 'é'), (r'[eE]3', 'è'), (r'[eE]([a-zA-Z])2', 'é\\1'), (r'[eE]([a-zA-Z])3', 'è\\1'),
                    (r'[eE]([sStT])([zZ,])2', 'é\\1\\2'), (r'[eE]([sStT])([zZ,])3', 'è\\1\\2'),
                    
                    (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'í\\1'), 
                    (r'[iI]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                    (r'[iI]([a-zA-Z][aeiouAEIOU])2', 'í\\1'), (r'[iI]([a-zA-Z][aeiouAEIOU])3', 'ì\\1'),
                    (r'[iI]2', 'í'), (r'[iI]3', 'ì'), (r'[iI]([a-zA-Z])2', 'í\\1'), (r'[iI]([a-zA-Z])3', 'ì\\1'),
                    (r'[iI]([sStT])([zZ,])2', 'í\\1\\2'), (r'[iI]([sStT])([zZ,])3', 'ì\\1\\2'),
                    
                    (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ó\\1'), 
                    (r'[oO]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                    (r'[oO]([a-zA-Z][aeiouAEIOU])2', 'ó\\1'), (r'[oO]([a-zA-Z][aeiouAEIOU])3', 'ò\\1'),
                    (r'[oO]2', 'ó'), (r'[oO]3', 'ò'), (r'[oO]([a-zA-Z])2', 'ó\\1'), (r'[oO]([a-zA-Z])3', 'ò\\1'),
                    (r'[oO]([sStT])([zZ,])2', 'ó\\1\\2'), (r'[oO]([sStT])([zZ,])3', 'ò\\1\\2'),
                    
                    (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])2', 'ú\\1'), 
                    (r'[uU]([a-zA-Z][aeiouAEIOU][a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                    (r'[uU]([a-zA-Z][aeiouAEIOU])2', 'ú\\1'), (r'[uU]([a-zA-Z][aeiouAEIOU])3', 'ù\\1'),
                    (r'[uU]2', 'ú'), (r'[uU]3', 'ù'), (r'[uU]([a-zA-Z])2', 'ú\\1'), (r'[uU]([a-zA-Z])3', 'ù\\1'),
                    (r'[uU]([sStT])([zZ,])2', 'ú\\1\\2'), (r'[uU]([sStT])([zZ,])3', 'ù\\1\\2'),
                    
        ## this subscripts numbers after 2 and 3; CHECK IF ANY SIGNS GO HIGHER THAN 18.
                    (r'([a-zA-Z])4', '\\1₄'), (r'([a-zA-Z])5', '\\1₅'), (r'([a-zA-Z])6', '\\1₆'), 
                    (r'([a-zA-Z])7', '\\1₇'), (r'([a-zA-Z])8', '\\1₈'), (r'([a-zA-Z])9', '\\1₉'), 
                    (r'([a-zA-Z])10', '\\1₁₀'), (r'([a-zA-Z])11', '\\1₁₁'), (r'([a-zA-Z])12', '\\1₁₂'), 
                    (r'([a-zA-Z])13', '\\1₁₃'), (r'([a-zA-Z])14', '\\1₁₄'), (r'([a-zA-Z])15', '\\1₁₅'), 
                    (r'([a-zA-Z])16', '\\1₁₆'),(r'([a-zA-Z])17', '\\1₁₇'), (r'([a-zA-Z])18', '\\1₁₈')]
        
        ## determinative converter; check ARM1 for logograms
        tittles =  [(r's,', 'ṣ'), (r'sz', 'š'), (r't,', 'ṭ'), (r'S,', 'Ṣ'), (r'SZ', 'Š'), (r'T,', 'Ṭ'),
                    (r'{d}', 'ᵈ'), (r'{diš}', '𒁹'), (r'{geš}', 'ᵍᵉˢᶻ'), (r'{i7}', 'ⁱ⁷'), (r'{i₇}', 'ⁱ⁷'), 
                    (r'{iri}', 'ⁱʳⁱ'), (r'{ki}', 'ᵏⁱ'), (r'{kuš}', 'ᵏᶸˢᶻ'), (r'{lu2}', 'ˡᶸ²'), 
                    (r'{lú}', 'ˡᶸ²'), (r'{munus}', 'ᵐᶸⁿᶸˢ'), (r'{še}', 'ˢᶻᵉ'), (r'{uzu}', 'ᶸᶻᶸ'),
                    (r'\(u\)', '(𒌋)'), (r'\(diš\)', '(𒁹)')]
        
        self.accents = \
            [(re.compile(regex), repl) for (regex, repl) in accents]
        self.tittles = \
            [(re.compile(regex), repl) for (regex, repl) in tittles]

    
    def transliterate(self, text):
        # gives signs accents & subscript numbers #
        for (pattern, repl) in self.accents:
            text = re.subn(pattern, repl, text)[0]
       
        # crosses t's & dots i's #
        for (pattern, repl) in self.tittles:
            text = re.subn(pattern, repl, text)[0]
            
        # capitalizes sumerian by finding instances of underscores#
        for a in re.finditer(r'\_\w*\_', text):
            text = re.sub(r'\_\w*\_', lambda x: x.group(0).upper(), text)
        for b in re.finditer(r'[\_]\w*[\s-]\w*[\_]', text):
            text = re.sub(r'[\_]\w*[\s-]\w*[\_]', lambda y: y.group(0).upper(), text)
        for c in re.finditer(r'[\_]\w*[\s-]\w*[\s-]\w*[\_]', text):                    
            text = re.sub(r'[\_]\w*[\s-]\w*[\s-]\w*[\_]', lambda c: c.group(0).upper(), text)
        for d in re.finditer(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', text):                    
            text = re.sub(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*\_]', lambda d: d.group(0).upper(), text)
        for e in re.finditer(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', text):                    
            text = re.sub(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', lambda e: e.group(0).upper(), text)
        for f in re.finditer(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', text):                    
            text = re.sub(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', lambda f: f.group(0).upper(), text)
        for g in re.finditer(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', text):                    
            text = re.sub(r'[\_]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\w*[\_]', lambda c: g.group(0).upper(), text)
        #lowercases any akkadian found in the above section #
        for cc in re.finditer(r'\_[\s-]\w*[\s-]\_', text):
            text = re.sub(r'\_[\s-]\w*[\s-]\_', lambda cc: cc.group(0).lower(), text)
        for dd in re.finditer(r'\_[\s-]\w*[\s-]\w*[\s-]\_', text):
            text = re.sub(r'\_[\s-]\w*[\s-]\w*[\s-]\_', lambda dd: dd.group(0).lower(), text)
        for ee in re.finditer(r'\_[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\_', text):
            text = re.sub(r'\_[\s-]\w*[\s-]\w*[\s-]\w*[\s-]\_', lambda ee: ee.group(0).lower(), text)
        #removes logogram markers -- keep off until above is checked and balanced.
            #text = re.sub(r'_', '', text)
        return text