class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo = 0
        hi = x
        #
        while lo + 1 != hi:
            mid = (lo + hi) >> 1
            num = mid ** 2
            if num <= x:
                lo = mid
            else:
                hi = mid
            return lo if lo ** 2 == x else 1


if __name__ == '__main__':
    print(Solution().mySqrt(6))
