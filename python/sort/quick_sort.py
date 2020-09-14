from typing import List

## 挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
## 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
## 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
class Solution:
    def quick_sort(self, nums: List[int]):
        n = len(nums)
        self.qSort(nums, 0, n - 1)

    def qSort(self, nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.qSort(nums, left, index - 1)
            self.qSort(nums, index + 1, right)

    def partition(self, nums, left, right):
        small = left - 1
        pivot = nums[right]
        for i in range(left, right):
            if nums[i] < pivot:
                small += 1
                if small != i:
                    nums[small], nums[i] = nums[i], nums[small]
        small += 1
        nums[small], nums[right] = nums[right], nums[small]
        return small

nums = [64, 34, 25, 12, 22, 11, 90]
Solution().quick_sort(nums)
print(nums)