from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums):
    if not nums:
        return None
    n = len(nums)
    index = 0
    head = TreeNode(nums[index])
    queue = deque()
    queue.append(head)
    while index < n:
        index += 1
        if index >= n:
            return head
        cur = queue.popleft()
        if nums[index]:
            cur.left = TreeNode(nums[index])
            queue.append(cur.left)

        index += 1
        if index >= n:
            return head
        if nums[index]:
            cur.right = TreeNode(nums[index])
            queue.append(cur.right)