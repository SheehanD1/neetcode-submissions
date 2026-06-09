class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0;
        for n in nums:
            if (n-1) not in store:
                cur = 0
                temp = n
                while temp in store:
                    temp+= 1
                    cur+= 1
                if cur > result:
                    result = cur
        return result
        