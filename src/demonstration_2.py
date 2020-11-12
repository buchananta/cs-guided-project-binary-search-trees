"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_BST(self, root):
    # Your code here
    return recurse(root, float('-inf'), float('inf')
    
def recurse(root, min_bound, max_bound):
    if root is None:
        return True
    elif root.value < min_bound or root.value > max_bound:
        return False
    else:
      return recurse(root.left, min_bound, root.value - 1) \
      and recurse(root.right, root.value, max_bound - 1)

# With in-order traversal
def in_order_traverse(root, result = []):
    if not root:
        return
    in_order_traverse(root.left, result)
    result.append(root.value)
    in_order_travers(root.right, result)

def is_sorted(elements):
    # traverse elements two at a time
    for i in range(1, len(elements)):
        if elements[i -1] > elements[i]:
            return False
    return True

def is_valid_BST(root):
    elements = in_order_traverse(root)
    return is_sorted(elements)
