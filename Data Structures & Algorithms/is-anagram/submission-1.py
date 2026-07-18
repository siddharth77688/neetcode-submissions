from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = Counter(s)
        str2 = Counter(t)

        if str1 == str2:
            return True
        
        return False