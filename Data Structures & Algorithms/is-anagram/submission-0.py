class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        f = {}
        for c in s:
            if c in f:
                f[c] += 1
            else: 
                f[c] = 1
        for c in t:
            if c not in f: False
            elif f[c] == 1:
                del f[c]
            else: 
                f[c] -=1
        return not f 