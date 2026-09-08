class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            IndDiff = seen.get(diff)
            if IndDiff !=None:
                return [IndDiff, i]
            else:
                seen[nums[i]] = i
