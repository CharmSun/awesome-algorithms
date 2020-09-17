from mod.tree_node import TreeNode, buildTree
    
class Solution:
    def inorderTraversal(self, root: TreeNode):
        ret = []
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                ret.append(node.val)
                p = node.right
        return ret

root = buildTree([1,None,2,3])
print(Solution().inorderTraversal(root))