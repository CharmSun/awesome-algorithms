from typing import List

## 归并排序：
## 分割：递归地把当前序列平均分割成两半。
## 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
class Solution:
    def merge_sort(self, nums: List[int]):
        tmp_nums = [0] * len(nums)
        self.m_sort(nums, tmp_nums, 0, len(nums)-1)

    def m_sort(self, nums: List[int], tmp_nums: List[int], l, r):
        if l < r:
            m = (l + r) // 2
            self.m_sort(nums, tmp_nums, l, m)
            self.m_sort(nums, tmp_nums, m+1, r)
            self.merge(nums, tmp_nums, l, m, r)

    def merge(self, nums, tmp_nums, l, m, r):
        i = l
        j = m+1
        k = l
        while i <= m and j <= r:
            if nums[i] <= nums[j]:
                tmp_nums[k] = nums[i]
                i += 1
            else:
                tmp_nums[k] = nums[j]
                j += 1
            k += 1
        while i <= m:
            tmp_nums[k] = nums[i]
            k += 1
            i += 1
        while j <= r:
            tmp_nums[k] = nums[j]
            k += 1
            j += 1
        for k in range(l, r+1):
            nums[k] = tmp_nums[k]

nums = [64, 34, 25, 12, 22, 11, 90]
Solution().merge_sort(nums)
print(nums)