class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        longest = s[0]  # at least one char will always be a palindrome

        for length in range(1, len(s) + 1):  # start from 1
            for start in range(len(s) - length + 1):
                substr = s[start:start + length]
                if substr == substr[::-1]:
                    if len(substr) > len(longest):
                        longest = substr
        return longest
