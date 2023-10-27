import unittest
class Solution(unittest.TestCase):
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_of_ones = 0
        for c in s:
            if c == '1':
                count_of_ones += 1
        count_of_zeroes = len(s) - count_of_ones
        return '1' * (count_of_ones - 1) + '0' * count_of_zeroes + '1'


    def test_max_odd_binary_num_1(self):
        '''Test case function for max odd binary num'''
        self.calc = Solution()
        s = "010"
        result = self.calc.maximumOddBinaryNumber(s)
        expected = "001"
        self.assertEqual(result, expected)

    def test_max_odd_binary_num_1(self):
        '''Test case function for max odd binary num'''
        self.calc = Solution()
        s = "0101"
        result = self.calc.maximumOddBinaryNumber(s)
        expected = "1001"
        self.assertEqual(result, expected)

