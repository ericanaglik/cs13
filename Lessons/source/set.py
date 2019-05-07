from hashtable import hashtable

class Set(object):
    def __init__(self, items = None):
        self.size = 0
        self.hashtable = Hashtable()

    def __iter__(self):
        #allows it to be iterable
        return self._generator()

    def _generator(self):
        #helper function for iterable
        for item in self.hashtable.keys():
            yield item

    def contains(self, item):
        return self.hashtable.contains(item)

    def add(self, item):
        if not self.contains(item):
            self.hashtable.set(item, None)

    def remove(self, item):
        if self.contains(item):
            self.hashtable.delete(item, None)
    
    def union(self, other_set):
        new_set = Set()
        for item in other_set:
            new_set.add(item)
        for item in self:
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        new_set = Set()
        for item in other_set:
            if self.contains(item):
                new_set.add(item)
        return new_set

    def difference(self, other_set): 
        new_set = Set()
        for item in self:
            if not other_set.contains(item):
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        for item in self:
            if not other_set.contains(item):
                return False
        return True
