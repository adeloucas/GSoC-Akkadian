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
    def test_chunk_text(self):
        """
        Tests _chunk_text.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._chunk_text(text_file)  # pylint: disable=protected-access
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

    def test_chunk_text_no_metadata(self):
        """
        Tests _chunk_text.
        """
        path = os.path.join('..', 'texts', 'two_text_no_metadata.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._chunk_text(text_file)  # pylint: disable=protected-access
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


    def test_chunk_text_norm(self):
        """
        Tests chunk_text normalized text finding and collating.
        """
        path = os.path.join('..', 'texts', 'cdli_corpus.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._chunk_text(text_file, only_normalization=True)[2]
        goal = ['&P254202 = ARM 01, 001',
                '#tr.ts: ana yaḫdu-lim',
                '#tr.ts: qibima',
                '#tr.ts: umma abi-samarma',
                '#tr.ts: salīmam ēpuš',
                '#tr.ts: aššum mušēzibam lā īšu',
                '#tr.ts: salīmam ša ēpušu',
                '#tr.ts: ul ēpuš salīmum',
                '#tr.ts: ul salīmumma',
                '#tr.ts: ištu mušēzibam lā īšu',
                '#tr.ts: alānūya ša lā iṣṣabtū',
                '#tr.ts: inanna iṣṣabtū',
                '#tr.ts: ina nekurti awīl ḫaššim',
                '#tr.ts: ursim awīl karkamis',
                '#tr.ts: u yamḫad',
                '#tr.ts: alānū annûtum ul iḫliqū',
                '#tr.ts: ina nekurti samsi-adduma',
                '#tr.ts: iḫtalqū',
                '#tr.ts: u alānū ša kīma uḫḫuru ušezib',
                '#tr.ts: u napaštī uballiṭ',
                '#tr.ts: pīqat ḫaṣerāt',
                '#tr.ts: aššum ālanūka',
                '#tr.ts: u mārūka šalmū',
                '#tr.ts: ana napaštiya itūr']
        self.assertEqual(output, goal)

    def test_find_cdli_number(self):
        """
        Tests find_cdli_number.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._find_cdli_number(text_file)  # pylint: disable=protected-access
        goal = ['&P254202', '&P254203']
        self.assertEqual(output, goal)

    def test_find_edition(self):
        """
        Tests find_edition.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._find_edition(text_file)  # pylint: disable=protected-access
        goal = ['ARM 01, 001', 'ARM 01, 002']
        self.assertEqual(output, goal)

    def test_find_metadata(self):
        """
        Tests find_metadata.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._find_metadata(text_file)  # pylint: disable=protected-access
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
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        output = cdli._find_transliteration(text_file)  # pylint: disable=protected-access
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
        cdli = CDLICorpus()
        cdli._ingest(text_file)  # pylint: disable=protected-access
        goal = {'cdli number': ['&P254202'],
                'text edition': ['ARM 01, 001'],
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
                'transliteration': ['&P254202 = ARM 01, 001',
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

    def test_ingest_text_file(self):
        """
        Tests ingest_text_file
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        goal = [{'cdli number': ['&P254202'],
                 'metadata': ['Primary publication: ARM 01, 001',
                              'Author(s): Dossin, Georges',
                              'Publication date: 1946',
                              'Secondary publication(s): Durand, '
                              'Jean-Marie, LAPO 16, 0305',
                              'Collection: National Museum of '
                              'Syria, Damascus, Syria',
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
                 'text edition': ['ARM 01, 001'],
                 'transliteration': ['&P254202 = ARM 01, 001',
                                     '#atf: lang akk',
                                     '@tablet',
                                     '@obverse',
                                     '1. a-na ia-ah-du-li-[im]',
                                     '2. qi2-bi2-[ma]',
                                     '3. um-ma a-bi-sa-mar#-[ma]',
                                     '4. sa-li-ma-am e-pu-[usz]',
                                     '5. asz-szum mu-sze-zi-ba-am# '
                                     '[la i-szu]',
                                     '6. [sa]-li#-ma-am sza e-[pu-szu]',
                                     '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
                                     '8. [u2-ul] sa-[li-mu-um-ma]',
                                     '$ rest broken',
                                     '@reverse',
                                     '$ beginning broken',
                                     "1'. isz#-tu mu#-[sze-zi-ba-am "
                                     "la i-szu]",
                                     "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
                                     "3'. i-na-an-na is,-s,a-ab-[tu]",
                                     "4'. i-na ne2-kur-ti _lu2_ "
                                     "ha-szi-[im{ki}]",
                                     "5'. ur-si-im{ki} _lu2_ "
                                     "ka-ar-ka#-[mi-is{ki}]",
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
                                     "15'. [a-na na-pa]-asz2#-ti-ia "
                                     "i-tu-ur"]},
                {'cdli number': ['&P254203'],
                 'metadata': ['Primary publication: ARM 01, 002',
                              'Author(s): Dossin, Georges',
                              'Publication date: 1946',
                              'Secondary publication(s): Durand, '
                              'Jean-Marie, LAPO 16, 0306',
                              'Collection: National Museum of '
                              'Syria, Damascus, Syria',
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
                              'CDLI no.: P254203'],
                 'text edition': ['ARM 01, 002'],
                 'transliteration': ['&P254203 = ARM 01, 002',
                                     '#atf: lang akk',
                                     '@tablet',
                                     '@obverse',
                                     '1. a-na ia-ah-du-[li-im]',
                                     '2. qi2-bi2-[ma]',
                                     '3. um-ma a-bi-sa-mar-[ma]',
                                     '4. asz-szum sza a-qa-bi-kum '
                                     'la ta-ha-asz2#',
                                     '5. a-na ma-ni-im lu-ud-bu-ub',
                                     '6. szum-ma a-na?-<ku> a-na '
                                     'a-bi-ia la ad#-[bu-ub]',
                                     '7. szum-ma a-bi-sa-mar te-zi-ir#',
                                     '8. u3 a-la#-ni#-ka te-zi-ir-ma#',
                                     '9. i-na an-ni-a-tim sza a-da-bu-[bu]',
                                     '10. a-na-ku mi-im-ma u2-ul e-le#-[i]',
                                     '11. sza sza-ru-ti-ka u3 sza '
                                     'ra-pa#-[szi-ka e-pu-usz]',
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
                                     "11'. pi2-qa-at ta-qa-ab#-[bi "
                                     "um-ma at-ta-a-ma]",
                                     '@left',
                                     '1. {disz}a-bi-sa-mar u2-ul ma-ri '
                                     'u3 bi-ti a-na la '
                                     'bi-tu#-[tu-ur2-ma]',
                                     '2. bi-tum bi-it-ka u3 '
                                     '{disz}a-bi#-[sa]-mar# '
                                     'ma-ru-ka-[ma]']}]
        self.assertEqual(cdli.texts, goal)

    def test_table_of_contents(self):
        """
        Tests table_of_contents.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        output = cdli.table_of_contents()
        goal = ["edition: ['ARM 01, 001']; cdli number: ['&P254202']",
                "edition: ['ARM 01, 002']; cdli number: ['&P254203']"]
        self.assertEqual(output, goal)

    def test_call_text(self):
        """
        Tests call_text.
        """
        path = os.path.join('..', 'texts', 'ARM1Akkadian.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        output = cdli.call_text('&P254226')
        goal = ['&P254226 = ARM 01, 025',
                '#version: 0.1',
                '#atf: lang akk',
                '@tablet',
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

    def test_abnormalities(self):
        """Tests lines 83, 102, 121-2"""
        path = os.path.join('..', 'texts', 'two_text_abnormalities.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        goal = [{'cdli number': ['P254202'],
                 'metadata': 'None found.',
                 'text edition': ['ARM 01, 001'],
                 'transliteration': ['P254202 = ARM 01, 001',
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
                                     "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"]},
                {'cdli number': ['&P254203'],
                 'metadata': 'None found.',
                 'text edition': [''],
                 'transliteration': ['&P254203 =',
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
                                     '1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la '
                                     'bi-tu#-[tu-ur2-ma]',
                                     '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# '
                                     'ma-ru-ka-[ma]']}]
        self.assertEqual(cdli.texts, goal)

    def test_call_metadata(self):
        """
        Tests call_metadata.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        output = cdli.call_metadata('&P254202')
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
