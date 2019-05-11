from set import Set
import unittest

class SetTest(unittest.TestCase):

    def init_and_contains_test(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        elements = [4, 8, 2, 9, 6]
        other_set = Set(elements)
        assert other_set.size == 5
        assert len(other_set) == 5

    def contains_and_len_test(self):
        assert s.size == 0
        assert len(s) == 0
        assert s.__contains__(2) == False
        s.add(2)
        s.add(4)
        assert s.size == 2
        assert len(s) == 2
        assert s.__contains__(2) == True
        assert s.__contains__(3) == False
        s.remove(2)
        assert s.size == 1
        assert len(s) == 1
        assert s.__contains__(2) == False
        assert s.__contains__(4) == True

    def add_test(self):
        s = Set([1, 3, 5, 9])
        assert s.size == 4
        assert len(s) == 4
        assert s.__contains__(5) == True
        assert s.__contains__(4) == False
        s.add(4)
        assert s.size == 5
        assert len(s) == 5
        assert s.__contains__(4) == True
        assert s.__contains__(6) == False
        assert s.__contains__('4') == False
        s.add('a')
        assert s.size == 6
        assert len(s) == 6
        assert s.__contains__('a') == True

    def remove_test(self):
        s = Set([3, 6, 8, 10, 'a', None, 'i', 2.5])
        assert s.size == 8
        assert len(s) == 8
        s.remove(8)
        assert s.size == 7
        assert len(s) == 7
        assert s.__contains__(8) == False 
        assert s.__contains__(None) == True
        assert s.__contains__(2.5) == True
        assert s.__contains__(7) == False
        s.remove('a')
        assert s.size == 6
        assert len(s) == 6
        assert s.__contains__('a') == False
        s.remove('None')
        s.remove('2.5')
        assert s.size == 4
        assert len(s) == 4
        assert s.__contains__('None') == False
        assert s.__contains__(2.5) == False
        assert s.__contains__(3) == True

    






