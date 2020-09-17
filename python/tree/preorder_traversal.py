from mod.tree_node import TreeNode, buildTree

class Solution:
    def preorderTraversal(self, root: TreeNode):
        ret = []
        p = root
        stack = []
        while p or stack:
            if p:
                ret.append(p.val)
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                p = node.right
        return ret

root = buildTree([1,None,2,3])
print(Solution().preorderTraversal(root))