"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    """
    The left subtree of a node contains only nodes with values lesser than the node’s value.
    The right subtree of a node contains only nodes with values greater than or equal to the node’s value.
    The left and right subtree each must also be a binary search tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if self.value > value:
            if self.left is not None:
                # make that (left) node, call insert
                self.left.insert(value)
            else:
                # set the left to the new node with the new value
                self.left = BSTNode(value)

        # elif new value >= self.value
        if self.value <= value:
            # if self.right is already taken by node
            if self.right is not None:
                # make that (right) node call insert
                self.right.insert(value)
            # set the right child to the new node with new value
            else:
                self.right = BSTNode(value)
                return True
            """
            # if there is no left child already here
            # add the new node to the left
            if self.left != None:
                self.left.insert(value)
                # create a BSTNode and encapsulate the value in it then set it to the left
                # otherwise call insert on the left node
            else:
                self.left = BSTNode(value)
                # otherwise (the new nodes value is greaterthan or equal to the current node value)
        if self.value >= value:
            # if there is no right child already here
            if self.right is None:
                # add the new node to the right
                self.right.insert(value)
                # create a BSTNode and encapsulate the value in it then set it to the right
                # otherwise call insert on the right node
            else:
                self.right = BSTNode(value)
                return True
        """
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if the value of the current node matches the target
        # return True
        if self.value is target:
            return True
            # check if the target is less than the current nodes value
        if self.value > target:
            # if there is no left child already here
            # return False
            if self.left is None:
                return False
            # otherwise
            # return a call of contains on the left child passing in the target value
            result = self.left.contains(target)
        # otherwise (the target is greater than the current nodes value)
        if self.value < target:
            # if there is no right child already here
            # return False
            if self.right is None:
                return False
            # otherwise
            # return a call of contains on the right child passing in the target value
            result = self.right.contains(target)

        return result

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
        # return None
        current = self
        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
        # return the nodes value
        # return a call to get max on the right child
        # -----------------------------------------------

        # iterative aproach

        # initialise the max value

        # get a ref to the current node
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.right
        return max_val

        # loop while there is still a current node
        # if the current value is greater than the max value, update the max value
        # move on to the next right node

        # return the max value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.value is None:
            pass
        else:
            fn(self.value)
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)
        # call the function passing in the current nodes value

        # if there is a node to the left
        # call the function on the left value

        # if there is a node to the right
        # call the function on the right node

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()
