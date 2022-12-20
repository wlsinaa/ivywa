class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        else:
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val != q.val:
                return False
            L = True
            R = True
            if p.left and p.left:
                L = self.isSameTree(p.left, q.left)
            if q.right and q.right:
                R = self.isSameTree(p.right, q.right)

            if (not p.left and q.left) or (p.left and not q.left):
                L = False
            if (not p.right and q.right) or (p.right and not q.right):
                R = False
        return (L and R)