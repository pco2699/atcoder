import sys
from io import StringIO
import unittest
from ABC137 import E

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
        input = """3 3 10
1 2 20
2 3 30
1 3 45"""
        output = """35"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 2 10
1 2 100
2 2 100"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 5 10
1 2 1
1 4 1
3 4 1
2 2 100
3 3 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()