class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int lowestPrice = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < lowestPrice) {
                lowestPrice = prices[i];
            } else {
                max = max < prices[i] - lowestPrice ? prices[i] - lowestPrice : max;
            }
        }
        return max;
    }
}
