from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        maxFreq = 0
        longestSub = 0
        freq = defaultdict(int)
        for end in range(len(s)):
            c = s[end]

            freq[c] += 1

            maxFreq = max(maxFreq, freq[c])

            if (end - start + 1 - maxFreq > k):
                freq[s[start]] -= 1
                start += 1

            longestSub = max(longestSub, end - start + 1)

        return longestSub