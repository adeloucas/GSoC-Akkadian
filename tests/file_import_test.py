"""
This file tests methods in file_import.py.
"""

import os
import unittest
from Importer.file_import import FileImport  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_read_file(self):
        """
        Tests __read_file__.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'Akkadian.txt')
        output = cdli.read_file(file)
        final = output[3042:3054]
        goal = ['24. _{gesz}ma2_ dan-na-tam',
                '25. a-na be-el _{gesz}ma2_',
                '26. i-na-ad-di-in',
                '@law 236',
                '27. szum-ma a-wi-lum',
                '28. _{gesz}ma2_-szu',
                '29. a-na _ma2-lah5_',
                '30. a-na ig-ri-im',
                '31. id-di-in-ma',
                '32. _ma2-lah5_ i-gi-ma',
                '33. _{gesz}ma2_ ut,-t,e4-bi',
                '34. u3 lu uh2-ta-al-li-iq']
        self.assertEqual(final, goal)

    def test_discern_texts(self):
        """
        Tests __discern_texts__.
        """
        cdli = FileImport()
        text = \
            ["Primary publication: ARM 01, 001",
             "Author(s): Dossin, Georges",
             "&P254202 = ARM 01, 001",
             "#atf: lang akk",
             "@tablet",
             "@obverse",
             "1. a-na ia-ah-du-li-[im]",
             "2. qi2-bi2-[ma]",
             "3. um-ma a-bi-sa-mar#-[ma]",
             "Primary publication: ARM 01, 002",
             "Author(s): Dossin, Georges",
             "&P254203 = ARM 01, 002"]
        output = cdli.__discern_texts__(text)
        goal = ["&P254202 = ARM 01, 001", "&P254203 = ARM 01, 002"]
        self.assertEqual(output, goal)

    def test_split_texts(self):
        """
        Tests __split_texts__.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'cdli_text.txt')
        text = cdli.read_file(file)
        output = cdli.__split_texts__(text)
        goal = ([['&P254202 = ARM 01, 001',
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
                  '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# '
                  'ma-ru-ka-[ma]']])
        self.maxDiff = None                 # pylint: disable =invalid-name
        self.assertEqual(output, goal)

    def test_texts_within_file(self):
        """
        Tests texts_within_file.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'ARM1Akkadian.txt')
        text = cdli.read_file(file)
        goal = ['&P254202 = ARM 01, 001',
                '&P254203 = ARM 01, 002',
                '&P254204 = ARM 01, 003',
                '&P254205 = ARM 01, 004',
                '&P254206 = ARM 01, 005',
                '&P254207 = ARM 01, 006',
                '&P254208 = ARM 01, 007',
                '&P254209 = ARM 01, 008',
                '&P254210 = ARM 01, 009',
                '&P254211 = ARM 01, 010',
                '&P254212 = ARM 01, 011',
                '&P254213 = ARM 01, 012',
                '&P254214 = ARM 01, 013',
                '&P254215 = ARM 01, 014',
                '&P254216 = ARM 01, 015']
        output = cdli.texts_within_file(text[0:1000])
        self.assertEqual(output, goal)

    def test_text_contents(self):
        """
        Tests text_contents.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'cdli_text.txt')
        text = cdli.read_file(file)
        output = cdli.__text_contents__(text)
        goal = {'&P254202 = ARM 01, 001':
                    ["&P254202 = ARM 01, 001",
                     "#atf: lang akk",
                     "@tablet",
                     "@obverse",
                     "1. a-na ia-ah-du-li-[im]",
                     "2. qi2-bi2-[ma]",
                     "3. um-ma a-bi-sa-mar#-[ma]",
                     "4. sa-li-ma-am e-pu-[usz]",
                     "5. asz-szum mu-sze-zi-ba-am# [la i-szu]",
                     "6. [sa]-li#-ma-am sza e-[pu-szu]",
                     "7. [u2-ul] e-pu-usz sa#-[li-mu-um]",
                     "8. [u2-ul] sa-[li-mu-um-ma]",
                     "$ rest broken",
                     "@reverse",
                     "$ beginning broken",
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
                '&P254203 = ARM 01, 002':
                    ["&P254203 = ARM 01, 002",
                     "#atf: lang akk",
                     "@tablet",
                     "@obverse",
                     "1. a-na ia-ah-du-[li-im]",
                     "2. qi2-bi2-[ma]",
                     "3. um-ma a-bi-sa-mar-[ma]",
                     "4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#",
                     "5. a-na ma-ni-im lu-ud-bu-ub",
                     "6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]",
                     "7. szum-ma a-bi-sa-mar te-zi-ir#",
                     "8. u3 a-la#-ni#-ka te-zi-ir-ma#",
                     "9. i-na an-ni-a-tim sza a-da-bu-[bu]",
                     "10. a-na-ku mi-im-ma u2-ul e-le#-[i]",
                     "11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]",
                     "12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]",
                     "13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]",
                     "14. u3 lu ma-at ia-ma-ha-ad#{ki}",
                     "15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]",
                     "$ rest broken",
                     "@reverse",
                     "$ beginning broken",
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
                     "@left",
                     "1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti "
                     "a-na la bi-tu#-[tu-ur2-ma]",
                     "2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# "
                     "ma-ru-ka-[ma]"]}

        self.assertEqual(output, goal)

    def test_text_print(self):
        """
        Tests text_print.
        """
        cdli = FileImport()
        output = cdli.text_print('cdli_text.txt', '&P254202 = ARM 01, 001')
        goal = ["&P254202 = ARM 01, 001",
                "#atf: lang akk",
                "@tablet",
                "@obverse",
                "1. a-na ia-ah-du-li-[im]",
                "2. qi2-bi2-[ma]",
                "3. um-ma a-bi-sa-mar#-[ma]",
                "4. sa-li-ma-am e-pu-[usz]",
                "5. asz-szum mu-sze-zi-ba-am# [la i-szu]",
                "6. [sa]-li#-ma-am sza e-[pu-szu]",
                "7. [u2-ul] e-pu-usz sa#-[li-mu-um]",
                "8. [u2-ul] sa-[li-mu-um-ma]",
                "$ rest broken",
                "@reverse",
                "$ beginning broken",
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


if __name__ == '__main__':
    unittest.main()
