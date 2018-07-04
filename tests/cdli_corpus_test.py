"""
This file tests methods in cdli_corpus.py.
"""

import unittest
import os
from Importer.file_importer import FileImport  # pylint: disable =import-error
from Importer.cdli_corpus import CDLICorpus  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


""" NOTES FROM LAST NIGHT:
        fi = FileImport('texts/cdli_corpus.txt')
        fi.read_file()
        cdli = CorpusImporter(corpus_type='cdli')
        cdli.ingest(fi.file_lines)
        fi = FileImport("http://www.etcsl.ox.co.uk/corpus.txt")
        fi.read_file()
        etcsl = CorpusImporter(corpus_type='etcsl')
        etcsl.ingest(fi.file_lines)
        texts = [
            {'pnum': 'P123123', 'edition': ['ARM 1...'],
             'metadata': ['line1', 'line2', 'line3'],
             'lines': ['1. xxx', '2. xxx']},
            {'pnum': 'P363453', 'edition': ['ARM 1...'],
             'metadata': ['line1', 'line2', 'line3'],
             'lines': ['1. xxx', '2. xxx']}]
        print([text['pnum'] for text in self.texts])
        [text['lines'] for text in self.texts if text['pnum'] == 'P123123'][0]
        """


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests CDLICorpus class.
    """
    def test_chunk_text(self):
        """
        Tests chunk_text.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        output = cdli.chunk_text()
        goal = [['Primary publication: ARM 01, 001',
                 'Author(s): Dossin, Georges',
                 'Publication date: 1946',
                 'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0305',
                 'Collection: National Museum of Syria, Damascus, Syria',
                 'Museum no.: NMSD —',
                 'Accession no.:',
                 'Provenience: Mari (mod. Tell Hariri)',
                 'Excavation no.:',
                 'Period: Old Babylonian (ca. 1900-1600 BC)',
                 'Dates referenced:',
                 'Object type: tablet',
                 'Remarks:',
                 'Material: clay',
                 'Language: Akkadian',
                 'Genre: Letter',
                 'Sub-genre:',
                 'CDLI comments:',
                 'Catalogue source: 20050104 cdliadmin',
                 'ATF source: cdlistaff',
                 'Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. (en)',
                 'UCLA Library ARK: 21198/zz001rsp8x',
                 'Composite no.:',
                 'Seal no.:',
                 'CDLI no.: P254202',
                 'Transliteration:',
                 '&P254202 = ARM 01, 001',
                 '#atf: lang akk',
                 '@tablet',
                 '@obverse',
                 '1. a-na ia-ah-du-li-[im]',
                 '2. qi2-bi2-[ma]',
                 '3. um-ma a-bi-sa-mar#-[ma]',
                 '4. sa-li-ma-am e-pu-[usz]',
                 '5. asz-szum mu-sze-zi-ba-am# [la i-szu]',
                 '6. [sa]-li#-ma-am sza e-[pu-szu]',
                 '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
                 '8. [u2-ul] sa-[li-mu-um-ma]',
                 '$ rest broken',
                 '@reverse',
                 '$ beginning broken',
                 "1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]",
                 "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
                 "3'. i-na-an-na is,-s,a-ab-[tu]",
                 "4'. i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]",
                 "5'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]",
                 "6'. u3 ia-am-ha-ad[{ki}]",
                 "7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#",
                 "8'. i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma",
                 "9'. ih-ta-al-qu2",
                 "10'. u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#",
                 "11'. u3 na-pa-asz2-ti u2-ba-li-it,",
                 "12'. pi2-qa-at ha-s,e-ra#-at",
                 "13'. asz-szum a-la-nu-ka",
                 "14'. u3 ma-ru-ka sza-al#-[mu]",
                 "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"],
                ['Primary publication: ARM 01, 002',
                 'Author(s): Dossin, Georges',
                 'Publication date: 1946',
                 'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0306',
                 'Collection: National Museum of Syria, Damascus, Syria',
                 'Museum no.: NMSD —',
                 'Accession no.:',
                 'Provenience: Mari (mod. Tell Hariri)',
                 'Excavation no.:',
                 'Period: Old Babylonian (ca. 1900-1600 BC)',
                 'Dates referenced:',
                 'Object type: tablet',
                 'Remarks:',
                 'Material: clay',
                 'Language: Akkadian',
                 'Genre: Letter',
                 'Sub-genre:',
                 'CDLI comments:',
                 'Catalogue source: 20050104 cdliadmin',
                 'ATF source: cdlistaff',
                 'Translation:',
                 'UCLA Library ARK: 21198/zz001rsp9f',
                 'Composite no.:',
                 'Seal no.:',
                 'CDLI no.: P254203',
                 'Transliteration:',
                 '&P254203 = ARM 01, 002',
                 '#atf: lang akk',
                 '@tablet',
                 '@obverse',
                 '1. a-na ia-ah-du-[li-im]',
                 '2. qi2-bi2-[ma]',
                 '3. um-ma a-bi-sa-mar-[ma]',
                 '4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#',
                 '5. a-na ma-ni-im lu-ud-bu-ub',
                 '6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]',
                 '7. szum-ma a-bi-sa-mar te-zi-ir#',
                 '8. u3 a-la#-ni#-ka te-zi-ir-ma#',
                 '9. i-na an-ni-a-tim sza a-da-bu-[bu]',
                 '10. a-na-ku mi-im-ma u2-ul e-le#-[i]',
                 '11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]',
                 '12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]',
                 '13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]',
                 '14. u3 lu ma-at ia-ma-ha-ad#{ki}',
                 '15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]',
                 '$ rest broken',
                 '@reverse',
                 '$ beginning broken',
                 "1'. um#-[...]",
                 "2'. lu#-[...]",
                 "3'. a-[...]",
                 "4'. szum#-[...]",
                 "5'. a-na# [...]",
                 "6'. ma-li# [...]",
                 "7'. u3 u2-hu-ur# [...]",
                 "8'. a-su2-ur-ri [...]",
                 "9'. szu-zi-ba-an#-[ni ...]",
                 "10'. a-na [...]",
                 "11'. pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]",
                 '@left',
                 '1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na '
                 'la bi-tu#-[tu-ur2-ma]',
                 '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]']]
        self.assertEqual(output, goal)

    def test_find_cdli_number(self):
        """
        Tests find_cdli_number.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        output = cdli.find_cdli_number()
        goal = ['&P254202', '&P254203']
        self.assertEqual(output, goal)

    def test_find_edition(self):
        """
        Tests find_edition.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        output = cdli.find_edition()
        goal = ['ARM 01, 001', 'ARM 01, 002']
        self.assertEqual(output, goal)

    def test_find_metadata(self):
        """
        Tests find_metadata.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        output = cdli.find_metadata()
        goal = [['Primary publication: ARM 01, 001',
                 'Author(s): Dossin, Georges',
                 'Publication date: 1946',
                 'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0305',
                 'Collection: National Museum of Syria, Damascus, Syria',
                 'Museum no.: NMSD —',
                 'Accession no.:',
                 'Provenience: Mari (mod. Tell Hariri)',
                 'Excavation no.:',
                 'Period: Old Babylonian (ca. 1900-1600 BC)',
                 'Dates referenced:',
                 'Object type: tablet',
                 'Remarks:',
                 'Material: clay',
                 'Language: Akkadian',
                 'Genre: Letter',
                 'Sub-genre:',
                 'CDLI comments:',
                 'Catalogue source: 20050104 cdliadmin',
                 'ATF source: cdlistaff',
                 'Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. (en)',
                 'UCLA Library ARK: 21198/zz001rsp8x',
                 'Composite no.:',
                 'Seal no.:',
                 'CDLI no.: P254202'],
                ['Primary publication: ARM 01, 002',
                 'Author(s): Dossin, Georges',
                 'Publication date: 1946',
                 'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0306',
                 'Collection: National Museum of Syria, Damascus, Syria',
                 'Museum no.: NMSD —',
                 'Accession no.:',
                 'Provenience: Mari (mod. Tell Hariri)',
                 'Excavation no.:',
                 'Period: Old Babylonian (ca. 1900-1600 BC)',
                 'Dates referenced:',
                 'Object type: tablet',
                 'Remarks:',
                 'Material: clay',
                 'Language: Akkadian',
                 'Genre: Letter',
                 'Sub-genre:',
                 'CDLI comments:',
                 'Catalogue source: 20050104 cdliadmin',
                 'ATF source: cdlistaff',
                 'Translation:',
                 'UCLA Library ARK: 21198/zz001rsp9f',
                 'Composite no.:',
                 'Seal no.:',
                 'CDLI no.: P254203']]
        self.assertEqual(output, goal)

    def test_find_transliteration(self):
        """
        Tests find_transliteration.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        output = cdli.find_transliteration()
        goal = [['&P254202 = ARM 01, 001',
                 '#atf: lang akk',
                 '@tablet',
                 '@obverse',
                 '1. a-na ia-ah-du-li-[im]',
                 '2. qi2-bi2-[ma]',
                 '3. um-ma a-bi-sa-mar#-[ma]',
                 '4. sa-li-ma-am e-pu-[usz]',
                 '5. asz-szum mu-sze-zi-ba-am# [la i-szu]',
                 '6. [sa]-li#-ma-am sza e-[pu-szu]',
                 '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
                 '8. [u2-ul] sa-[li-mu-um-ma]',
                 '$ rest broken',
                 '@reverse',
                 '$ beginning broken',
                 "1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]",
                 "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
                 "3'. i-na-an-na is,-s,a-ab-[tu]",
                 "4'. i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]",
                 "5'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]",
                 "6'. u3 ia-am-ha-ad[{ki}]",
                 "7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#",
                 "8'. i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma",
                 "9'. ih-ta-al-qu2",
                 "10'. u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#",
                 "11'. u3 na-pa-asz2-ti u2-ba-li-it,",
                 "12'. pi2-qa-at ha-s,e-ra#-at",
                 "13'. asz-szum a-la-nu-ka",
                 "14'. u3 ma-ru-ka sza-al#-[mu]",
                 "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"],
                ['&P254203 = ARM 01, 002',
                 '#atf: lang akk',
                 '@tablet',
                 '@obverse',
                 '1. a-na ia-ah-du-[li-im]',
                 '2. qi2-bi2-[ma]',
                 '3. um-ma a-bi-sa-mar-[ma]',
                 '4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#',
                 '5. a-na ma-ni-im lu-ud-bu-ub',
                 '6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]',
                 '7. szum-ma a-bi-sa-mar te-zi-ir#',
                 '8. u3 a-la#-ni#-ka te-zi-ir-ma#',
                 '9. i-na an-ni-a-tim sza a-da-bu-[bu]',
                 '10. a-na-ku mi-im-ma u2-ul e-le#-[i]',
                 '11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]',
                 '12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]',
                 '13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]',
                 '14. u3 lu ma-at ia-ma-ha-ad#{ki}',
                 '15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]',
                 '$ rest broken',
                 '@reverse',
                 '$ beginning broken',
                 "1'. um#-[...]",
                 "2'. lu#-[...]",
                 "3'. a-[...]",
                 "4'. szum#-[...]",
                 "5'. a-na# [...]",
                 "6'. ma-li# [...]",
                 "7'. u3 u2-hu-ur# [...]",
                 "8'. a-su2-ur-ri [...]",
                 "9'. szu-zi-ba-an#-[ni ...]",
                 "10'. a-na [...]",
                 "11'. pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]",
                 '@left',
                 '1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na '
                 'la bi-tu#-[tu-ur2-ma]',
                 '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]']]
        self.assertEqual(output, goal)

    def test_ingest(self):
        """
        Tests ingest.
        """
        path = os.path.join('..', 'texts', 'single_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        cdli.ingest()
        goal = {'cdli numbers': ['&P254202'],
                'text editions': ['ARM 01, 001'],
                'metadata': ['Primary publication: ARM 01, 001',
                             'Author(s): Dossin, Georges',
                             'Publication date: 1946',
                             'Secondary publication(s): Durand, '
                             'Jean-Marie, LAPO 16, 0305',
                             'Collection: National Museum of Syria, '
                             'Damascus, Syria',
                             'Museum no.: NMSD —',
                             'Accession no.:',
                             'Provenience: Mari (mod. Tell Hariri)',
                             'Excavation no.:',
                             'Period: Old Babylonian (ca. 1900-1600 BC)',
                             'Dates referenced:',
                             'Object type: tablet',
                             'Remarks:',
                             'Material: clay',
                             'Language: Akkadian',
                             'Genre: Letter',
                             'Sub-genre:',
                             'CDLI comments:',
                             'Catalogue source: 20050104 cdliadmin',
                             'ATF source: cdlistaff',
                             'Translation: Durand, Jean-Marie (fr); '
                             'Guerra, Dylan M. (en)',
                             'UCLA Library ARK: 21198/zz001rsp8x',
                             'Composite no.:',
                             'Seal no.:',
                             'CDLI no.: P254202'],
                'transliterations': ['&P254202 = ARM 01, 001',
                                     '#atf: lang akk',
                                     '@tablet',
                                     '@obverse',
                                     '1. a-na ia-ah-du-li-[im]',
                                     '2. qi2-bi2-[ma]',
                                     '3. um-ma a-bi-sa-mar#-[ma]',
                                     '4. sa-li-ma-am e-pu-[usz]',
                                     '5. asz-szum mu-sze-zi-ba-am# [la i-szu]',
                                     '6. [sa]-li#-ma-am sza e-[pu-szu]',
                                     '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
                                     '8. [u2-ul] sa-[li-mu-um-ma]',
                                     '$ rest broken',
                                     '@reverse',
                                     '$ beginning broken',
                                     "1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]",
                                     "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
                                     "3'. i-na-an-na is,-s,a-ab-[tu]",
                                     "4'. i-na ne2-kur-ti _lu2_ "
                                     "ha-szi-[im{ki}]",
                                     "5'. ur-si-im{ki} _lu2"
                                     "_ ka-ar-ka#-[mi-is{ki}]",
                                     "6'. u3 ia-am-ha-ad[{ki}]",
                                     "7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#",
                                     "8'. i-na ne2-kur-ti "
                                     "{disz}sa-am-si-{d}iszkur#-ma",
                                     "9'. ih-ta-al-qu2",
                                     "10'. u3 a-la-nu sza ki-ma "
                                     "u2-hu-ru u2-sze-zi-ib#",
                                     "11'. u3 na-pa-asz2-ti u2-ba-li-it,",
                                     "12'. pi2-qa-at ha-s,e-ra#-at",
                                     "13'. asz-szum a-la-nu-ka",
                                     "14'. u3 ma-ru-ka sza-al#-[mu]",
                                     "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"]}
        self.assertEqual(cdli.text, goal)

    def test_print_text_editions(self):
        """
        Tests print_text_editions.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        cdli.ingest()
        output = cdli.print_text_editions()
        goal = "text editions: ['ARM 01, 001', 'ARM 01, 002']"
        self.assertEqual(output, goal)

    def test_print_cdli_numbers(self):
        """
        Tests print_cdli_numbers.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        cdli.ingest()
        output = cdli.print_cdli_numbers()
        goal = "cdli numbers: ['&P254202', '&P254203']"
        self.assertEqual(output, goal)

    def test_print_text(self):
        """
        Tests print_text.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        cdli.ingest()
        output = cdli.print_text('ARM 01, 001')
        goal = ['&P254202 = ARM 01, 001',
                '#atf: lang akk',
                '@tablet',
                '@obverse',
                '1. a-na ia-ah-du-li-[im]',
                '2. qi2-bi2-[ma]',
                '3. um-ma a-bi-sa-mar#-[ma]',
                '4. sa-li-ma-am e-pu-[usz]',
                '5. asz-szum mu-sze-zi-ba-am# [la i-szu]',
                '6. [sa]-li#-ma-am sza e-[pu-szu]',
                '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
                '8. [u2-ul] sa-[li-mu-um-ma]',
                '$ rest broken',
                '@reverse',
                '$ beginning broken',
                "1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]",
                "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
                "3'. i-na-an-na is,-s,a-ab-[tu]",
                "4'. i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]",
                "5'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]",
                "6'. u3 ia-am-ha-ad[{ki}]",
                "7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#",
                "8'. i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma",
                "9'. ih-ta-al-qu2",
                "10'. u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#",
                "11'. u3 na-pa-asz2-ti u2-ba-li-it,",
                "12'. pi2-qa-at ha-s,e-ra#-at",
                "13'. asz-szum a-la-nu-ka",
                "14'. u3 ma-ru-ka sza-al#-[mu]",
                "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"]
        self.assertEqual(output, goal)

    def test_print_metadata(self):
        """
        Tests print_metadata.
        """
        path = os.path.join('..', 'texts', 'cdli_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus(text_file)
        cdli.ingest()
        output = cdli.print_metadata('&P254202')
        goal = ['Primary publication: ARM 01, 001',
                'Author(s): Dossin, Georges',
                'Publication date: 1946',
                'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0305',
                'Collection: National Museum of Syria, Damascus, Syria',
                'Museum no.: NMSD —',
                'Accession no.:',
                'Provenience: Mari (mod. Tell Hariri)',
                'Excavation no.:',
                'Period: Old Babylonian (ca. 1900-1600 BC)',
                'Dates referenced:',
                'Object type: tablet',
                'Remarks:',
                'Material: clay',
                'Language: Akkadian',
                'Genre: Letter',
                'Sub-genre:',
                'CDLI comments:',
                'Catalogue source: 20050104 cdliadmin',
                'ATF source: cdlistaff',
                'Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. (en)',
                'UCLA Library ARK: 21198/zz001rsp8x',
                'Composite no.:',
                'Seal no.:',
                'CDLI no.: P254202']
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
