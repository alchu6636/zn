
from zn import Zn
import unittest

class TestZn(unittest.TestCase):

    def setUp(self):
        self.z2 = Zn(2)
        self.z3 = Zn(3)
        self.z9 = Zn(9)
        self.z10 = Zn(10)
        self.z99 = Zn(99)
        self.z100 = Zn(100)

    def stub_test_str(self):
        result = self.z2.__str__()
        self.assertEqual(result, """Z2
 +| 0 1  *| 0 1
--+---- --+----
 0| 0 1  0| 0 0
 1| 1 0  1| 0 1""")

    def test_init_error(self):
        Zn(2)
        self.assertRaises(ValueError, Zn, 1)
        
    def test_col_width(self):
        self.assertEqual(Zn.TableFormat(2)._col_width(), 2)
        self.assertEqual(Zn.TableFormat(9)._col_width(), 2)
        self.assertEqual(Zn.TableFormat(10)._col_width(), 3)
        self.assertEqual(Zn.TableFormat(99)._col_width(), 3)
        self.assertEqual(Zn.TableFormat(100)._col_width(), 4)

    def test_cap_data(self):
        self.assertEqual(Zn.Cap(Zn.TableFormat(2)).data(), " 0/ 1".split("/"))
        self.assertEqual(Zn.Cap(Zn.TableFormat(3)).data(), " 0/ 1/ 2".split("/"))

    def test_data_data(self):
        self.assertEqual(Zn.Data(1, Zn.TableFormat(2)).data(), " 0/ 1".split("/"))
        self.assertEqual(Zn.Data(2, Zn.TableFormat(3)).data(), " 0/ 2/ 1".split("/"))

    def test_cap(self):
        self.assertEqual(Zn.StringTable(2).cap(), " *| 0 1")
        self.assertEqual(Zn.StringTable(10).cap(), "  *|  0  1  2  3  4  5  6  7  8  9")

    def test_data(self):
        self.assertEqual(Zn.Data(1, Zn.TableFormat(2)).output(), " 1/|/ 0/ 1".split("/"))
        self.assertEqual(Zn.Data(2, Zn.TableFormat(3)).output(), " 2/|/ 0/ 2/ 1".split("/"))

    def test_sep(self):
        self.assertEqual(Zn.StringTable(2).sep(), "--+----")
        self.assertEqual(Zn.StringTable(3).sep(), "--+------")

    def test_str_multi2(self):
        self.assertEqual(self.z2.str_multi_table(), \
""" *| 0 1
--+----
 0| 0 0
 1| 0 1""".split("\n"))
        
    def test_mul(self):
        self.assertEqual(self.z3.mul(2, 1), 2)
        self.assertEqual(self.z3.mul(2, 2), 1)
        self.assertEqual(self.z3.mul(2, 3), 0)

    def test_add(self):
        self.assertEqual(self.z3.add(2, 1), 0)
        self.assertEqual(self.z3.add(2, 2), 1)
if __name__ == '__main__':
    unittest.main()
