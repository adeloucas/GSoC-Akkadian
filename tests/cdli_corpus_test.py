"""
This file tests methods in cdli_corpus.py.
"""

import unittest
import os
from Importer.file_importer import FileImport  # pylint: disable =import-error
from Importer.cdli_corpus import CDLICorpus  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests CDLICorpus class.
    """
    def test_parse_file(self):
        """
        Tests parse_file.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.chunks
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

    def test_call_text(self):
        """
        Tests calling a text.
        """
        path = os.path.join('..', 'texts', 'ARM1Akkadian.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.catalog['P254226']['raw_text']
        goal = ['@tablet',
                '@obverse',
                '@column 1',
                '1. a-na ia-as2-ma-ah-{d}iszkur',
                '2. qi2-bi2-ma',
                '3. um-ma {d}utu-szi-{d}iszkur',
                '4. a-bu-ka-a-ma',
                '5. asz-szum _{lu2}nagar mesz_ sza tu-ut-tu-ul{ki}',
                '6. sza i-na szu-ba-at-{d}utu{ki} wa-asz-bu',
                '7. a-na tu-ut-tu-ul{ki}',
                '8. tu-ur-ri-im',
                '9. sza ta-asz-pu-ra-am',
                '10. a-na {d!}iszkur-lu2-ti',
                '11. asz3-ta-pa-ar _{lu2}nagar mesz_ szu-nu-ti',
                '12. a-na tu-ut-tu-ul{ki}',
                '13. u2-ta-ar',
                '14. u3 qa-as-su2-nu li-isz-ku-nu-ma',
                '15. {gesz}ma2-tu{hi-a} li-pu-szu']
        self.assertEqual(output, goal)

    def test_find_cdli_number(self):
        """
        Tests list_pnums.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.list_pnums()
        goal = ['P254202', 'P254203']
        self.assertEqual(output, goal)

    def test_find_edition(self):
        """
        Tests list_editions.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.list_editions()
        goal = ['ARM 01, 001', 'ARM 01, 002']
        self.assertEqual(output, goal)

    def test_find_metadata(self):
        """
        Tests calling metadata in a file.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = [cdli.catalog[text]['metadata'] for text in cdli.catalog]
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
        Tests calling transliteration in a file.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = [cdli.catalog[text]['transliteration'] for text in cdli.catalog]
        goal = [['a-na ia-ah-du-li-[im]',
                 'qi2-bi2-[ma]',
                 'um-ma a-bi-sa-mar#-[ma]',
                 'sa-li-ma-am e-pu-[usz]',
                 'asz-szum mu-sze-zi-ba-am# [la i-szu]',
                 '[sa]-li#-ma-am sza e-[pu-szu]',
                 '[u2-ul] e-pu-usz sa#-[li-mu-um]',
                 '[u2-ul] sa-[li-mu-um-ma]',
                 'isz#-tu mu#-[sze-zi-ba-am la i-szu]',
                 'a-la-nu-ia sza la is,-s,a-ab#-[tu]',
                 'i-na-an-na is,-s,a-ab-[tu]',
                 'i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]',
                 'ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]',
                 'u3 ia-am-ha-ad[{ki}]',
                 'a-la-nu an-nu-tum u2-ul ih-li-qu2#',
                 'i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma',
                 'ih-ta-al-qu2',
                 'u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#',
                 'u3 na-pa-asz2-ti u2-ba-li-it,',
                 'pi2-qa-at ha-s,e-ra#-at',
                 'asz-szum a-la-nu-ka',
                 'u3 ma-ru-ka sza-al#-[mu]',
                 '[a-na na-pa]-asz2#-ti-ia i-tu-ur'],
                ['a-na ia-ah-du-[li-im]',
                 'qi2-bi2-[ma]',
                 'um-ma a-bi-sa-mar-[ma]',
                 'asz-szum sza a-qa-bi-kum la ta-ha-asz2#',
                 'a-na ma-ni-im lu-ud-bu-ub',
                 'szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]',
                 'szum-ma a-bi-sa-mar te-zi-ir#',
                 'u3 a-la#-ni#-ka te-zi-ir-ma#',
                 'i-na an-ni-a-tim sza a-da-bu-[bu]',
                 'a-na-ku mi-im-ma u2-ul e-le#-[i]',
                 'sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]',
                 'u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]',
                 'u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]',
                 'u3 lu ma-at ia-ma-ha-ad#{ki}',
                 'u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]',
                 'um#-[...]',
                 'lu#-[...]',
                 'a-[...]',
                 'szum#-[...]',
                 'a-na# [...]',
                 'ma-li# [...]',
                 'u3 u2-hu-ur# [...]',
                 'a-su2-ur-ri [...]',
                 'szu-zi-ba-an#-[ni ...]',
                 'a-na [...]',
                 'pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]',
                 '{disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]',
                 'bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]']]
        self.assertEqual(output, goal)

    def test_table_of_contents(self):
        """
        Tests toc.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.toc()
        goal = ['Pnum: P254202, Edition: ARM 01, 001, length: 23 line(s)',
                'Pnum: P254203, Edition: ARM 01, 002, length: 28 line(s)']
        self.assertEqual(output, goal)

    def test_abnormalities(self):
        """Tests lines 83, 102, 121-2"""
        path = os.path.join('..', 'texts', 'two_text_abnormalities.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.parse_file(text_file)
        goal = {'P254202': {'edition': 'ARM 01, 001',
                            'metadata': [],
                            'normalization': [],
                            'pnum': 'P254202',
                            'raw_text': ['@obverse',
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
                            'translation': [],
                            'transliteration': ['a-na ia-ah-du-li-[im]',
                                                'qi2-bi2-[ma]',
                                                'um-ma a-bi-sa-mar#-[ma]',
                                                'sa-li-ma-am e-pu-[usz]',
                                                'asz-szum mu-sze-zi-ba-am# [la i-szu]',
                                                '[sa]-li#-ma-am sza e-[pu-szu]',
                                                '[u2-ul] e-pu-usz sa#-[li-mu-um]',
                                                '[u2-ul] sa-[li-mu-um-ma]',
                                                'isz#-tu mu#-[sze-zi-ba-am la i-szu]',
                                                'a-la-nu-ia sza la is,-s,a-ab#-[tu]',
                                                'i-na-an-na is,-s,a-ab-[tu]',
                                                'i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]',
                                                'ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]',
                                                'u3 ia-am-ha-ad[{ki}]',
                                                'a-la-nu an-nu-tum u2-ul ih-li-qu2#',
                                                'i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma',
                                                'ih-ta-al-qu2',
                                                'u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#',
                                                'u3 na-pa-asz2-ti u2-ba-li-it,',
                                                'pi2-qa-at ha-s,e-ra#-at',
                                                'asz-szum a-la-nu-ka',
                                                'u3 ma-ru-ka sza-al#-[mu]',
                                                '[a-na na-pa]-asz2#-ti-ia i-tu-ur']},
                'P254203': {'edition': '',
                            'metadata': [],
                            'normalization': [],
                            'pnum': 'P254203',
                            'raw_text': ['@obverse',
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
                                         '1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]',
                                         '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]'],
                            'translation': [],
                            'transliteration': ['a-na ia-ah-du-[li-im]',
                                                'qi2-bi2-[ma]',
                                                'um-ma a-bi-sa-mar-[ma]',
                                                'asz-szum sza a-qa-bi-kum la ta-ha-asz2#',
                                                'a-na ma-ni-im lu-ud-bu-ub',
                                                'szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]',
                                                'szum-ma a-bi-sa-mar te-zi-ir#',
                                                'u3 a-la#-ni#-ka te-zi-ir-ma#',
                                                'i-na an-ni-a-tim sza a-da-bu-[bu]',
                                                'a-na-ku mi-im-ma u2-ul e-le#-[i]',
                                                'sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]',
                                                'u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]',
                                                'u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]',
                                                'u3 lu ma-at ia-ma-ha-ad#{ki}',
                                                'u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]',
                                                'um#-[...]',
                                                'lu#-[...]',
                                                'a-[...]',
                                                'szum#-[...]',
                                                'a-na# [...]',
                                                'ma-li# [...]',
                                                'u3 u2-hu-ur# [...]',
                                                'a-su2-ur-ri [...]',
                                                'szu-zi-ba-an#-[ni ...]',
                                                'a-na [...]',
                                                'pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]',
                                                '{disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]',
                                                'bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]']}}
        self.assertEqual(cdli.catalog, goal)

    def test_print_catalog(self):
        """
        Tests _chunk_text.
        """
        path = os.path.join('..', 'texts', 'single_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        cdli = CDLICorpus()
        cdli.parse_file(f_i.file_lines)
        output = cdli.print_catalog(catalog_filter=['transliteration'])
        goal = print(output)
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
