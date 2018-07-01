"""
This file tests methods in file_import.py.
"""

import os
import unittest
from Importer.file_importer import FileImport  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'


class Test1(unittest.TestCase):  # pylint: disable=R0904
    """
    Tests file_importer functions.
    """
    def test_read_file(self):
        """
        Tests read_file.
        """
        text = os.path.join('..', 'texts', 'Akkadian.txt')
        cdli = FileImport(text)
        output = cdli.read_file()
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

    def test_import_text(self):
        """
        Tests import_text.
        """
        text = os.path.join('..', 'texts', 'cdli_text.txt')
        cdli = FileImport(text)
        output = cdli.import_text('&P254202')
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

    def test_discern_texts(self):
        """
        Tests __discern_texts__.
        """
        text = os.path.join('..', 'texts', 'cdli_text.txt')
        cdli = FileImport(text)
        output = cdli.__discern_texts__()
        goal = ["&P254202 = ARM 01, 001", "&P254203 = ARM 01, 002"]
        self.assertEqual(output, goal)

    def test_split_texts(self):
        """
        Tests __split_texts__.
        """
        text = os.path.join('..', 'texts', 'cdli_text.txt')
        cdli = FileImport(text)
        output = cdli.__split_texts__()
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

    def test_text_call_names(self):
        """
        Tests __text_call_names__.
        """
        text = os.path.join('..', 'texts', 'ARM1Akkadian.txt')
        cdli = FileImport(text)
        output = cdli.__text_call_names__()
        goal = ['&P254202', 'ARM 01, 001', '&P254203', 'ARM 01, 002',
                '&P254204', 'ARM 01, 003', '&P254205', 'ARM 01, 004',
                '&P254206', 'ARM 01, 005', '&P254207', 'ARM 01, 006',
                '&P254208', 'ARM 01, 007', '&P254209', 'ARM 01, 008',
                '&P254210', 'ARM 01, 009', '&P254211', 'ARM 01, 010',
                '&P254212', 'ARM 01, 011', '&P254213', 'ARM 01, 012',
                '&P254214', 'ARM 01, 013', '&P254215', 'ARM 01, 014',
                '&P254216', 'ARM 01, 015', '&P254217', 'ARM 01, 016',
                '&P254218', 'ARM 01, 017', '&P254219', 'ARM 01, 018',
                '&P254220', 'ARM 01, 019', '&P254221', 'ARM 01, 020',
                '&P254222', 'ARM 01, 021', '&P254223', 'ARM 01, 022',
                '&P254224', 'ARM 01, 023', '&P254225', 'ARM 01, 024',
                '&P254226', 'ARM 01, 025', '&P254227', 'ARM 01, 026',
                '&P254228', 'ARM 01, 027', '&P254229', 'ARM 01, 028',
                '&P254230', 'ARM 01, 029', '&P254231', 'ARM 01, 030',
                '&P254232', 'ARM 01, 031', '&P254233', 'ARM 01, 032',
                '&P254234', 'ARM 01, 033', '&P254235', 'ARM 01, 034',
                '&P254236', 'ARM 01, 035', '&P254237', 'ARM 01, 036',
                '&P254238', 'ARM 01, 037', '&P254239', 'ARM 01, 038',
                '&P254240', 'ARM 01, 039', '&P254241', 'ARM 01, 040',
                '&P254242', 'ARM 01, 041', '&P254243', 'ARM 01, 042',
                '&P254244', 'ARM 01, 043', '&P254245', 'ARM 01, 044',
                '&P254246', 'ARM 01, 045', '&P254247', 'ARM 01, 046',
                '&P254248', 'ARM 01, 047', '&P254249', 'ARM 01, 048',
                '&P254250', 'ARM 01, 049', '&P254251', 'ARM 01, 050',
                '&P254252', 'ARM 01, 051', '&P254253', 'ARM 01, 052',
                '&P254254', 'ARM 01, 053', '&P254255', 'ARM 01, 054',
                '&P254256', 'ARM 01, 055', '&P254257', 'ARM 01, 056',
                '&P254258', 'ARM 01, 057', '&P254259', 'ARM 01, 058',
                '&P254260', 'ARM 01, 059', '&P254261', 'ARM 01, 060',
                '&P254262', 'ARM 01, 061', '&P254263', 'ARM 01, 062',
                '&P254264', 'ARM 01, 063', '&P254265', 'ARM 01, 064',
                '&P254266', 'ARM 01, 065', '&P254267', 'ARM 01, 066',
                '&P254268', 'ARM 01, 067', '&P254269', 'ARM 01, 068',
                '&P254270', 'ARM 01, 069', '&P254271', 'ARM 01, 070',
                '&P254272', 'ARM 01, 071', '&P254273', 'ARM 01, 072',
                '&P254274', 'ARM 01, 073', '&P254275', 'ARM 01, 074',
                '&P254276', 'ARM 01, 075', '&P254277', 'ARM 01, 076',
                '&P254278', 'ARM 01, 077', '&P254279', 'ARM 01, 078',
                '&P254280', 'ARM 01, 079', '&P254281', 'ARM 01, 080',
                '&P254282', 'ARM 01, 081', '&P254283', 'ARM 01, 082',
                '&P254284', 'ARM 01, 083', '&P254285', 'ARM 01, 084',
                '&P254286', 'ARM 01, 085', '&P254287', 'ARM 01, 086',
                '&P254288', 'ARM 01, 087', '&P254289', 'ARM 01, 088',
                '&P254290', 'ARM 01, 089', '&P254291', 'ARM 01, 090',
                '&P254292', 'ARM 01, 091', '&P254293', 'ARM 01, 092',
                '&P254294', 'ARM 01, 093', '&P254295', 'ARM 01, 094',
                '&P254296', 'ARM 01, 095', '&P254297', 'ARM 01, 096',
                '&P254298', 'ARM 01, 097', '&P254299', 'ARM 01, 098',
                '&P254300', 'ARM 01, 099', '&P254301', 'ARM 01, 100',
                '&P254302', 'ARM 01, 101', '&P254303', 'ARM 01, 102',
                '&P254304', 'ARM 01, 103', '&P254305', 'ARM 01, 104',
                '&P254306', 'ARM 01, 105', '&P254307', 'ARM 01, 106',
                '&P254308', 'ARM 01, 107', '&P254309', 'ARM 01, 108',
                '&P254310', 'ARM 01, 109', '&P254311', 'ARM 01, 110',
                '&P254312', 'ARM 01, 111', '&P254313', 'ARM 01, 112',
                '&P254314', 'ARM 01, 113', '&P254315', 'ARM 01, 114',
                'P254316', 'ARM 01, 115', '&P254317', 'ARM 01, 116',
                '&P254318', 'ARM 01, 117', '&P254319', 'ARM 01, 118',
                '&P254320', 'ARM 01, 119', '&P254321', 'ARM 01, 120',
                '&P254322', 'ARM 01, 121', '&P254323', 'ARM 01, 122',
                '&P254324', 'ARM 01, 123', '&P254325', 'ARM 01, 124',
                '&P254326', 'ARM 01, 125', '&P254327', 'ARM 01, 126',
                '&P254328', 'ARM 01, 127', '&P254329', 'ARM 01, 128',
                '&P254330', 'ARM 01, 129', '&P254331', 'ARM 01, 130',
                '&P254332', 'ARM 01, 131', '&P254333', 'ARM 01, 132',
                '&P254334', 'ARM 01, 133', '&P254335', 'ARM 01, 134',
                '&P254336', 'ARM 01, 135', '&P254337', 'ARM 01, 136',
                '&P254338', 'ARM 01, 137', '&P254339', 'ARM 01, 138',
                '&P254340', 'ARM 01, 139']
        self.assertEqual(output, goal)


if __name__ == '__main__':
    unittest.main()
