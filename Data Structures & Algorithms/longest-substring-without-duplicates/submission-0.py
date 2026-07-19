class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hset = set()
        left =0  
        maxLen = 0

        for right in range(n):

            while s[right] in hset:
                hset.remove(s[left])
                left += 1
            
            hset.add(s[right])
            maxLen = max(maxLen,right-left+1)
        return maxLen