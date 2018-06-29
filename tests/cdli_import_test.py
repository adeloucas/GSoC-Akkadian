"""
This file tests methods in cdli_import.py.
"""

import unittest
from Importer.cdli_import import CDLIImport # pylint: disable =import-error


__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests.
    """
    def test_file_pull(self):
        """
        Tests file_pull.
        """
        cdli = CDLIImport()
        output = cdli.__file_pull__('cdli_text.txt', '&P254202')
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

    def test_import_text(self):  # false positive: I have issues importing...
        """
        Tests __cdli_pull__.
        """
        cdli = CDLIImport()
        output = cdli.import_text('&P254315')
        goal = ['&P254315 = ARM 01, 114',
                '#atf: lang akk',
                '@tablet',
                '@obverse',
                '1. a-na a-ad-da-a',
                '2. qi2-bi2-ma#',
                '3. um-ma ia-as2-ma-ah-{d}iszkur',
                '4. _dumu_-ka-a-ma',
                '5. an-nu-um-ma ki-ma na-asz-pa-ar-ti',
                '6. a-[ad]-da-a 4(u) _lu2 szu-ku6 mesz_',
                '7. [u2]-sza-as,#-bi-ta#-am#-ma',
                '$ rest broken',
                '@reverse',
                '1. a-na# [s,e-er a-ad-da-a]',
                '2. at,-t,a3-ar-dam']
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
