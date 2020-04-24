""" Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive approach


class Solution:
    def isValidBST(self, root):
        return self.validator(root)

    def validator(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        # Is this particular node following the BST rules?
        if val <= lower or val >= upper:
            return False
        # Recursively validate through right and left nodes
        # This node (val) will be the new lower limit for all nodes to its right
        if not self.validator(node.right, val, upper):
            return False
        # This node (val) will be the new upper limit for all nodes to its left
        if not self.validator(node.left, lower, val):
            return False
        return True

# Time complexity : O(N), we traverse each node.
# Space complexity : O(N), we store the entire tree.
