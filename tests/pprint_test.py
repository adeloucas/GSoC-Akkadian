"""
This file tests methods in pretty_print.py.
"""

import unittest
import os
from Importer.file_importer import FileImport  # pylint: disable =import-error
from Importer.cdli_corpus import CDLICorpus  # pylint: disable =import-error
from PrettyPrint.pretty_print import PrettyPrint  # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_markdown_single_text(self):
        """
        Tests markdown_single_text.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        p_p = PrettyPrint()
        p_p.markdown_single_text(cdli.texts, 'P254203')
        output = p_p.markdown_text
        goal = """ARM 01, 002
---
### metadata
    Primary publication: ARM 01, 002
 	Author(s): Dossin, Georges
 	Publication date: 1946
 	Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0306
 	Collection: National Museum of Syria, Damascus, Syria
 	Museum no.: NMSD —
 	Accession no.:
 	Provenience: Mari (mod. Tell Hariri)
 	Excavation no.:
 	Period: Old Babylonian (ca. 1900-1600 BC)
 	Dates referenced:
 	Object type: tablet
 	Remarks:
 	Material: clay
 	Language: Akkadian
 	Genre: Letter
 	Sub-genre:
 	CDLI comments:
 	Catalogue source: 20050104 cdliadmin
 	ATF source: cdlistaff
 	Translation:
 	UCLA Library ARK: 21198/zz001rsp9f
 	Composite no.:
 	Seal no.:
 	CDLI no.: P254203
### transliteration
    &P254203 = ARM 01, 002
 	#atf: lang akk
 	@tablet
 	@obverse
 	1. a-na ia-ah-du-[li-im]
 	2. qi2-bi2-[ma]
 	3. um-ma a-bi-sa-mar-[ma]
 	4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#
 	5. a-na ma-ni-im lu-ud-bu-ub
 	6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]
 	7. szum-ma a-bi-sa-mar te-zi-ir#
 	8. u3 a-la#-ni#-ka te-zi-ir-ma#
 	9. i-na an-ni-a-tim sza a-da-bu-[bu]
 	10. a-na-ku mi-im-ma u2-ul e-le#-[i]
 	11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]
 	12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]
 	13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]
 	14. u3 lu ma-at ia-ma-ha-ad#{ki}
 	15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]
 	$ rest broken
 	@reverse
 	$ beginning broken
 	1'. um#-[...]
 	2'. lu#-[...]
 	3'. a-[...]
 	4'. szum#-[...]
 	5'. a-na# [...]
 	6'. ma-li# [...]
 	7'. u3 u2-hu-ur# [...]
 	8'. a-su2-ur-ri [...]
 	9'. szu-zi-ba-an#-[ni ...]
 	10'. a-na [...]
 	11'. pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]
 	@left
 	1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]
 	2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]  
"""
        self.assertEqual(output, goal)

    def test_html_print_file(self):
        """
        Tests html_print_file.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        destination = os.path.join('..', 'tests', 'html_file.html')
        p_p = PrettyPrint()
        p_p.html_print_file(cdli.texts, destination)
        f_o = FileImport(destination)
        f_o.read_file()
        output = f_o.raw_file
        goal = \
"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ARM 01, 001</title>
</head>
<body><table cellpadding="10"; border="1">
<tr><th>
<h2>ARM 01, 001</h2>
</th><th>
<h3>metadata</h3>
</th><th>
<h3>transliteration</h3>
</th></tr><tr><td></td><td>
<font size='2'>
    Primary publication: ARM 01, 001<br> 
Author(s): Dossin, Georges<br> 
Publication date: 1946<br> 
Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0305<br> 
Collection: National Museum of Syria, Damascus, Syria<br> 
Museum no.: NMSD —<br> 
Accession no.:<br> 
Provenience: Mari (mod. Tell Hariri)<br> 
Excavation no.:<br> 
Period: Old Babylonian (ca. 1900-1600 BC)<br> 
Dates referenced:<br> 
Object type: tablet<br> 
Remarks:<br> 
Material: clay<br> 
Language: Akkadian<br> 
Genre: Letter<br> 
Sub-genre:<br> 
CDLI comments:<br> 
Catalogue source: 20050104 cdliadmin<br> 
ATF source: cdlistaff<br> 
Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. (en)<br> 
UCLA Library ARK: 21198/zz001rsp8x<br> 
Composite no.:<br> 
Seal no.:<br> 
CDLI no.: P254202     
</font></td><td>
<p>&P254202 = ARM 01, 001<br> 
#atf: lang akk<br> 
@tablet<br> 
@obverse<br> 
1. a-na ia-ah-du-li-[im]<br> 
2. qi2-bi2-[ma]<br> 
3. um-ma a-bi-sa-mar#-[ma]<br> 
4. sa-li-ma-am e-pu-[usz]<br> 
5. asz-szum mu-sze-zi-ba-am# [la i-szu]<br> 
6. [sa]-li#-ma-am sza e-[pu-szu]<br> 
7. [u2-ul] e-pu-usz sa#-[li-mu-um]<br> 
8. [u2-ul] sa-[li-mu-um-ma]<br> 
$ rest broken<br> 
@reverse<br> 
$ beginning broken<br> 
1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]<br> 
2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]<br> 
3'. i-na-an-na is,-s,a-ab-[tu]<br> 
4'. i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]<br> 
5'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]<br> 
6'. u3 ia-am-ha-ad[{ki}]<br> 
7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#<br> 
8'. i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma<br> 
9'. ih-ta-al-qu2<br> 
10'. u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#<br> 
11'. u3 na-pa-asz2-ti u2-ba-li-it,<br> 
12'. pi2-qa-at ha-s,e-ra#-at<br> 
13'. asz-szum a-la-nu-ka<br> 
14'. u3 ma-ru-ka sza-al#-[mu]<br> 
15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur
</td></tr></table>
<br>
</body>
</html><!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ARM 01, 002</title>
</head>
<body><table cellpadding="10"; border="1">
<tr><th>
<h2>ARM 01, 002</h2>
</th><th>
<h3>metadata</h3>
</th><th>
<h3>transliteration</h3>
</th></tr><tr><td></td><td>
<font size='2'>
    Primary publication: ARM 01, 002<br> 
Author(s): Dossin, Georges<br> 
Publication date: 1946<br> 
Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0306<br> 
Collection: National Museum of Syria, Damascus, Syria<br> 
Museum no.: NMSD —<br> 
Accession no.:<br> 
Provenience: Mari (mod. Tell Hariri)<br> 
Excavation no.:<br> 
Period: Old Babylonian (ca. 1900-1600 BC)<br> 
Dates referenced:<br> 
Object type: tablet<br> 
Remarks:<br> 
Material: clay<br> 
Language: Akkadian<br> 
Genre: Letter<br> 
Sub-genre:<br> 
CDLI comments:<br> 
Catalogue source: 20050104 cdliadmin<br> 
ATF source: cdlistaff<br> 
Translation:<br> 
UCLA Library ARK: 21198/zz001rsp9f<br> 
Composite no.:<br> 
Seal no.:<br> 
CDLI no.: P254203     
</font></td><td>
<p>&P254203 = ARM 01, 002<br> 
#atf: lang akk<br> 
@tablet<br> 
@obverse<br> 
1. a-na ia-ah-du-[li-im]<br> 
2. qi2-bi2-[ma]<br> 
3. um-ma a-bi-sa-mar-[ma]<br> 
4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#<br> 
5. a-na ma-ni-im lu-ud-bu-ub<br> 
6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]<br> 
7. szum-ma a-bi-sa-mar te-zi-ir#<br> 
8. u3 a-la#-ni#-ka te-zi-ir-ma#<br> 
9. i-na an-ni-a-tim sza a-da-bu-[bu]<br> 
10. a-na-ku mi-im-ma u2-ul e-le#-[i]<br> 
11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]<br> 
12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]<br> 
13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]<br> 
14. u3 lu ma-at ia-ma-ha-ad#{ki}<br> 
15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]<br> 
$ rest broken<br> 
@reverse<br> 
$ beginning broken<br> 
1'. um#-[...]<br> 
2'. lu#-[...]<br> 
3'. a-[...]<br> 
4'. szum#-[...]<br> 
5'. a-na# [...]<br> 
6'. ma-li# [...]<br> 
7'. u3 u2-hu-ur# [...]<br> 
8'. a-su2-ur-ri [...]<br> 
9'. szu-zi-ba-an#-[ni ...]<br> 
10'. a-na [...]<br> 
11'. pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]<br> 
@left<br> 
1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]<br> 
2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]
</td></tr></table>
<br>
</body>
</html>"""
        self.assertEqual(output, goal)

    def test_html_print_single_text(self):
        """
        Tests html_print_single_text.
        """
        path = os.path.join('..', 'texts', 'two_text.txt')
        destination = os.path.join('..', 'tests', 'html_single_text.html')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.ingest_text_file(text_file)
        p_p = PrettyPrint()
        p_p.html_print_single_text(cdli.texts, '&P254203', destination)
        f_o = FileImport(destination)
        f_o.read_file()
        output = f_o.raw_file
        goal = \
            """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ARM 01, 002</title>
</head>
<body><table cellpadding="10"; border="1">
<tr><th>
<h2>ARM 01, 002</h2>
</th><th>
<h3>metadata</h3>
</th><th>
<h3>transliteration</h3>
</th></tr><tr><td></td><td>
<font size='2'>
    Primary publication: ARM 01, 002<br> 
Author(s): Dossin, Georges<br> 
Publication date: 1946<br> 
Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0306<br> 
Collection: National Museum of Syria, Damascus, Syria<br> 
Museum no.: NMSD —<br> 
Accession no.:<br> 
Provenience: Mari (mod. Tell Hariri)<br> 
Excavation no.:<br> 
Period: Old Babylonian (ca. 1900-1600 BC)<br> 
Dates referenced:<br> 
Object type: tablet<br> 
Remarks:<br> 
Material: clay<br> 
Language: Akkadian<br> 
Genre: Letter<br> 
Sub-genre:<br> 
CDLI comments:<br> 
Catalogue source: 20050104 cdliadmin<br> 
ATF source: cdlistaff<br> 
Translation:<br> 
UCLA Library ARK: 21198/zz001rsp9f<br> 
Composite no.:<br> 
Seal no.:<br> 
CDLI no.: P254203     
</font></td><td>
<p>&P254203 = ARM 01, 002<br> 
#atf: lang akk<br> 
@tablet<br> 
@obverse<br> 
1. a-na ia-ah-du-[li-im]<br> 
2. qi2-bi2-[ma]<br> 
3. um-ma a-bi-sa-mar-[ma]<br> 
4. asz-szum sza a-qa-bi-kum la ta-ha-asz2#<br> 
5. a-na ma-ni-im lu-ud-bu-ub<br> 
6. szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]<br> 
7. szum-ma a-bi-sa-mar te-zi-ir#<br> 
8. u3 a-la#-ni#-ka te-zi-ir-ma#<br> 
9. i-na an-ni-a-tim sza a-da-bu-[bu]<br> 
10. a-na-ku mi-im-ma u2-ul e-le#-[i]<br> 
11. sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]<br> 
12. u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]<br> 
13. u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]<br> 
14. u3 lu ma-at ia-ma-ha-ad#{ki}<br> 
15. u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]<br> 
$ rest broken<br> 
@reverse<br> 
$ beginning broken<br> 
1'. um#-[...]<br> 
2'. lu#-[...]<br> 
3'. a-[...]<br> 
4'. szum#-[...]<br> 
5'. a-na# [...]<br> 
6'. ma-li# [...]<br> 
7'. u3 u2-hu-ur# [...]<br> 
8'. a-su2-ur-ri [...]<br> 
9'. szu-zi-ba-an#-[ni ...]<br> 
10'. a-na [...]<br> 
11'. pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]<br> 
@left<br> 
1. {disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]<br> 
2. bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]
</td></tr></table>
<br>
</body>
</html>"""
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
