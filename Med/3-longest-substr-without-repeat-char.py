class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        sub_strs = []
        sub_str = []

        if s == '':
            return 0

        while i < len(s):
            substr = s[i]
            if substr not in sub_str:
                sub_str.append(substr)
            else:
                sub_strs.append(sub_str.copy())
                #The following code doesn't work for the case below.
                #s = "dvdf"
                #sub_str.clear()
                '''
                d → no duplicate → add → ['d']
                v → no duplicate → add → ['d', 'v']
                d → duplicate → append ['d', 'v'] to sub_strs, then:

                sub_str.clear() → now empty
                sub_str.append('d') → ['d']
                But this misses the potential substring vdf, which is valid and longer.
                '''
                dup_index = sub_str.index(substr)
                sub_str = sub_str[dup_index + 1:]
                #This way, it only cuts the duplicate and earlier part.
                sub_str.append(substr)
            i = i + 1
            if i == len(s):
                sub_strs.append(sub_str.copy())
        lens = []
        if sub_strs:
            for substr in sub_strs:
                lens.append(len(substr))
        else:
            lens.append(len(sub_str))
        return max(lens)
        
