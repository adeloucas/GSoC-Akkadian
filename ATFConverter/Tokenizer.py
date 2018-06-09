"""
This module is for tokenizing cuneiform transliterations based off CDLI's ATF-format; it reads ATF material and
converts the data into readable, mutable tokens. The string tokenizer is used for any string-based input (e.g.
copy-and-paste lines from a document) and line tokenizer is for any .txt document that is downloaded from CDLI pages.

The ATFConverter depends upon the word and sign tokenizer outputs.

The logic for this module is based off CLTK's Tokenizer (https://github.com/cltk/cltk/tree/master/cltk/tokenize).
"""

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import re
from nltk.tokenize import RegexpTokenizer

class Tokenizer(object):
    """
    The Tokenizer has the option of preserving damage marked by CDLI.
    ATF-format signs denoting damage and their meaning:
        # = Signs which are damaged
        [] = Signs which are completely broken away
        x = Signs which cannot be identified
        n = Numbers which cannot be identified
        ! = Indicates uncertainty of reading
        ? = Indicates correction
        * = Indicates a collated reading

    For in depth reading on ATF-formatting for CDLI and ORACC:
        Oracc ATF Primer = http://oracc.museum.upenn.edu/doc/help/editinginatf/primer/index.html
        ATF Structure = http://oracc.museum.upenn.edu/doc/help/editinginatf/primer/structuretutorial/index.html
        ATF Inline = http://oracc.museum.upenn.edu/doc/help/editinginatf/primer/inlinetutorial/index.html
    """
    def __init__(self, preserve_damage=False):
        """
        :param preserve_damage: turns on or off preserve damage.
        """
        self.damage = preserve_damage
        #self.metadata = preserve_metadata

    def string_tokenizer(self: object, untokenized_string: str, include_blanks=False):
        """
        This function is based off CLTK's line tokenizer. Use this for strings rather than .txt files.

        input: '20. u2-sza-bi-la-kum\n1. a-na ia-as2-ma-ah-{d}iszkur#\n2. qi2-bi2-ma\n3. um-ma {d}utu-szi-{d}iszkur\n'
        ouput:['20. u2-sza-bi-la-kum', '1. a-na ia-as2-ma-ah-{d}iszkur#', '2. qi2-bi2-ma']

        :param untokenized string
        :param include_blanks: instances of empty lines
        :return: lines as strings in list
        """
        assert isinstance(untokenized_string, str), 'Incoming argument must be a string.'
        if include_blanks:
            tokenized_lines = untokenized_string.splitlines()
        else:
            tokenized_lines = [line for line in untokenized_string.splitlines() if line != r'\\n']
        return tokenized_lines

    def line_tokenizer(self, text):
        """
        Makes a list of lines from a .txt file; outputs only line numbered lines (ignores metadata).

        input:  21. u2-wa-a-ru at-ta e2-kal2-la-ka _e2_-ka wu-e-er
                22. ... u2-ul szi-...
                23. ... x ...
        output:['21. u2-wa-a-ru at-ta e2-kal2-la-ka _e2_-ka wu-e-er',
                '22. ... u2-ul szi-...',
                '23. ... x ...',

        :param: .txt file containing untokenized string
        :return: lines as strings in list
        """
        # create data / no_data = True / False for this
        line_output = []

        with open(text, mode='r+', encoding='utf8') as f:
            lines = f.readlines()
            assert isinstance(text, str), 'Incoming argument must be a string.'
        for line in lines:
            # Strip out damage characters
            if not self.damage:
                line = ''.join(c for c in line if c not in "#[]?!") #Add '*', 'xn'(?)
            if re.match(r'^\d*\.|\d\'\.', line):
                line_output.append(line.strip())
        return line_output

    def word_tokenizer(self, line):
        """
        Operates on a single line of text, returns all words in the line as a tuple in a list.

        input: "1. isz-pur-ram a-na"
        output: [("isz-pur-ram", "akkadian"), ("a-na", "akkadian")]

        :param: line: text string
        :return: list of tuples: (word, language)
        """
        beginning_underscore = "_[^_]+(?!_)$"
            # only match a string if it has a beginning underscore anywhere
        ending_underscore = "^(?<!_)[^_]+_" 
            # only match a string if it has an ending underscore anywhere
        two_underscores = "_[^_]+_" 
            # only match a string if it has two underscores

        words = line.split()[1:]
            # split the line on spaces ignoring the first split (which is the line number)
        language = "akkadian"
        output_words = []
        for word in words:
            if re.search(two_underscores, word):
                # If the string has two underscores in it then the word is
                # in Sumerian while the neighboring words are in Akkadian.
                output_words.append((word, "sumerian"))
            elif re.search(beginning_underscore, word):
                # If the word has an initial underscore somewhere
                # but no other underscores than we're starting a block
                # of Sumerian.
                language = "sumerian"
                output_words.append((word, language))
            elif re.search(ending_underscore, word):
                # If the word has an ending underscore somewhere
                # but not other underscores than we're ending a block
                # of Sumerian.
                output_words.append((word, language))
                language = "akkadian"
            else:
                # If there are no underscore than we are continuing
                # whatever language we're currently in.
                output_words.append((word, language))
        return output_words

    def sign_tokenizer(self, word):
        """
        Takes tuple (word, language) and splits the word up into individual sign tuples (sign, language) in a list.

        input: ("{gisz}isz-pur-ram", "akkadian")
        output: [("gisz", "determinative"), ("isz", "akkadian"), ("pur", "akkadian"), ("ram", "akkadian")]

        :param: tuple created by word_tokenizer2
        :return: list of tuples: (sign, function or language)
        """
        word, word_language = word
        signs_output = []

        if word[0] == "{":
            # Take care of initial determinative
            determinative = re.search("{(.+)}", word)
            signs_output.append((determinative[1], "determinative"))
            # Take match out of word
            word = word[determinative.end():]

        # Akkadian is easy...
        if word_language == "akkadian":
            for sign in word.split('-'):
                signs_output.append((sign, "akkadian"))

        # Sumerian and mixed words are harder...
        elif word_language == "sumerian":
            language = "sumerian"
            for sign in word.split('-'):
                if sign[-1] == "_":
                    # We've reached the last Sumerian sign, the rest is a 
                    # phonetic compliment in Akkadian.
                    signs_output.append((sign[:-1], "sumerian"))
                    language = "akkadian"
                else:
                    signs_output.append((sign, language))

        if signs_output[-1][0][-1] == "}":
            # Take care of final determinative
            determinative = re.search("{(.+)}", signs_output[-1][0])
            signs_output[-1] = (signs_output[-1][0][:determinative.start()], signs_output[-1][1])
            signs_output.append((determinative[1], "determinative"))

        return signs_output

    def word_tokenizer2(self, line_tokenizer):
        """
        Looks at strings in a list (from line_tokenizer) and breaks lines down by words. Includes damages.

        input: ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n']
        output: [['[u2?-wa?-a?-ru?]', 'at-ta', 'e2-[kal2-la-ka', '_e2_-ka', 'wu?-e?-er?]']]

        :param: list of lines as string
        :return: words as strings in list
        """
        word_tokenizer = RegexpTokenizer(r'[\s]|^\d*\.|\d\'\.', gaps=True)
        word_output = [word_tokenizer.tokenize(line) for line in line_tokenizer]
        return word_output

    def sign_tokenizer2(self, line_tokenizer):
        """
        Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs. Excludes special characters.

        input: ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n']
        output: [['u2', 'wa', 'a', 'ru', 'at', 'ta', 'e2', 'kal2', 'la', 'ka', '_e2_', 'ka', 'wu', 'e', 'er']]

        :param: list: line_tokenizer
        :return: signs as strings in list
        """
        sign_tokenizer = RegexpTokenizer(r'[\s\-\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(_{\w*})|({\w*.})', gaps=True)
        sign_output = [sign_tokenizer.tokenize(str(line)) for line in line_tokenizer]
        return sign_output

    def sign_tokenizer2_space_and_hyphen_incl(self, line_tokenizer):
        """
        Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs to be rebuilt into words. Includes
        spaces and hyphens for use with ATFConverter's "reader_reconstruction".

        input: ['21. [u2?-wa?-a?-ru?] at-ta e2-[kal2-la-ka _e2_-ka wu?-e?-er?]\n']
        output: [[' ', 'u2', '-', 'wa', '-', 'a', '-', 'ru', ' ', 'at', '-', 'ta', ' ', 'e2', '-', 'kal2', '-', 'la',
                '-', 'ka', ' ', '_e2_', '-', 'ka', ' ', 'wu', '-', 'e', '-', 'er', '\n']]

        :param: list: line_tokenizer
        :return: signs as strings in list
        """
        sign_tokenizer = RegexpTokenizer(r'[\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(\-)|(\s)|(_{\w*})|({\w*.})', gaps=True)
        sign_output = [sign_tokenizer.tokenize(str(line)) for line in line_tokenizer]
        return sign_output