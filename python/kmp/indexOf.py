from typing import List

# 求模式串在主串中的位置, 没有则返回-1

class Solution1:
    ## 暴力破解法
    def indexOf(self, s: str, p: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1 # 一旦不匹配，i后退，j归0
                j = 0
        if j == len(p):
            return i - j
        return -1

class Solution2:
    # KMP算法
    # 求模式串的next数组，表示模式串位置 j 不匹配时，左移的位置，-1表示需要移动主串了
    def getNext(self, p: str) -> List(int):
        j = 0
        k = -1
        next = [-1] * len(p)
        while j < len(p) - 1:
            if k == -1 or p[j] == p[k]:
                j += 1
                k += 1
                if p[j] == p[k]:
                    next[j] = next[k] # 对next的进一步优化，p[j+1]与p[k+1]相同时，可以避免不必要的比较，进一步移动模式串
                else:
                    next[j] = k # p[j], p[k]相同时，next[j+1] = k+1
            else:
                k = next[k] # p[j], p[k]相同时，不断循环找k的位置
        return next


    def indexOf(self, s: str, p: str) -> int:
        next = self.getNext(p)
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(p):
            return i - j
        return -1
        