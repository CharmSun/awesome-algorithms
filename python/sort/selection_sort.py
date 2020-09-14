from typing import List

class Solution:

    ## 选择排序：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    # 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    # 以此类推，直到所有元素均排序完毕。
    def selection_sort(self, nums: List[int]):
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

nums = [64, 25, 12, 22, 11] 
Solution().selection_sort(nums)
print(nums)