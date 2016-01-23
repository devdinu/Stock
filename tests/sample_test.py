import unittest


class SampleTestCase(unittest.TestCase):
    def test_failure(self):
        assert False==True

    def test_succcess(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
