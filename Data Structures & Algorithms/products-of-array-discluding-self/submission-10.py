class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = [1] * len(nums)
        prefix[0] = 1
        sufix = [1] * len(nums)
        sufix[len(nums) - 1] = 1
        right = 1
        for i in range(1, len(nums), 1):
            right *= nums[i - 1]
            prefix[i] = right
        left = 1
        for i in range(len(nums) - 2, -1, -1):
            left *= nums[i + 1]
            sufix[i] = left
        for i in range(len(result)):
            result[i] = prefix[i] * sufix[i]
        return result