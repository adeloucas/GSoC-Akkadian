"""
This file tests methods in pretty_print.py.
"""

import unittest
import os
from Importer.file_importer import FileImport  # pylint: disable =import-error
from PrettyPrint.pretty_print import PrettyPrint  # pylint: disable =import-error
from Importer.cdli_corpus import CDLICorpus  # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_print(self):
        """
        Tests underscore_remover.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        pp = PrettyPrint()
        pp.markdown_print(cdli.texts, 'ARM 01, 001')
        goal = ["['&P254202'] ['ARM 01, 001'] ['Primary publication: ARM 01, 001', "
                "'Author(s): Dossin, Georges', 'Publication date: 1946', 'Secondary "
                "publication(s): Durand, Jean-Marie, LAPO 16, 0305', 'Collection: National "
                "Museum of Syria, Damascus, Syria', 'Museum no.: NMSD —', 'Accession no.:', "
                "'Provenience: Mari (mod. Tell Hariri)', 'Excavation no.:', 'Period: Old "
                "Babylonian (ca. 1900-1600 BC)', 'Dates referenced:', 'Object type: tablet', "
                "'Remarks:', 'Material: clay', 'Language: Akkadian', 'Genre: Letter', "
                "'Sub-genre:', 'CDLI comments:', 'Catalogue source: 20050104 cdliadmin', 'ATF "
                "source: cdlistaff', 'Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. "
                "(en)', 'UCLA Library ARK: 21198/zz001rsp8x', 'Composite no.:', 'Seal no.:', "
                "'CDLI no.: P254202'] ['&P254202 = ARM 01, 001', '#atf: lang akk', '@tablet', "
                "'@obverse', '1. a-na ia-ah-du-li-[im]', '2. qi2-bi2-[ma]', '3. um-ma "
                "a-bi-sa-mar#-[ma]', '4. sa-li-ma-am e-pu-[usz]', '5. asz-szum "
                "mu-sze-zi-ba-am# [la i-szu]', '6. [sa]-li#-ma-am sza e-[pu-szu]', '7. "
                "[u2-ul] e-pu-usz sa#-[li-mu-um]', '8. [u2-ul] sa-[li-mu-um-ma]', '$ rest "
                'broken\', \'@reverse\', \'$ beginning broken\', "1\'. isz#-tu '
                'mu#-[sze-zi-ba-am la i-szu]", "2\'. a-la-nu-ia sza la is,-s,a-ab#-[tu]", '
                '"3\'. i-na-an-na is,-s,a-ab-[tu]", "4\'. i-na ne2-kur-ti _lu2_ '
                'ha-szi-[im{ki}]", "5\'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]", "6\'. u3 '
                'ia-am-ha-ad[{ki}]", "7\'. a-la-nu an-nu-tum u2-ul ih-li-qu2#", "8\'. i-na '
                'ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma", "9\'. ih-ta-al-qu2", "10\'. u3 '
                'a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#", "11\'. u3 na-pa-asz2-ti '
                'u2-ba-li-it,", "12\'. pi2-qa-at ha-s,e-ra#-at", "13\'. asz-szum a-la-nu-ka", '
                '"14\'. u3 ma-ru-ka sza-al#-[mu]", "15\'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"]']
        output = pp.markdown_print(cdli.texts, 'ARM 01, 001')
        self.assertEqual(output, goal)
