class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        while left < right:
            if (heights[right] if heights[left] > heights[right] else heights[left]) * (right - left) > result:
                result = (heights[right] if heights[left] > heights[right] else heights[left]) * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result

        