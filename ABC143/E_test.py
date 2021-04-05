import sys
from io import StringIO
import unittest
from ABC143 import E

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        E.e()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 2 5
1 2 3
2 3 3
2
3 2
1 3"""
        output = """0
1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 0 1
1
2 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 4 4
1 2 2
2 3 2
3 4 3
4 5 2
20
2 1
3 1
4 1
5 1
1 2
3 2
4 2
5 2
1 3
2 3
4 3
5 3
1 4
2 4
3 4
5 4
1 5
2 5
3 5
4 5"""
        output = """0
0
1
2
0
0
1
2
0
0
0
1
1
1
0
0
2
2
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()