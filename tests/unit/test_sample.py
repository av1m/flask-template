"""
Tests are typically located in the tests folder.
Tests are functions that start with test_, in Python modules that start with test_.
Tests can also be further grouped in classes that start with Test.
"""


class TestSample:
    """Just a simple test class"""

    def test_sample(self):
        """Run a sample test"""
        inc1 = lambda x: x + 1
        assert inc1(2) == 2
