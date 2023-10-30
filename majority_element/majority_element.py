class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = None
        count  = 0
        for val in nums:
            if count == 0:
                answer = val
            # Notice here that if we change this if answer == val to elif,
            # we need to add count = 1 in line 7 (first condition)
            if answer == val:
                count += 1
            else:
                count -= 1
        return answer


