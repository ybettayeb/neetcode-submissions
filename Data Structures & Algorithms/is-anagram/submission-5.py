class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmapS, hmapT = {}, {}

        for i in range(len(s)):
            hmapS[s[i]] = 1 + hmapS.get(s[i], 0)
            hmapT[t[i]] = 1 + hmapT.get(t[i], 0)
        return hmapT == hmapS