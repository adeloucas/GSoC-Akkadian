"""
This file tests methods in cdli_import.py.
"""

import os
import unittest
from ATFConverter.cdli_import import FileImport # pylint: disable =import-error


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
                 '1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]',
                 '2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]']]
        self.assertEqual(list(output), goal)

    def text_text_contents(self):
        """
        Tests text_contents.
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
        output = cdli.text_contents(text)
        goal = {'&P254202 = ARM 01, 001':
                    ["Primary publication: ARM 01, 001",
                     "Author(s): Dossin, Georges",
                     "&P254202 = ARM 01, 001",
                     "#atf: lang akk",
                     "@tablet",
                     "@obverse",
                     "1. a-na ia-ah-du-li-[im]",
                     "2. qi2-bi2-[ma]",
                     "3. um-ma a-bi-sa-mar#-[ma]"],
                '&P254203 = ARM 01, 002':
                    ["Primary publication: ARM 01, 002",
                     "Author(s): Dossin, Georges",
                     "&P254203 = ARM 01, 002"]}
        self.assertEqual(output, goal)

    def test_texts_within_file(self):
        """
        Tests texts_within_file.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'Akkadian.txt')
        text = cdli.read_file(file)
        goal = "&P249253 = RIME 4.03.06.add21, ex. 01"
        output = cdli.texts_within_file(text)
        self.assertEqual(output, goal)

    def test_text_print(self):
        """
        Tests text_print.
        """
        cdli = FileImport()
        file = os.path.join('..', 'texts', 'Akkadian.txt')
        text = cdli.read_file(file)
        content = cdli.text_contents(text[0:50])
        output = cdli.text_print(content,
                                 '&P249253 = RIME 4.03.06.add21, ex. 01')
        goal = \
"""Primary publication: RIME 4.03.06.add21, ex. 01
Author(s): Frayne, Douglas R.
Publication date: 1990
Secondary publication(s): Bergmann, Eugen, Codex Hammurapi
Collection: Louvre Museum, Paris, France
Museum no.: Sb 00008
Accession no.:
Provenience: Susa (mod. Shush)
Excavation no.:
Period: Old Babylonian (ca. 1900-1600 BC)
Dates referenced: Hammurapi.00.00.00
Object type: other (see object remarks)
Remarks: stele
Material: stone: basalt
Language: Akkadian
Genre: Royal/Monumental
Sub-genre: witness
CDLI comments:
Catalogue source: 20041012 cdliadmin
ATF source: Roth, Martha
Translation:
UCLA Library ARK: 21198/zz001t8p9j
Composite no.: Q006387
Seal no.:
CDLI no.: P249253
Transliteration:
&P249253 = RIME 4.03.06.add21, ex. 01
#atf: lang akk
@object stele
@surface a
@column 1
@prologue
1. i3-nu an s,i-ru-um
2. _lugal_ {d}a-nun-na-ki
3. {d}en-lil2
4. be-el sza-me-e
5. u3 er-s,e-tim
6. sza-i-im
7. szi-ma-at _kalam_
8. a-na {d}marduk
9. _dumu_ re-esz-ti-im
10. sza {d}en-ki
11. {d}en-lil2-ut
12. kisz ni-szi3
13. i-szi-mu-szum
14. in i-gi4-gi4
15. u2-szar-bi2-u3-szu
16. babila{ki}
17. szum-szu s,i-ra-am ib-bi-u3
18. in ki-ib-ra-tim"""
        self.assertEqual(output, goal)
# start with CDLIImport


if __name__ == '__main__':
    unittest.main()
