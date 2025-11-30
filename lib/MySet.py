class MySet:
    """
    A custom implementation of a Set data structure using a Dictionary (hash map)
    to ensure O(1) average time complexity for core operations like add, delete, and has.
    """

    def __init__(self, enumerable=[]):
        """
        Initializes a new MySet. 
        It adds unique values from an iterable (like a list) to the internal dictionary.
        """
        self.dictionary = {}
        # Iterate over the input list and add each value as a key to the dictionary.
        # Since dictionary keys must be unique, this naturally handles duplicates.
        for value in enumerable:
            self.dictionary[value] = True  # Value doesn't matter, only the key's presence

    def has(self, value):
        """
        Checks if the value is present in the MySet. Must have O(1) runtime.
        """
        # Checking for key existence in a dictionary is O(1) average time.
        return value in self.dictionary

    def add(self, value):
        """
        Adds the value to the MySet if it isn't already present. Must have O(1) runtime.
        """
        # Inserting a key/value pair into a dictionary is O(1) average time.
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """
        Removes the value from the MySet. Must have O(1) runtime.
        """
        # pop() is used to remove a key. The optional 'None' is the default
        # return value if the key is not found, preventing a KeyError exception.
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """
        Returns the number of elements in the MySet.
        """
        return len(self.dictionary)

    # --- Bonus Methods ---

    def clear(self):
        """
        Removes all items from the set, and returns the updated set.
        """
        self.dictionary.clear()
        return self

    def __str__(self):
        """
        Provides a readable string representation of the MySet (e.g., MySet: {1, 2, 3}).
        """
        # Get all the keys (the set elements) and convert them to strings
        set_list = [str(key) for key in self.dictionary.keys()]
        # Join the list elements with a comma and space, and format the output string
        return f'MySet: {{{", ".join(set_list)}}}'
pass