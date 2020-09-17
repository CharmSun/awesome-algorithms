from mod.tree_node import TreeNode, buildTree

class Solution:
    def postorderTraversal(self, root: TreeNode):
        ret = []
        p = root
        stack = []
        while p or stack:
            if p:
                ret.append(p.val)
                stack.append(p)
                p = p.right
            else:
                node = stack.pop()
                p = node.left
        return ret[::-1]
        
root = buildTree([1,None,2,3])
print(Solution().postorderTraversal(root))