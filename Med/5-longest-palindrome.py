class Solution:
    def longestPalindrome(self, s: str) -> str:
     
        if s == s[::-1]:
            return s
     
        min = 2 # 🚫 Never use 'min' as a variable name. Use such as min_len
        i = min
        sub_strs = []

        i = min
        # It's storing all palindromic substrings and lengths — unnecessary memory usage.
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
            # This can be simplified. If sub_strs is empty and the string isn't a palindrome, the longest palindromic substring is always s[0].
            if len(s) == 1:
                return s
            else:
                return s[0:1]
            
