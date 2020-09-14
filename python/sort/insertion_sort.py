from typing import List

class Solution:

    ## 插入排序：通过构建有序序列，对于未排序数据，
    # 在已排序序列中从后向前扫描，找到相应位置并插入。
    def insertion_sort(self, nums: List[int]):
        for i in range(1, len(nums)):
            cur = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > cur:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = cur

nums = [12, 11, 13, 5, 6] 
Solution().insertion_sort(nums)
print(nums)