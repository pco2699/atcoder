import sys
from io import StringIO
import unittest
import A

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        A.a()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test1(self):
        input = """2"""
        output = """8"""
        self.assertIO(input, output)
    def test2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()