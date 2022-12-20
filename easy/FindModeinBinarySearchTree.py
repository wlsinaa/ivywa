class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.a = {}
        # left
        self.add(root)
        times = 0
        item = []
        for i in self.a:
            if self.a.get(i) == times:
                item.append(i)
            if self.a.get(i) > times:
                times = self.a.get(i)
                item = []
                item.append(i)

        return item

    def add(self, node):
        if node:
            if node.val not in self.a.keys():
                self.a[node.val] = 0
            self.a[node.val] += 1
            L = self.add(node.left)
            R = self.add(node.right)