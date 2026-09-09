class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, concat_strs = "",""
        for s in strs:
            sizes = sizes + str(len(s)) + ";"
            concat_strs = concat_strs + s
        return sizes + "#" + concat_strs




    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        # Split into [sizes_part, strings_part]
        parts = s.split("#", 1)
        sizes_part = parts[0]
        strs = parts[1]
        
        # NOW split only the sizes part
        sizes = sizes_part.split(";")
        # Remove empty string from trailing ";"
        sizes = [x for x in sizes if x]
        
        res = []
        totalSize = 0
        for size in sizes:
            res.append(strs[totalSize:totalSize + int(size)])
            totalSize += int(size)
        return res



