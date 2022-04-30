class Node:
    """
    
    """
    __slots__ = ["tree", "keys", "children"]

    def __init__(self, tree, keys=None, children=None):
        """
        :param tree: The tree
        :type tree: Btree
        :param keys : list of key
        :type Keys : List or None
        :param Children : list of child
        :type children : List or None
       
        """
        self.tree = tree
        self.keys = keys or []
        self.children = children or []
        if self.children:
            assert len(self.keys) + 1 == len(self.children), \
                    "one more child than data key required"

    def __repr__(self):
        name = getattr(self, "children", 0) and "Root" or "Leaf"
        return "<%s %s>" % (name, ", ".join(map(str, self.keys)))
    

    def is_leaf(self):
        """
        return true if the node is a leaf false otherwise
        """
        return self.children == []

    
    def lateral(self, parent, parent_index, dest, dest_index):
        """
        return true if the node is a leaf false otherwise
        """
        if parent_index > dest_index:
            dest.keys.append(parent.keys[dest_index])
            parent.keys[dest_index] = self.keys.pop(0)
            if self.children:
                dest.children.append(self.children.pop(0))
        else:
            dest.keys.insert(0, parent.keys[parent_index])
            parent.keys[parent_index] = self.keys.pop()
            if self.children:
                dest.children.insert(0, self.children.pop())

    def shrink(self, ancestors):
        """
        return true if the node is a leaf false otherwise
        """
        parent = None
        if ancestors:
            parent, parent_index = ancestors.pop()
            # try to lend to the left neighboring siblings
            if parent_index:
                left_sib = parent.children[parent_index - 1]
                if len(left_sib.keys) < self.tree.order:
                    self.lateral(parent, parent_index, left_sib, parent_index - 1)

            # try the right neighbor
            if parent_index + 1 < len(parent.children):
                right_sib = parent.children[parent_index + 1]
                if len(right_sib.keys) < self.tree.order:
                    self.lateral(parent, parent_index, right_sib, parent_index + 1)

        siblings, push = self.split_node()

        if not parent:
            parent, parent_index = self.tree.ROOT(
                    self.tree, children=[self]), 0
            self.tree._root = parent

        # pass the median up to the parent
        parent.keys.insert(parent_index, push)
        parent.children.insert(parent_index + 1, siblings)
        if len(parent.keys) > parent.tree.order:
            parent.shrink(ancestors)

    def grow(self, ancestors):
        """
        return true if the node is a leaf false otherwise
        """
        parent, parent_index = ancestors.pop()
        minimum = self.tree.order // 2
        left_sib = right_sib = None

        # try to borrow from the right siblings
        if parent_index + 1 < len(parent.children):
            right_sib = parent.children[parent_index + 1]
            if len(right_sib.keys) > minimum:
                right_sib.lateral(parent, parent_index + 1, self, parent_index)

        # try to borrow from the left siblings
        if parent_index:
            left_sib = parent.children[parent_index - 1]
            if len(left_sib.keys) > minimum:
                left_sib.lateral(parent, parent_index - 1, self, parent_index)

        # consolidate with a siblings - try left first
        if left_sib:
            left_sib.keys.append(parent.keys[parent_index - 1])
            left_sib.keys.extend(self.keys)
            if self.children:
                left_sib.children.extend(self.children)
            parent.keys.pop(parent_index - 1)
            parent.children.pop(parent_index)
        else:
            self.keys.append(parent.keys[parent_index])
            self.keys.extend(right_sib.keys)
            if self.children:
                self.children.extend(right_sib.children)
            parent.keys.pop(parent_index)
            parent.children.pop(parent_index + 1)

        if len(parent.keys) < minimum:
            if ancestors:
                # parent is not the root
                parent.grow(ancestors)
            elif not parent.keys:
                # parent is root, and its now empty
                self.tree._root = left_sib or self

    def split_node(self):
        """
        Split a node at the middle and find the key that should grow up and the new siblings 
        """
        center = len(self.keys) // 2
        median = self.keys[center]
        siblings = Node(self.tree,self.keys[center + 1:],self.children[center + 1:])
        self.keys = self.keys[:center]
        self.children = self.children[:center + 1]
        return siblings, median

    def insert(self, index, key, ancestors):
        """
        Insert 
        return true if the node is a leaf false otherwise
        """
        self.keys.insert(index, key)
        if len(self.keys) > self.tree.order:
            self.shrink(ancestors)

    def delete(self, index, ancestors):
        """
        Delete an index from a node
        :param index :
        :type index :
        :param ancestors :
        :type ancestors :
        :  
        """
        minimum = self.tree.order // 2

        if self.children:
            # try promoting from the right subtree first,
            # but only if it won't have to resize
            additional_ancestors = [(self, index + 1)]
            descendent = self.children[index + 1]
            while descendent.children:
                additional_ancestors.append((descendent, 0))
                descendent = descendent.children[0]
            if len(descendent.keys) > minimum:
                ancestors.extend(additional_ancestors)
                self.keys[index] = descendent.keys[0]
                descendent.remove(0, ancestors)

            # fall back to the left child
            additional_ancestors = [(self, index)]
            descendent = self.children[index]
            while descendent.children:
                additional_ancestors.append((descendent, len(descendent.children) - 1))
                descendent = descendent.children[-1]
            ancestors.extend(additional_ancestors)
            self.keys[index] = descendent.keys[-1]
            descendent.remove(len(descendent.children) - 1, ancestors)
        else:
            self.keys.pop(index)
            if len(self.keys) < minimum and ancestors:
                self.grow(ancestors)


    """
 

    def get_size(self):
        
        Return the node size

        :rtype: integer
        
        return self.__size


    def searchNode(self,key):
        
        Predicates that test  if *key* is in the node.

        :param key: The key
        :type key: integer
        :return: True if *key* is in keys, False otherwise
        :rtype: bool


        return key in self.keys


    def is_empty (self):
        
        Predicates that test *node* is an empty node.

        :param node: The node
        :type node: dict or None
        :return: True if *node* is empty, False otherwise
        :rtype: bool
        
        return self.parent is None 
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()