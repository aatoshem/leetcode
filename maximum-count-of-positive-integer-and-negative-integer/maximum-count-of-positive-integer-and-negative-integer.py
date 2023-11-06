import math
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def binSearch(nums, target):
            lo = -1
            hi = len(nums)
            while lo + 1 != hi:
                mid = (lo + hi) >> 1
                if nums[mid] < target:
                    lo = mid
                else:
                    hi = mid
            return hi

        # Gets All negatives
        neg = binSearch(nums, 0)
        # Gets All negatives + Zeroes
        neg_zeroes = binSearch(nums, 1)
        pos = len(nums) - neg_zeroes
        return max(pos, neg)

if __name__ == '__main__':
    print(Solution().maximumCount([-1563,-236,-114,-55,0,447,687,752,1021,1636]))