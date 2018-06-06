import re
from nltk.tokenize import RegexpTokenizer

class Tokenizer(object):

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
        #create data / no_data = True / False for this
        line_output = []

        with open(text, mode='r+', encoding='utf8') as f:
            lines = f.readlines()
            assert isinstance(text, str), 'Incoming argument must be a string.'
            for line in lines:
                if re.match(r'^\d*\.|\d\'\.', line):
                    line_output.append(line)
            return line_output

    def word_tokenizer(self, line_tokenizer):
        """Looks at the strings in a list and breaks lines down by words. Includes special characters"""
        word_output = []
        word_tokenizer = RegexpTokenizer(r'[\s]|^\d*\.|\d\'\.', gaps=True)
        for line in line_tokenizer:
            word_output.append(word_tokenizer.tokenize(line))
        return word_output

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