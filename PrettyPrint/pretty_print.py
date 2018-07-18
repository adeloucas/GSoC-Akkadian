"""
This module is for printing texts in Markdown or HTML.
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
        Empty.
        """

    def markdown_print_file(self, ingest_text, filename):
        """
        Prints whole text_file in markdown.
        :param ingest_text: text ingested by cdli_corpus
        :param filename: where you wish to save the markdown data
        :return: output in filename.md
       """
        with open(filename, mode='r+', encoding='utf8') as text_file:
            for text in ingest_text:
                edition = text['text edition'][0]
                metadata = '\n \t'.join(text['metadata'][0])
                transliteration = '\n \t'.join(text['transliteration'][0])
                m_d = """
{edition}
---
###### metadata
    {metadata}
###### transliteration
    {transliteration} 
""".format(edition=edition, metadata=metadata, transliteration=transliteration)
                self.markdown_file = m_d
                text_file.write(self.markdown_file)

    def markdown_print_single_text(self, ingest_text, cdli_number, filename):
        """
        Prints single text in file in markdown.
       :param ingest_text: text ingested by cdli_corpus
       :param cdli_number: text you wish to print
       :param filename: where you wish to save the markdown data
       :return: output in filename.md
       """
        with open(filename, mode='r+', encoding='utf8') as text_file:
            for text in ingest_text:
                cdli = text['cdli number'][0]
                if cdli_number in cdli:
                    edition = text['text edition'][0]
                    metadata = '\n \t'.join(text['metadata'][0])
                    transliteration = '\n \t'.join(text['transliteration'][0])
                    m_d = """
{edition}
---
###### metadata
    {metadata}
###### transliteration
    {transliteration} 
""".format(edition=edition, metadata=metadata, transliteration=transliteration)
                    self.markdown_text = m_d
                    text_file.write(self.markdown_text)

    def html_print(self, origin, destination):
        """
        Prints text_file in html.
        :param filename: the file name where you want to save the print.
        :param origin: where markdown data is
        :param destination: where you wish to save the HTML data
        :return: output in html_file.html.
        """
        html = markdown.markdown(origin)
        with open(destination, mode='r+', encoding='utf8') as text_file:
            self.html = html
            text_file.write(self.html)
