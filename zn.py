import math

class Zn:
    def __init__(self, char):
        if char < 2:
            raise ValueError
        self._char = char

    def mul(self, x, y):
        return x * y % self._char
    
    def add(self, x, y):
        return (x + y) % self._char
    
    class TableFormat:
        def __init__(self, char, op, elements, symbol):
            self._char = char
            self._op = op
            self.elements = elements
            self.symbol = symbol
            
        def col_width(self):
            return int(math.log(self._char -1, 10)) + 2

        def op(self, x, y):
            return self._op(x, y)
        
    class TableParts:
        def align(self, value):
            form = "%" + str(self._format.col_width()) + "s"
            return form % value
            
        def sep(self):
            return "|"
        
        def data(self):
            return map(self.cell, self._format.elements)

        def output(self):    
            return [ self.cap(), self.sep()] + self.data()
            
    class Cap(TableParts):
        def __init__(self, tf):
            self._format = tf
            
        def cap(self):
            return self.align(self._format.symbol)

        def cell(self, col):
            return self.align(col)
        
    class Sep(TableParts):
        def __init__(self, tf):
            self._format = tf
            
        def _horizen(self):
            return "-" * self._format.col_width()

        def cap(self):
            return self._horizen()
        
        def sep(self):
            return "+"

        def cell(self, stub):
            return self._horizen()
            
    class Data(TableParts):
        def __init__(self, row, tf):
            self._row = row
            self._format = tf
            
        def cap(self):
            return self.align(self._row)
        
        def cell(self, col):
            return self.align(self._format.op(self._row, col))
           
    class StringTable(TableParts):
        def __init__(self, tf):
            self._format = tf
        
        def cap(self):
            ar = Zn.Cap(self._format).output()
            return "".join(ar)

        def sep(self):
            ar = Zn.Sep(self._format).output()
            return "".join(ar)

        def cell(self, row):
            ar = Zn.Data(row, self._format).output()
            return "".join(ar)
            
    def str_multi_table(self):
        return Zn.StringTable(Zn.TableFormat(self._char, self.mul, range(1, self._char), "*")).output()

    def str_add_table(self):
        return Zn.StringTable(Zn.TableFormat(self._char, self.add, range(0, self._char), "+")).output()

    def name(self):
        return "Z" + str(self._char)
    
    def __str__(self):
        add = self.str_add_table()
        mul = self.str_multi_table()+[""]
        spc = [" "] * len(add)
        ar = zip(add, spc, mul)
        ar2 = map("".join, ar)
        return "\n".join([self.name()]+ar2)
        
        
if __name__ == '__main__':
    print "\n".join(Zn(5).str_multi_table())
    print "\n".join(Zn(11).str_multi_table())
    print "\n".join(Zn(17).str_multi_table())
