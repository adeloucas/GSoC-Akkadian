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

    def words(self, line_tokenizer):
        """Looks at the strings in a list and breaks lines down by words. Includes special characters"""
        word_output = []
        word_tokenizer = RegexpTokenizer(r'[\s]|^\d*\.|\d\'\.', gaps=True)
        for line in line_tokenizer:
            word_output.append(word_tokenizer.tokenize(line))
        return word_output

    def signs(self, line_tokenizer):
        """Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs. Excludes special characters."""
        sign_output = []
        sign_tokenizer = RegexpTokenizer(r'[\s\-\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(_{\w*})|({\w*.})', gaps=True)
        for line in line_tokenizer:
            sign_output.append(sign_tokenizer.tokenize(str(line)))

        return sign_output

    def signs_for_breakdown(self, line_tokenizer):
        """Utilizes NLTK's RegexpTokenizer to break down lines into individuals signs to be rebuilt into words after analysis."""
        sign_output = []
        sign_tokenizer = RegexpTokenizer(r'[\#\!\?\[\]\<\>|]|^\d*\.|\d\'\.|(\-)|(\s)|(_{\w*})|({\w*.})', gaps=True)
        for line in line_tokenizer:
            sign_output.append(sign_tokenizer.tokenize(str(line)))

        return sign_output

    def determinatives(self, line_tokenizer):
        """Returns determinatives found in a list."""
        determinatives_output = []
        determinatives = re.compile(r'{\w*}')
        for sign in determinatives.finditer(str(line_tokenizer)):
            determinatives_output.append(sign.group())
        return determinatives_output

    def numbers(self, line_tokenizer):
        """Returns numbers and number signs found in a list."""
        numbers_output = []
        number_signs_output = []
        zipped_output = []
        numbers = re.compile(r'\d\/\d|\d\(|\d\s\(|n\(')
        number_signs = re.compile(r'\(\w*\)')
        for sign in numbers.finditer(str(line_tokenizer)):
            numbers_output.append(sign.group())
            numbers_output = [s.replace('(', '') for s in numbers_output]
        for sign in number_signs.finditer(str(line_tokenizer)):
            number_signs_output.append(sign.group())
        zipped_output = list(zip(numbers_output, number_signs_output))
        return zipped_output

    def sumerian(self, line_tokenizer):
        """Returns Sumerian found in a list."""
        sumerian_output = []
        sumerian = re.compile(r'(?<=_).*?(?=_)')
        akkadian = re.compile(r'(?<=[^\s]_).*?(?=_)')
        for signs in sumerian.finditer(str(line_tokenizer)):
            sumerian_output.append(signs.group())
        for signs in akkadian.finditer(str(line_tokenizer)):
            sumerian_output.remove(signs.group())
        return sumerian_output

    def sumerian_words(self, sumerian):
        """Returns a breakdown of Sumerian words found in list of Sumerian."""
        output = []
        word = RegexpTokenizer(r'[\s|]', gaps=True)
        for line in sumerian:
            output.append(word.tokenize(re.subn('-', '.', line.upper())[0]))
        return output

    def sumerian_signs(self, sumerian):
        """Returns a breakdown of Sumerian signs found in a list of Sumerian."""
        output = []
        sign = RegexpTokenizer(r'[\.\s\(\)\{\}|]', gaps=True)
        for line in sumerian:
            output.append(sign.tokenize(re.subn('-', '.', line.upper())[0]))
        return output