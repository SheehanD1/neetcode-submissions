class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = 0;
            for (int j = i; j < result.length; j++) {
                if (temperatures[i] < temperatures[j]) {
                    result[i] = j - i;
                    j = result.length;
                }
            }
        }
        return result;
    }
}
