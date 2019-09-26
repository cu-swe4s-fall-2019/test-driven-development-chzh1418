import unittest
import data_viz
import sys


class TestDataViz(unittest.TestCase):
    # Test the data_viz module
    def test_data_viz_no_input(self):
        A = []

        with self.assertRaises(NameError) as ex:
            data_viz.boxplot(A, None)
        self.assertEqual(str(ex.exception), 'Out_file_name required')

    def test_dat_viz_exist(self):
        A = []
        file_name = 'file1.png'
        file = open(file_name, 'w')
        file.close()

        with self.assertRaises(SystemExit) as ex:
            data_viz.boxplot(A, file_name)
        self.assertEqual(str(ex.exception), 'File already exits')


if __name__ == '__main__':
    unittest.main()
