class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nbNums = len(nums)
        return len(set(nums)) != nbNums