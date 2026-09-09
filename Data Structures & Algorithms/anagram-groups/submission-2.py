class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seens = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in seens:
                seens[sorted_s] += [s]
            else:
                seens[sorted_s] = [s]    
        return list(seens.values())

        