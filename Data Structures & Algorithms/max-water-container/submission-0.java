class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        int left = 0;
        int right = heights.length - 1;
        while (left < right) {
            int curHeight = Math.min(heights[left], heights[right]);
            int curArea = (right - left) * curHeight;
            if (curArea > maxArea) {
                maxArea = curArea;
            }
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
