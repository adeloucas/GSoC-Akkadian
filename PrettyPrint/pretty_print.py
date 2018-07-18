"""
This module is for printing texts for Markdown or HTML.
"""

import markdown

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class PrettyPrint(object):
    """
    Prints texts in markdown or in HTML.
    """
    def __init__(self):
        """
        None
        """
        self.markdown = []

    def markdown_print(self, ingest_text, edition_or_cdli_number):
                                                               #, filename):
        """
        Prints text_file in markdown.
       :param ingest_text: text ingested by cdli_corpus
       :param edition_or_cdli_number: text you wish to print
       :return: output in markdown_file.md / filename.md
       """
        for text in ingest_text:
            cdli = text['cdli number']
            edition = text['text edition']
            metadata = text['metadata'][0]
            transliteration = text['transliteration'][0]
            if edition_or_cdli_number in edition or \
                    cdli:
                return ["{} {} {} {}".format(cdli, edition,
                                             metadata, transliteration)]
                # self.markdown.append(final_thing)
        # with open(filename, mode='r+', encoding='utf8') as text_file:
        #    text_file.write(html)
        #    return text_file

    def html_print(self, filename):
        """
        Prints text_file in html.
        :param filename: the file name where you want to save the print.
        :return: output in html_file.html.
        """
        html = markdown.markdown(self.markdown)
        with open(filename, mode='r+', encoding='utf8') as text_file:
            text_file.write(html)
            return text_file
