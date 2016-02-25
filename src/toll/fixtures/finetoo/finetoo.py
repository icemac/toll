import unittest


class Test_FineToo(unittest.TestCase):
    """It does not fail, too."""

    def test_fine__1(self):
        self.assertTrue(True)


def test_suite():
    """Create test suite for `python setup.py test`."""
    return unittest.TestSuite([unittest.makeSuite(Test_FineToo)])
