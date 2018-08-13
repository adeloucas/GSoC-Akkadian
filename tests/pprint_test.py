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
        path = os.path.join('..', 'texts', 'cdli_corpus.txt')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.parse_file(text_file)
        p_p = PrettyPrint()
        p_p.markdown_single_text(cdli.catalog, 'P254203')
        output = p_p.markdown_text
        goal = """ARM 01, 002
P254203
---
### metadata
    
### transliteration
    a-na ia-ah-du-[li-im]
	qi2-bi2-[ma]
	um-ma a-bi-sa-mar-[ma]
	asz-szum sza a-qa-bi-kum la ta-ha-asz2#
	a-na ma-ni-im lu-ud-bu-ub
	szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]
	szum-ma a-bi-sa-mar te-zi-ir#
	u3 a-la#-ni#-ka te-zi-ir-ma#
	i-na an-ni-a-tim sza a-da-bu-[bu]
	a-na-ku mi-im-ma u2-ul e-le#-[i]
	sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]
	u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]
	u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]
	u3 lu ma-at ia-ma-ha-ad#{ki}
	u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]
	um#-[...]
	lu#-[...]
	a-[...]
	szum#-[...]
	a-na# [...]
	ma-li# [...]
	u3 u2-hu-ur# [...]
	a-su2-ur-ri [...]
	szu-zi-ba-an#-[ni ...]
	a-na [...]
	pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]
	{disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]
	bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]
### normalization
    
### translation
      
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
        cdli.parse_file(text_file)
        destination = os.path.join('..', 'tests', 'html_file.html')
        p_p = PrettyPrint()
        p_p.html_print_file(cdli.catalog, destination)
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
<h2>ARM 01, 001<br>P254202</h2>
</th><th>
<h3>transliteration</h3>
</th><th>
<h3>normalization</h3>
</th><th>
<h3>translation</h3>
</tr><tr><td>
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
CDLI no.: P254202</td><td>
<p>a-na ia-ah-du-li-[im]<br>
qi2-bi2-[ma]<br>
um-ma a-bi-sa-mar#-[ma]<br>
sa-li-ma-am e-pu-[usz]<br>
asz-szum mu-sze-zi-ba-am# [la i-szu]<br>
[sa]-li#-ma-am sza e-[pu-szu]<br>
[u2-ul] e-pu-usz sa#-[li-mu-um]<br>
[u2-ul] sa-[li-mu-um-ma]<br>
isz#-tu mu#-[sze-zi-ba-am la i-szu]<br>
a-la-nu-ia sza la is,-s,a-ab#-[tu]<br>
i-na-an-na is,-s,a-ab-[tu]<br>
i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]<br>
ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]<br>
u3 ia-am-ha-ad[{ki}]<br>
a-la-nu an-nu-tum u2-ul ih-li-qu2#<br>
i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma<br>
ih-ta-al-qu2<br>
u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#<br>
u3 na-pa-asz2-ti u2-ba-li-it,<br>
pi2-qa-at ha-s,e-ra#-at<br>
asz-szum a-la-nu-ka<br>
u3 ma-ru-ka sza-al#-[mu]<br>
[a-na na-pa]-asz2#-ti-ia i-tu-ur
</td><td>
<p>
</td><td>
<font size='2'>

</font></td></tr>

</table>
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
<h2>ARM 01, 002<br>P254203</h2>
</th><th>
<h3>transliteration</h3>
</th><th>
<h3>normalization</h3>
</th><th>
<h3>translation</h3>
</tr><tr><td>
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
CDLI no.: P254203</td><td>
<p>a-na ia-ah-du-[li-im]<br>
qi2-bi2-[ma]<br>
um-ma a-bi-sa-mar-[ma]<br>
asz-szum sza a-qa-bi-kum la ta-ha-asz2#<br>
a-na ma-ni-im lu-ud-bu-ub<br>
szum-ma a-na?-<ku> a-na a-bi-ia la ad#-[bu-ub]<br>
szum-ma a-bi-sa-mar te-zi-ir#<br>
u3 a-la#-ni#-ka te-zi-ir-ma#<br>
i-na an-ni-a-tim sza a-da-bu-[bu]<br>
a-na-ku mi-im-ma u2-ul e-le#-[i]<br>
sza sza-ru-ti-ka u3 sza ra-pa#-[szi-ka e-pu-usz]<br>
u3 lu-u2 sza sza-ru-ut-ka u2-ul te-le#-[i]<br>
u3 lu-u2 sza ra-pa-szi-ka [te-ep-pe2-esz]<br>
u3 lu ma-at ia-ma-ha-ad#{ki}<br>
u3# lu# _u4 8(disz)-kam_ isz-tu [i-na-an-na]<br>
um#-[...]<br>
lu#-[...]<br>
a-[...]<br>
szum#-[...]<br>
a-na# [...]<br>
ma-li# [...]<br>
u3 u2-hu-ur# [...]<br>
a-su2-ur-ri [...]<br>
szu-zi-ba-an#-[ni ...]<br>
a-na [...]<br>
pi2-qa-at ta-qa-ab#-[bi um-ma at-ta-a-ma]<br>
{disz}a-bi-sa-mar u2-ul ma-ri u3 bi-ti a-na la bi-tu#-[tu-ur2-ma]<br>
bi-tum bi-it-ka u3 {disz}a-bi#-[sa]-mar# ma-ru-ka-[ma]
</td><td>
<p>
</td><td>
<font size='2'>

</font></td></tr>

</table>
<br>
</body>
</html>"""
        self.assertEqual(output, goal)

    def test_html_print_single_text(self):
        """
        Tests html_print_single_text.
        """
        path = os.path.join('..', 'texts', 'cdli_corpus.txt')
        destination = os.path.join('..', 'tests', 'html_single_text.html')
        f_i = FileImport(path)
        f_i.read_file()
        text_file = f_i.file_lines
        cdli = CDLICorpus()
        cdli.parse_file(text_file)
        p_p = PrettyPrint()
        p_p.html_print_single_text(cdli.catalog, 'P500444', destination)
        f_o = FileImport(destination)
        f_o.read_file()
        output = f_o.raw_file
        goal = \
            """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>NABU 2017/015</title>
</head>
<body><table cellpadding="10"; border="1">
<tr><th>
<h2>NABU 2017/015<br>P500444</h2>
</th><th>
<h3>transliteration</h3>
</th><th>
<h3>normalization</h3>
</th><th>
<h3>translation</h3>
</tr><tr><td>
</td><td>
<p>a-na {d}nin-urta<br>
be-li2 ra-bi-i<br>
be-li2-szu<br>
ka-dasz2-man-{d}en-lil2<br>
_lugal_ babila2{ki}<br>
_dumu_ ka-dasz2-man-tur2-gu _lugal_<br>
a-na szu-ru-uk _bala_-szu<br>
i-qi2-isz
</td><td>
<p>ana ninurta<br>
bēli rabî<br>
bēlišu<br>
kadašman-enlil<br>
šar bābili<br>
mār kadašman-turgu šarri<br>
ana šūruk palîšu<br>
iqīš
</td><td>
<font size='2'>
For Ninurta,<br>
the great lord,<br>
his lord,<br>
did Kadašman-Enlil,<br>
king of Babylon,<br>
son of Kadašman-Turgu, the king,<br>
for the lengthening of his reign<br>
offer (this seal).
</font></td></tr>

</table>
<br>
</body>
</html>"""
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
