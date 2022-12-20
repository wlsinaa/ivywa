# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        default = 0
        self.a = []
        self.findeven(root)
        return sum(self.a)
    def findeven(self,tree2):
        if tree2:
            if tree2.val % 2 ==0:
                self.findgradson(tree2,2)
            self.findeven(tree2.left)
            self.findeven(tree2.right)
    def findgradson(self, tree,level):
        if tree and level >= 0:
                # append
            if level == 0:
                self.a.append(tree.val)
            self.findgradson(tree.left,level - 1)
            self.findgradson(tree.right,level - 1)