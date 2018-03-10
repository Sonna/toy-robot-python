"""
== Usage example:

    with OutputBuffer() as bf:
        print('hello world')
    assert bf.out == 'hello world\n'

== Source:
- [unit testing \- How to assert output with nosetest/unittest in python? \-
  Stack Overflow]
  (https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python/46879182#46879182)
"""
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# from io import StringIO
# from io import BytesIO as StringIO
import sys


class OutputBuffer(object):
    def __init__(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    def __enter__(self):
        self.original_stdout, self.original_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = self.stdout, self.stderr
        return self

    def __exit__(self, exception_type, exception, traceback):
        sys.stdout, sys.stderr = self.original_stdout, self.original_stderr

    @property
    def out(self):
        return self.stdout.getvalue()

    @property
    def err(self):
        return self.stderr.getvalue()


class InputBuffer(object):
    def __init__(self, input_string=''):
        self.stdin = StringIO(input_string)
        self.stderr = StringIO()

    def __enter__(self):
        self.original_stdin, self.original_stderr = sys.stdin, sys.stderr
        sys.stdin, sys.stderr = self.stdin, self.stderr
        return self

    def __exit__(self, exception_type, exception, traceback):
        sys.stdin, sys.stderr = self.original_stdin, self.original_stderr

    @property
    def in_value(self):
        return self.stdin.getvalue()

    @property
    def err(self):
        return self.stderr.getvalue()
