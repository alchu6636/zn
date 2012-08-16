
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
        self.t2 = Zn.TableFormat(2, self.z2.add)
        self.t3 = Zn.TableFormat(3, self.z3.add)
        self.t9 = Zn.TableFormat(9, self.z9.add)
        self.t10 = Zn.TableFormat(10, self.z10.add)
        self.t99 = Zn.TableFormat(99, self.z99.add)
        self.t100 = Zn.TableFormat(100, self.z100.add)

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
        self.assertEqual(self.t2._col_width(), 2)
        self.assertEqual(self.t3._col_width(), 2)
        self.assertEqual(self.t10._col_width(), 3)
        self.assertEqual(self.t99._col_width(), 3)
        self.assertEqual(self.t100._col_width(), 4)

    def test_cap_data(self):
        self.assertEqual(Zn.Cap(self.t2).data(), " 0/ 1".split("/"))
        self.assertEqual(Zn.Cap(self.t3).data(), " 0/ 1/ 2".split("/"))

    def test_data_data(self):
        self.assertEqual(Zn.Data(1, self.t2).data(), " 0/ 1".split("/"))
        self.assertEqual(Zn.Data(2, self.t3).data(), " 0/ 2/ 1".split("/"))
        
    def test_cap(self):
        self.assertEqual(Zn.StringTable(self.t2).cap(), " *| 0 1")
        self.assertEqual(Zn.StringTable(self.t10).cap(), "  *|  0  1  2  3  4  5  6  7  8  9")

    def test_data(self):
        self.assertEqual(Zn.Data(1, self.t2).output(), " 1/|/ 0/ 1".split("/"))
        self.assertEqual(Zn.Data(2, self.t3).output(), " 2/|/ 0/ 2/ 1".split("/"))

    def test_sep(self):
        self.assertEqual(Zn.StringTable(self.t2).sep(), "--+----")
        self.assertEqual(Zn.StringTable(self.t3).sep(), "--+------")

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
        
    def test_tableformat_op(self):
        self.assertEqual(self.t3.op(2, 1), 0)
        self.assertEqual(self.t3.op(2, 2), 1)

        
if __name__ == '__main__':
    unittest.main()
