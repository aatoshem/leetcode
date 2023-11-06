from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = -1
        hi = len(nums)
        while lo + 1 != hi:
            mid = (lo + hi) >> 1
            if nums[mid] == target:
                return mid
            # left side is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid
            # right side is sorted
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid
        return -1

if __name__ == '__main__':
    Solution().search([1,3], 2)