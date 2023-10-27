import re
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        noOnes = re.sub(r'1', '', s)
        noZeroes = re.sub(r'0', '', s)
        return re.sub(r'1$', noOnes + '1', noZeroes)