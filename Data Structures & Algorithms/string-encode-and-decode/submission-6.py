class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = ";".join(str(len(word)) for word in strs)
        words = "".join(strs)
        return sizes + "#" + words



    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        Components = s.split("#",1)
        if not Components[0]:
            return []
        sizes = Components[0].split(";")
        words = Components[1]
        strs = []
        totalIndex = 0
        for size in sizes:
            word = words[totalIndex:totalIndex+int(size)]
            strs.append(word)
            totalIndex = totalIndex + int(size)
        return strs
