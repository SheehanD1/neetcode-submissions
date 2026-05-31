class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> check = new HashSet<>();
        int maxLength = 0;
        for (int num : nums) {
            check.add(num);
        }
        for (int i = 0; i < nums.length; i++) {
            int length = 0;
            while (check.contains(nums[i] + length)) {
                length++;
            }
            maxLength = maxLength < length ? length : maxLength;
        }
        return maxLength;
    }
}
