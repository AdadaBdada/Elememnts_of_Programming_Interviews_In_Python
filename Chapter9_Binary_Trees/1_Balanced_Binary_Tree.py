# Leetcode 110. Balanced Binary Tree

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    pass


if __name__ == "__main__":
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))
    print(BalancedStatusWithHeight)
