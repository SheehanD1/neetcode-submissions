class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = ((r - l) // 2) + l
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
            