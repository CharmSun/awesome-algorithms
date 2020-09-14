from typing import List

class Solution:

    ## 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
    ## 但希尔排序是非稳定排序算法。
    ## 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
    ## 待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
    def shell_sort(self, nums: List[int]):
        n = len(nums)
        increment = n // 2
        while increment > 0:
            for i in range(increment, n):
                tmp = nums[i]
                j = i
                while j >= increment:
                    if nums[j - increment] > tmp:
                        nums[j] = nums[j - increment]
                        j -= increment
                    else:
                        break
                nums[j] = tmp
            increment = increment // 2

nums = [64, 25, 12, 22, 11] 
Solution().shell_sort(nums)
print(nums)