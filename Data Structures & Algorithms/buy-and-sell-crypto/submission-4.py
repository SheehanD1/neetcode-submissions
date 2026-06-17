class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastSeen = prices[0]
        profit = 0
        for n in prices:
            if leastSeen > n:
                leastSeen = n
            if n - leastSeen > profit:
                profit = n - leastSeen
        return profit
            
