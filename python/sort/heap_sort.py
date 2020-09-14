from typing import List

class Solution:
    ## 将元素i 下滤
    def perc_down(self, nums, i, n):
        tmp = nums[i]
        cur = i
        while 2 * cur + 1 < n:
            child = 2 * cur + 1
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if nums[child] > tmp:
                nums[cur] = nums[child]
                cur = child
            else:
                break
        nums[cur] = tmp

    def heap_sort(self, nums: List[int]):
        ## 最后一个有孩子的节点，开始下滤
        i = len(nums) // 2 - 1  
        ## 建立大顶堆
        while i >= 0:
            self.perc_down(nums, i, len(nums))
            i -= 1
        ## 将最大值交换放至最后，下滤位置0
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.perc_down(nums, 0, i)

nums = [64, 34, 25, 12, 22, 11, 90]
Solution().heap_sort(nums)
print(nums)