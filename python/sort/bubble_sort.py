from typing import List

class Solution:

    ## 冒泡排序：重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    ## 一次冒泡将最大值冒至最后
    def bubble_sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n):
            for j in range(0, n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
nums = [64, 34, 25, 12, 22, 11, 90]
Solution().bubble_sort(nums)
print(nums)
            