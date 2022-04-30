import bisect
import  Node


class BTree:
    ROOT = LEAF = Node.Node

    """
    examples:

    >>> b = BTree.BTree(2)
    """

    def __init__(self,order):
        """
        :param order : the order of the BTree
        :type order : Integer
        nbOfKeys =m-1
        nbOfChildren =m
        """
        self._root = self.LEAF(self)
        self.order = order
    
    def is_empty(self):
        """"
        Predicates that test *tree* is an empty tree.

        :param tree: The tree
        :type tree: dict or None
        :return: True if *tree* is empty, False otherwise
        :rtype: bool
        """
        return self.root is None
        
    def _path_to(self, key):
        """
       
        Return  the path from the root to *key*

        :param key: The key
        :type key: integer
        :return: a list of paths (the type of the node and the order of the node) from the root to the key 
        :rtype: list of tuples
        :examples:
        >>> b.search(2,b.root)
        >>> b._path_to(8)
        [(<Root 5>, 1), (<Root 7>, 1), (<Leaf 8, 9>, 0)]
        """

        current = self._root
        ancestry = []

        while getattr(current, "children", None):
            index = bisect.bisect_left(current.keys, key)
            ancestry.append((current, index))
            if index < len(current.keys) and current.keys[index] == key:
                return ancestry
            current = current.children[index]

        index = bisect.bisect_left(current.keys, key)
        ancestry.append((current, index))
        present = index < len(current.keys)
        present = present and current.keys[index] == key

        return ancestry

    def _present(self, key, ancestors):
        """
        Predicate that test if *key* is in the ancestors
        :param key : the key tha we're look to 
        :param ancestors : the ancestors 
        :return : True if the key is found , false otherwise
        : rtype: Boolean
        """
        last, index = ancestors[-1]
        return index < len(last.keys) and last.keys[index] == key
    
    def search(self, key):
        """
        Predicates that test *key* is in the tree.
        
        :param key: The key
        :type key: integer
        :return: True if *root* is in the tree, False otherwise
        :rtype: bool
        :examples:

        >>> b.search(2)
        True
        >>> b.search(0)
        True
        >>> b.search(5)
        False
        >>> b.search(1)
        True
        """

        return self._present(key, self._path_to(key))


    def insert(self, key):
        """
        Insert  *key* at the correct position the maintain a sorted order

        :param key: The key
        :type key: integer
        :return: None

        :examples:

        >>> t= BTree(2)
        >>> t.search(2)
        False
        >>> t.insert(2)
        >>> t.search(2)
        True
        """
        ancestors = self._path_to(key)
        node, index = ancestors[-1]
        while getattr(node, "children", None):
            node = node.children[index]
            index = bisect.bisect_left(node.keys, key)
            ancestors.append((node, index))
        node, index = ancestors.pop()
        node.insert(index, key, ancestors)
    
    def delete(self, key):
        """
        Delete  the *key* in the tree

        :param key: The key
        :type key: integer
        :return: None
        :examples:
        >>> t = BTree(2)
        >>> t.insert(3)
        >>> t.delete(3)
        >>> t.delete(14)
        ValueError: 14 not in BTree
  
        """
        ancestors = self._path_to(key)

        if self._present(key, ancestors):
            node, index = ancestors.pop()
            node.delete(index, ancestors)
        else:
            raise ValueError("%r not in %s" % (key, self.__class__.__name__))

  
    def __iter__(self):
        def _recurse(node):
            if node.children:
                for child, key in zip(node.children, node.keys):
                    for child_item in _recurse(child):
                        yield child_item
                    yield key
                for child_item in _recurse(node.children[-1]):
                    yield child_item
            else:
                for key in node.keys:
                    yield key

        for key in _recurse(self._root):
            yield key

    def __repr__(self):
        def recurse(node, accum, depth):
            accum.append(("  " * depth) + repr(node))
            for node in getattr(node, "children", []):
                recurse(node, accum, depth + 1)

        accum = []
        recurse(self._root, accum, 0)
        return "\n".join(accum)  
    
    
"""  
   
    def str(self):
        r = self.root
        return str(r+ '\n'.join([children for children in r.children]))

        
    def isBTree(self,root):
        
        Predicates that test *tree* is a Btree.

        :param root: The root
        :type root: Node or None
        :return: True if *tree* is b-tree, False otherwise
        :rtype: bool
        
        pass
    
    def linear_tree (self,root):
        
        Predicates that test *tree* is an empty tree.

        :param tree: The tree
        :type tree: dict or None
        :return: True if *tree* is empty, False otherwise
        :rtype: list
        
        pass

    def balanced(self,root):
        
        Predicates that test *tree* is an empty tree.

        :param root: The root
        :type root: Node or None
        :return: True if *tree* is balanced, False otherwise
        :rtype: bool
        
        pass

    def height_leaves(self,root):
        
        Predicates that test *tree* is an empty tree.

        :param root: The root
        :type root: Node or None
        :return: True if *tree* is empty, False otherwise
        :rtype: bool
        
        pass

    def operation(self):
        
        Predicates that test *tree* is an empty tree.

        :param tree: The tree
        :type tree: dict or None
        :return: True if *tree* is empty, False otherwise
        :rtype: None
        
        pass

"""

        
def main():
    b = BTree(2)
    for i in range(10):
        b.insert(i)
    print(b)
    print("after deletion")
    b.delete(1)
    print(b)
   


if __name__ == '__main__':
    main()