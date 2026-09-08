class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longestChain = 1
        currentChain = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # Ignore duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:
                currentChain += 1
            else:
                currentChain = 1

            longestChain = max(longestChain, currentChain)

        return longestChain


                

        