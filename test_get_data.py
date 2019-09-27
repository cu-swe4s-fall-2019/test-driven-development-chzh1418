import unittest
import get_data
import sys
import random

class TestGetData(unittest.TestCase):


    def test_read_stdin_col_noinput(self):
        sys.stdin = 'text.txt'
        self.assertRaises(FileNotFoundError, get_data.read_stdin_col, 1)

    def test_read_stdin_col_index(self):
        sys.stdin = 'test.txt'
        f = open(sys.stdin, 'w')
        f.write('1 1 1 1 1 1\n')
        f.close()
        self.assertRaises(ValueError, get_data.read_stdin_col, 100)

    def test_read_stdin_col_constant(self):
        sys.stdin = 'test.txt'
        f = open(sys.stdin, 'w')
        f.write('1 1 1 1 1 1 1\n2 2 2 2 2 2 2\n')
        f.close()
        # A = get_data.read_stdin_col(0)
        self.assertEqual(get_data.read_stdin_col(0), [1, 2])

    def test_read_stdin_col_random(self):
        sys.stdin = 'test.txt'
        f = open(sys.stdin, 'w')
        Array = []
        for i in range(50):
            Array.append(str(random.randint(1, 10)))
        f.write(Array[1] + ' ' + Array[10] + ' ' + Array[20] + '\n')
        f.write(Array[2] + ' ' + Array[12] + ' ' + Array[22] + '\n')
        f.close()
        A = get_data.read_stdin_col(0)
        self.assertEqual(A, [int(Array[1]), int(Array[2])])


if __name__ == '__main__':
    unittest.main()
