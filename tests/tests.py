__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from main.ATFConverter import ATFConverter

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test1(self):
        ATF = ATFConverter()
        text = [(r's,'), (r'S,'), (r't,'), (r'T,'), (r'sz'), (r'SZ'), (r's,a'), (r'as,-bat')]
        target = str(['ṣ', 'Ṣ', 'ṭ', 'Ṭ', 'š', 'Š', 'ṣa', 'aṣ-bat'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class test2(unittest.TestCase):  # pylint: disable=R0904

    def test2(self):
        ATF = ATFConverter()
        text = ['szi3', 'lil2', 'bi2', 't,e4', 'u3', 'aga2', 'ARAD2', 'geme2', 'sig17', 'u3 _ku3-sig17', 'ra-pi2-qi2']
        target = str(['šì', 'líl', 'bí', 'ṭe₄', 'ù', 'ága', 'áRAD', 'géme', 'sig₁₇', 'ù _kù-sig₁₇', 'ra-pí-qí'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class test3(unittest.TestCase):  # pylint: disable=R0904

    def test3(self):
        ATF = ATFConverter()
        text = ['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{munus}', '{še}', 
                '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'(u)', r'(diš)', r'(disz)', r'{i7}', r'{I7}']
        target = str(['ᵈ', 'ⁱʳⁱ', 'ˡᶸ²', 'ˡᶸ²', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ',
                      'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)','ⁱ⁷', 'ⁱ⁷'])

        output = ATF.convert(text)

        self.assertEqual(output, target)

class test4(unittest.TestCase):  # pylint: disable=R0904

    def test4(self):
        ATF = ATFConverter()
        text = [r'_lugal_',  r'_hé-gál_',  r'_ušumgal lugal_-rí',  r'_še_ ù _kù-babbar_',   r'lu _gu₄_ lu _udu_',  
                r'lu _gu₄_ lu _udu_ lu _anše_ lu _šáh_',  r'_|maš.en.gag|_',  r'_iti 6(𒁹)-kam_',  
                r'lu _árad |maš.en.gag|_', r'_a-šà_-šu ù _ᵍᵉˢᶻkiri₆_-šu', r'_aga#-ús_',  r'_aga-ús#_',  
                r'_a-šà_-šu _ᵍᵉˢᶻkiri₆_-šu# ù _é_-sú#', r'_áb# gu₄!(bi) hi-a_', r'_še_ ša i-na _a-šà_', 
                r'_[a]-šà_-šu', r'_a-šà u₈ udu hi-a_', r'_a-rá_ 3(𒁹)-šu a-na _dam-gàr_', 
                r'ša _dumu-meš_ ul-du-šum ù lu _lukur_ ša _dumu-meš_', r'_u₈ [udu hi-a_]', 
                r'ù lu _ur-mah_ id-du-uk _sipa_ ma-hi! _dingir_', r'_še kù]-babbar_', 
                r'_u₄ 2(𒁹)-kam# [3(𒁹)-kam]_ i-na _é-hi-a_-šu-nu', r'_iti#_', 
                r'_[ᵍᵉˢᶻ]má# hi-a gal_ la# im#-ma#-ad-du _1(𒌋)-kam_', r'_ᵍᵉˢᶻgešimmar ᵍᵉˢᶻšu-úr-mìn_ ù _ᵍᵉˢᶻaz_', 
                r'_a#-šà#-hi-a_', r'_2(𒁹) anše gú_ ù _1(𒁹) tur [..._]', r'_iti_ ti-ri-im _u₄ 1(𒌋) 5(𒁹)-kam ba-zal_-[ma]', 
                r'_1(𒌋)# gú# kù-sig₁₇_', r'a-na _5(𒁹) ˡᶸ²árad-meš_ i-yu-ti-in _1(𒁹)-àm_ ᵏᶸˢᶻna-da-tim# _2(𒁹)-àm_ ᵏᶸˢᶻme-še-[ni]', 
                r'_ᵈ#iškur#_', r'_gú# [kù]-babbar_ te-er-ha-at _dumu-munus_', r'_inim?-ᵈiškur#?_', 
                r'[_árad_] [a]-bi-im _u₄ 6(𒁹)-kam zal_-[ma]']
        target = str([r'_LUGAL_', r'_HÉ-GÁL_', r'_UŠUMGAL LUGAL_-rí', r'_ŠE_ ù _KÙ-BABBAR_', r'lu _GU₄_ lu _UDU_', 
                r'lu _GU₄_ lu _UDU_ lu _ANŠE_ lu _ŠÁH_',  r'_|MAŠ.EN.GAG|_', r'_ITI 6(𒁹)-KAM_', 
                r'lu _ÁRAD |MAŠ.EN.GAG|_', r'_A-ŠÀ_-šu ù _ᵍᵉˢᶻKIRI₆_-šu', r'_AGA#-ÚS_', r'_AGA-ÚS#_', 
                r'_A-ŠÀ_-šu _ᵍᵉˢᶻKIRI₆_-šu# ù _É_-sú#', r'_ÁB# GU₄!(BI) HI-A_',  r'_ŠE_ ša i-na _A-ŠÀ_', 
                r'_[A]-ŠÀ_-šu',  r'_A-ŠÀ U₈ UDU HI-A_',  r'_A-RÁ_ 3(𒁹)-šu a-na _DAM-GÀR_',  
                r'ša _DUMU-MEŠ_ ul-du-šum ù lu _LUKUR_ ša _DUMU-MEŠ_',  r'_U₈ [UDU HI-A_]',  
                r'ù lu _UR-MAH_ id-du-uk _SIPA_ ma-hi! _DINGIR_',  r'_ŠE KÙ]-BABBAR_', 
                r'_U₄ 2(𒁹)-KAM# [3(𒁹)-KAM]_ i-na _É-HI-A_-šu-nu',  r'_ITI#_', 
                r'_[ᵍᵉˢᶻ]MÁ# HI-A GAL_ la# im#-ma#-ad-du _1(𒌋)-KAM_', r'_ᵍᵉˢᶻGEŠIMMAR ᵍᵉˢᶻŠU-ÚR-MÌN_ ù _ᵍᵉˢᶻAZ_', 
                r'_A#-ŠÀ#-HI-A_', r'_2(𒁹) ANŠE GÚ_ ù _1(𒁹) TUR [..._]', r'_ITI_ ti-ri-im _U₄ 1(𒌋) 5(𒁹)-KAM BA-ZAL_-[ma]',  
                r'_1(𒌋)# GÚ# KÙ-SIG₁₇_', r'a-na _5(𒁹) ˡᶸ²ÁRAD-MEŠ_ i-yu-ti-in _1(𒁹)-ÀM_ ᵏᶸˢᶻna-da-tim# _2(𒁹)-ÀM_ ᵏᶸˢᶻme-še-[ni]', 
                r'_ᵈ#IŠKUR#_', r'_GÚ# [KÙ]-BABBAR_ te-er-ha-at _DUMU-MUNUS_', r'_INIM?-ᵈIŠKUR#?_', 
                r'[_ÁRAD_] [a]-bi-im _U₄ 6(𒁹)-KAM ZAL_-[ma]'])
        output = ATF.convert(text)
        self.maxDiff = None
        self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()
