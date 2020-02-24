class Set:
    """    
    Python List Implementation for Set ADT
    """
    def __init__(self):
        """
        Creates an empty list to represent the Set
        """
        self._items = []
        
    def __len__(self):
        """
        Returns the number of items in the set
        This allows you to find the number of items in the Set
        with len(setA)
        """
        return len(self._items)

    def __contains__(self, item):
        """
        Returns True if the set contains the passed in item
        and False, otherwise
        This allows you to code: if item in setA 
        """
        return item in self._items

    def add(self, item):
        """
        Adds a new item to the Set, 
        if the item is not already in the Set
        """
        if item not in self._items:
            self._items.append(item)

    def remove(self, item):
        """
        Removes an item from the Set, if it exists in the Set
        """
        if item in self._items:
            self._items.remove(item)

    def __str__(self):
        """
        Returns a string representation of the Set
        This method is called when str(setA) or print(setA) is coded.
        """
        return str(self._items)
    
    def __eq__(self, other_set):
        """
        Returns True if all the items in this set are the same
        items in the passed in other_set, and False, otherwise.
        This allows you to code: setA == setB 
        and get True or False returned.
        """
        if len(self) != len(other_set):
            return False
        else:
            return self.is_subset_of(other_set)
    
    def is_subset_of(self, other_set):
        """
        Returns True if all the items in this set are also 
        in the passed in other_set, and False, otherwise
        """
        for item in self:
            if item not in other_set:
                return False
        return True

    def union(self, other_set):
        """
        Creates a new Set by combining the items in this Set 
        with the items in the passed in other_set
        """
        new_set = Set()
        new_set._items = [] + self._items
        for item in other_set:
            if item not in self:
                new_set._items.append(item)
        return new_set

    def intersection(self, other_set):
        """
        Creates a new Set consisting of the items that are
        in both this Set and in the passed in other_set
        """
        new_set = Set()
        for item in self:
            if item in other_set:
                new_set._items.append(item)
        return new_set

    def difference(self, other_set):
        """
        Creates a new set consisting of the items that are
        in this set, but not in the passed in other_set
        """
        new_set = Set()
        for item in self:
            if item not in other_set:
                new_set._items.append(item)
        return new_set
        
    def __iter__(self):
        """
        Returns an iterator for traversing this set
        """
        return SetIterator(self._items)
        

class SetIterator:
    """
    An iterator for the Set ADT implemented as a Python list.
    """
    def __init__(self, the_list):
        """
        Initialize the list, from the one passed in
        Set the current item to index 0
        """
        self._set_items = the_list
        self._cur_item = 0

    def __iter__(self):
        """
        Return this iterator
        """
        return self

    def __next__(self):
        """
        Walk the Python list to return the next item in the set
        """
        if self._cur_item < len(self._set_items):
            item = self._set_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration
