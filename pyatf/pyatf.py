

ONE_CHAR = {
    "a2": "a₂",
    "a3": "a₃",
}

TWO_CHAR = {
    "ab2": "ab₂",
    "be3": "be₃"
}

TWO_THREE_TO_ACCENTS = {
    "₂": "\u0301",
    "₃": "\u0300"
}


class ATFConverter:
    def __init__(self, two_three=True):
        self.mappings = {**ONE_CHAR, **TWO_CHAR}
        if not two_three:
            """Convert subscripts to accents for output"""

    def process(self, text_string):
        """
        Expects a list of tokens, will return the list converted from
        ATF format to print-format
        """
        output = []
        for token in text_string:
            try:
                output.append(self.mappings[token])
            except KeyError:
                print("No conversion rule for: {}".format(token))
                output.append("ERROR: ({})".format(token))
        return output
