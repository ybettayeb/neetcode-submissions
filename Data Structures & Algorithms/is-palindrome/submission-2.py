class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_s = ''.join([i.lower() for i in s if i.isalnum()])
        i = 0
        j = len(sanitized_s)-1

        while i < j:
            if sanitized_s[i] != sanitized_s[j]:
                return False
            i = i +1
            j = j-1
        return True

        