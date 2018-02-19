import unittest

# https://stackoverflow.com/questions/17353213/init-for-unittest-testcase

class TestFileReader(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFileReader, self).__init__(*args, **kwargs)
        self.path = 'i1data.txt'

    def setUp(self):
        self.input_file = open(self.path,'r')
        pass

    def tearDown(self):
        self.input_file.close()
        pass

    def test_read(self):
        lines = self.input_file.readlines()

        self.assertEqual(len(lines),2)
        self.assertEqual(lines[0].split()[0], 'Bradman')




if __name__ == "__main__":
    unittest.main()