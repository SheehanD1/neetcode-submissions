class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> check = new HashSet<>();
        for (int n : nums) {
            if (check.contains(n)) {
                return true;
            }
            check.add(n);
        }
        return false;
    }
}
