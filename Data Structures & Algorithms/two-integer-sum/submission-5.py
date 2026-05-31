class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, c in enumerate(nums):
            if target - c in seen:
                return [seen[target - c], i]
            seen[c] = i

        return []
            