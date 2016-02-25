import unittest


class Test_Bad(unittest.TestCase):
    """It fails."""

    def test_fine__1(self):
        self.assertTrue(False)


def test_suite():
    """Create test suite for `python setup.py test`."""
    return unittest.TestSuite([unittest.makeSuite(Test_Bad)])
