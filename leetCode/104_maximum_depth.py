# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

s = Solution()

f = TreeNode(10)

assert s.maxDepth(f) == 1
f = TreeNode(10)
l = TreeNode(9)
r = TreeNode(11)
f.left = l
f.right = r
assert s.maxDepth(f) == 2
f.left.left = TreeNode(8)
assert s.maxDepth(f) == 3
