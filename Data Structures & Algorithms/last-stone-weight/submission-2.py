import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, y - x)
            elif x < y:
                heapq.heappush(stones, x - y)
        if stones:
            return heapq.heappop(stones) * -1
        else:
            return 0

            