__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

import unittest
from ATFConverter.ATFConverter import ATFConverter
from ATFConverter.Tokenizer import Tokenizer

class test1(unittest.TestCase):  # pylint: disable=R0904

    def test_convert_tittles(self):
        ATF = ATFConverter()
        signs = str([(r'as,'), (r'S,ATU'), (r'tet,'), (r'T,et'), (r'sza'), (r'ASZ')])
        target = str(['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ'])
        output = ATF.convert_consonant(signs)
        self.assertEqual(output, target)

    def test_get_number_from_sign(self):
        ATF = ATFConverter()
        signs = ["a", "a1", "be2", "bad3", "buru14"]
        target = [0, 1, 2, 3, 14]

        output = [ATF.get_number_from_sign(s)[1] for s in signs]

        self.assertEqual(output, target)

    def test_single_sign(self):
        ATF = ATFConverter(two_three=True)
        signs = ["a", "a1", "a2", "a3", "be2", "be3", "bad2", "bad3"]
        target = ["a", "a", "a₂", "a₃", "be₂", "be₃", "bad₂", "bad₃"]

        output = ATF.process(signs)

        self.assertEqual(output, target)

    def test_accents(self):
        ATF = ATFConverter(two_three=False)
        signs = ["a", "a2", "a3", "be2", "bad3", "buru14"]
        target = ["a", "á", "à", "bé", "bàd", "buru₁₄"]

        output = ATF.process(signs)

        self.assertEqual(output, target)

    def test_unknown_token(self):
        ATF = ATFConverter(two_three=True)
        signs = ["a2", "☉", "be3"]
        target = ["a₂", "☉", "be₃"]

        output = ATF.process(signs)

        self.assertEqual(output, target)

    def test_determinatives(self):
        ATF = ATFConverter()
        text = str(['{d}', '{iri}', '{lú}', '{lu2}', '{diš}', '{disz}', '{geš}', '{gesz}', '{munus}', '{še}', 
                '{sze}', '{uzu}', '{kuš}', '{kusz}', '{ki}', r'(u)', r'(diš)', r'(disz)', r'{i7}', r'{I7}'])
        target = str(['ᵈ', 'ⁱʳⁱ', 'ˡᶸ²', 'ˡᶸ²', '𒁹', '𒁹', 'ᵍᵉˢᶻ', 'ᵍᵉˢᶻ', 'ᵐᶸⁿᶸˢ', 'ˢᶻᵉ',
                      'ˢᶻᵉ', 'ᶸᶻᶸ', 'ᵏᶸˢᶻ', 'ᵏᶸˢᶻ', 'ᵏⁱ', '(𒌋)', '(𒁹)', '(𒁹)','ⁱ⁷', 'ⁱ⁷'])

        output = ATF.determination(text)
        self.maxDiff = None
        self.assertEqual(output, target)

 #   def test_sumerian(self):
 #       ATF = ATFConverter()
 #       sign = ['_lugal_',  '_hé-gál_',  '_ušumgal lugal_-rí',  '_še_ ù _kù-babbar_', 'lu _gu₄_ lu _udu_',  
 #               '_|maš.en.gag|_',  '_iti 6(𒁹)-kam_', #r'lu _gu₄_ lu _udu_ lu _anše_ lu _šáh_',
 #               'lu _árad |maš.en.gag|_', '_a-šà_-šu ù _ᵍᵉˢᶻkiri₆_-šu', '_aga#-ús_',  '_aga-ús#_',  
 #               '_a-šà_-šu _ᵍᵉˢᶻkiri₆_-šu# ù _é_-sú#', '_áb# gu₄!(bi) hi-a_', '_še_ ša i-na _a-šà_', 
 #               '_[a]-šà_-šu', '_a-šà u₈ udu hi-a_', '_a-rá_ 3(𒁹)-šu a-na _dam-gàr_', 
 #               'ša _dumu-meš_ ul-du-šum ù lu _lukur_ ša _dumu-meš_', '_u₈ [udu hi-a_]', 
 #               'ù lu _ur-mah_ id-du-uk _sipa_ ma-hi! _dingir_', '_še kù]-babbar_', 
 #               '_u₄ 2(𒁹)-kam# [3(𒁹)-kam]_ i-na _é-hi-a_-šu-nu', '_iti#_', 
 #               '_[ᵍᵉˢᶻ]má# hi-a gal_ la# im#-ma#-ad-du _1(𒌋)-kam_', '_ᵍᵉˢᶻgešimmar ᵍᵉˢᶻšu-úr-mìn_ ù _ᵍᵉˢᶻaz_', 
 #               '_a#-šà#-hi-a_', '_2(𒁹) anše gú_ ù _1(𒁹) tur [..._]', '_iti_ ti-ri-im _u₄ 1(𒌋) 5(𒁹)-kam ba-zal_-[ma]', 
 #               '_1(𒌋)# gú# kù-sig₁₇_', 'a-na _5(𒁹) ˡᶸ²árad-meš_ i-yu-ti-in _1(𒁹)-àm_ ᵏᶸˢᶻna-da-tim# _2(𒁹)-àm_ ᵏᶸˢᶻme-še-[ni]', 
 #               '_ᵈ#iškur#_', '_gú# [kù]-babbar_ te-er-ha-at _dumu-munus_', '_inim?-ᵈiškur#?_', 
 #               '[_árad_] [a]-bi-im _u₄ 6(𒁹)-kam zal_-[ma]']
 #       target = str(['_LUGAL_', '_HÉ-GÁL_', '_UŠUMGAL LUGAL_-rí', '_ŠE_ ù _KÙ-BABBAR_', 'lu _GU₄_ lu _UDU_', 
 #               '_|MAŠ.EN.GAG|_', '_ITI 6(𒁹)-KAM_', #r'lu _GU₄_ lu _UDU_ lu _ANŠE_ lu _ŠÁH_',
 #               'lu _ÁRAD |MAŠ.EN.GAG|_', '_A-ŠÀ_-šu ù _ᵍᵉˢᶻKIRI₆_-šu', '_AGA#-ÚS_', '_AGA-ÚS#_', 
 #               '_A-ŠÀ_-šu _ᵍᵉˢᶻKIRI₆_-šu# ù _É_-sú#', '_ÁB# GU₄!(BI) HI-A_',  '_ŠE_ ša i-na _A-ŠÀ_', 
 #               '_[A]-ŠÀ_-šu',  '_A-ŠÀ U₈ UDU HI-A_',  '_A-RÁ_ 3(𒁹)-šu a-na _DAM-GÀR_',  
 #               'ša _DUMU-MEŠ_ ul-du-šum ù lu _LUKUR_ ša _DUMU-MEŠ_',  '_U₈ [UDU HI-A_]',  
 #               'ù lu _UR-MAH_ id-du-uk _SIPA_ ma-hi! _DINGIR_',  '_ŠE KÙ]-BABBAR_', 
 #               '_U₄ 2(𒁹)-KAM# [3(𒁹)-KAM]_ i-na _É-HI-A_-šu-nu',  '_ITI#_', 
 #               '_[ᵍᵉˢᶻ]MÁ# HI-A GAL_ la# im#-ma#-ad-du _1(𒌋)-KAM_', '_ᵍᵉˢᶻGEŠIMMAR ᵍᵉˢᶻŠU-ÚR-MÌN_ ù _ᵍᵉˢᶻAZ_', 
 #               '_A#-ŠÀ#-HI-A_', '_2(𒁹) ANŠE GÚ_ ù _1(𒁹) TUR [..._]', '_ITI_ ti-ri-im _U₄ 1(𒌋) 5(𒁹)-KAM BA-ZAL_-[ma]',  
 #               '_1(𒌋)# GÚ# KÙ-SIG₁₇_', 'a-na _5(𒁹) ˡᶸ²ÁRAD-MEŠ_ i-yu-ti-in _1(𒁹)-ÀM_ ᵏᶸˢᶻna-da-tim# _2(𒁹)-ÀM_ ᵏᶸˢᶻme-še-[ni]', 
 #               '_ᵈ#IŠKUR#_', '_GÚ# [KÙ]-BABBAR_ te-er-ha-at _DUMU-MUNUS_', '_INIM?-ᵈIŠKUR#?_', 
 #               '[_ÁRAD_] [a]-bi-im _U₄ 6(𒁹)-KAM ZAL_-[ma]'])
 #       output = ATF.sumerianization(sign)
 #       self.maxDiff = None
 #       self.assertEqual(output, target)

if __name__ == '__main__':
    unittest.main()