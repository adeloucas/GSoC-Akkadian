
import unittest

from pyatf.pyatf import ATFConverter


class Test1(unittest.TestCase):

    def test_single_char(self):
        con = ATFConverter()
        text = ["a2", "a3"]
        target = ["a₂", "a₃"]

        output = con.process(text)

        self.assertEqual(output, target)

    def test_double_char(self):
        con = ATFConverter()
        text = ["ab2", "be3"]
        target = ["ab₂", "be₃"]

        output = con.process(text)

        self.assertEqual(output, target)

    def test_unknown_token(self):
        con = ATFConverter()
        text = ["a2", "☉", "be3"]
        target = ["a₂", "ERROR: (☉)", "be₃"]

        output = con.process(text)

        self.assertEqual(output, target)

if __name__ == "__main__":
    unittest.main()