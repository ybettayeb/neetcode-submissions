class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        queue = []
        matching = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in ["(","{","["]:
                queue.append(char)
            elif char in [")","}","]"]:
                if not queue or queue.pop() != matching[char]:
                    return False
        if queue:
            return False
        return True
