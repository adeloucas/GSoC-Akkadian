import re
from nltk.tokenize import RegexpTokenizer

class Tokenizer(object):

    def __init__(self, preserve_damage=False):
        self.damage = preserve_damage

    def string_tokenizer(self: object, untokenized_string: str, include_blanks=False):
        """This is CLTK's line tokenizer. Use this for strings rather than .txt files."""
        assert isinstance(untokenized_string, str), 'Incoming argument must be a string.'
        if include_blanks:
            tokenized_lines = untokenized_string.splitlines()
        else:
            tokenized_lines = [line for line in untokenized_string.splitlines() if line != r'\\n']
        return tokenized_lines

    def line_tokenizer(self, text):
        """Makes lines of a .txt file into a list, printing only line numbered lines (ignores metadata)."""
        # create data / no_data = True / False for this
        line_output = []

        with open(text, mode='r+', encoding='utf8') as f:
            lines = f.readlines()
            assert isinstance(text, str), 'Incoming argument must be a string.'
        for line in lines:
            # Strip out damage characters
            if not self.damage:
                line = ''.join(c for c in line if c not in "#[]?!")
            if re.match(r'^\d*\.|\d\'\.', line):
                line_output.append(line.strip())
        return line_output

    def word_tokenizer(self, line_tokenizer):
        """Looks at the strings in a list and breaks lines down by words. Includes special characters"""
        word_output = []
        word_tokenizer = RegexpTokenizer(r'[\s]|^\d*\.|\d\'\.', gaps=True)
        for line in line_tokenizer:
            word_output.append(word_tokenizer.tokenize(line))
        return word_output

    def word_tokenizer2(self, line):
        """Operates on a single line of text, returns all words in the line in a list.
        input: "1. isz-pur-ram a-na"
        output: [("isz-pur-ram", "akkadian"), ("a-na", "akkadian")]
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

    def sign_tokenizer2(self, word):
        """Takes a tuple (word, language) and splits the word up into individual
        sign tuples (sign, language) in a list.
        input: ("{gisz}isz-pur-ram", "akkadian")
        output: [("gisz", "determinative"), ("isz", "akkadian"), ("pur", "akkadian"), ("ram", "akkadian")]
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


    def sign_tokenizer(self, line_tokenizer):
        """Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs. Excludes special characters."""
        sign_output = []
        sign_tokenizer = RegexpTokenizer(r'[\s\-\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(_{\w*})|({\w*.})', gaps=True)
        for line in line_tokenizer:
            sign_output.append(sign_tokenizer.tokenize(str(line)))

        return sign_output

    def sign_tokenizer_space_and_hyphen_incl(self, line_tokenizer):
        """Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs to be rebuilt into words
        after analysis."""
        sign_output = []
        sign_tokenizer = RegexpTokenizer(r'[\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(\-)|(\s)|(_{\w*})|({\w*.})', gaps=True)
        for line in line_tokenizer:
            sign_output.append(sign_tokenizer.tokenize(str(line)))

        return sign_output