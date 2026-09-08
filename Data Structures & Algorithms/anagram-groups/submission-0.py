class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for word in strs:
            if hMap.get(tuple(sorted(word))) != None:
                hMap.get(tuple(sorted(word))).append(word)
            else:
                hMap[tuple(sorted(word))] = [word]

        return list(hMap.values())
        