class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> check = new HashSet<>();
        while (n != 1) {
            String temp = Integer.toString(n);
            int result = 0;
            while (n > 0) {
                int digit = n % 10;
                result += digit * digit;
                n /= 10;
            }
            if (check.contains(result)) {
                return false;
            }
            check.add(result);
            n = result;
        }
        return true;
    }
}
