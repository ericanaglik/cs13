from hashtable import hashtable

class Set(object):
    def __init__(self, items = None):
        self.size = 0
        self.hashtable = Hashtable()

    def contains(self, item):
        return self.hashtable.contains(item)

    def add(self, item):
        if not self.contains(item):
            self.hashtable.set(item, None)