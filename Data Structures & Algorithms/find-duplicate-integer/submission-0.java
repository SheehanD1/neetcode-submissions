class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> s = new HashSet<>();
        for (int num : nums) {
            if (!s.contains(num)) {
                s.add(num);
            } else {
                return num;
            }
        }
        return -1;
    }
}
