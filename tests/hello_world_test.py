import toy_robot
from .test_helpers import OutputBuffer

import unittest
import sys
# from io import BytesIO as StringIO
# from io import BytesIO,StringIO
# from io import StringIO

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class HelloWorldTestSuite(unittest.TestCase):
    def test_stdout(self):
        with OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, 'hello world\n')
        # self.assertEqual(bf.out, 'hello world\n'.encode())

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_foo(self):
        print('hello world')
        self.assertEqual(sys.stdout.getvalue(), 'hello world\n')

    def test_absolute_truth_and_meaning(self):
        assert True


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
