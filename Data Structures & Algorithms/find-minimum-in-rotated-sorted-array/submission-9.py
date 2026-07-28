class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = ((r - l) // 2) + l
            if nums[m] < nums[l]:
                r = m 
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                return nums[l]

        return -1
              