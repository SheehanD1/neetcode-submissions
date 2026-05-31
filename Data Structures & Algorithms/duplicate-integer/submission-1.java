class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> temp = new HashSet<>();
        for (int num : nums) {
            if (temp.contains(num)){
                return true;
            } else{
                temp.add(num);
            }
        }
        return false;
    }
}