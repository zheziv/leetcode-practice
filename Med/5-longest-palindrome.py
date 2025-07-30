class Solution:
    def longestPalindrome(self, s: str) -> str:
     
        if s == s[::-1]:
            return s
     
        min = 2
        i = min
        sub_strs = []

        i = min
        while i <= len(s):
            for j in range(len(s)):
                if i + j <= len(s):
                    substr = s[j:i+j]
                    if substr == substr[::-1]:
                        sub_strs.append(substr)
            i = i + 1

        if sub_strs:
            i_lens = {}
            for substr in sub_strs:
                i_lens[substr] = len(substr)
            return max(i_lens, key=i_lens.get)
        else:
            if len(s) == 1:
                return s
            else:
                return s[0:1]
            
