from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init_and_contains(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        elements = [4, 8, 2, 9, 6]
        other_set = Set(elements)
        assert other_set.size == 5
        assert len(other_set) == 5



