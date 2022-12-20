def dfs(self, node, parent, grandparent):
    if grandparent and grandparent.val % 2 == 0:
        self.sumG += node.val
    if node.left: self.dfs(node.left, node, parent)
    if node.right: self.dfs(node.right, node, parent)