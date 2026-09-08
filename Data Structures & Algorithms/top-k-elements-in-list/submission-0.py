class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
                count[num] = 1 + count.get(num,0)
        sorted_count = sorted(
            count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [num for num, frequency in sorted_count[:k]]
            
        