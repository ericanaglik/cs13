from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init_and_contains:
        s = Set()
        assert s.size == 0
        assert len(s) == 0


