import unittest
import get_data
import sys


class TestGetData(unittest.TestCase):

    def test_read_stdin_col_noinput(self):
        sys.stdin = None

        A = get_data.read_stdin_col()
        self.assertEqual(A, None)


if __name__ == '__main__':
    unittest.main()
