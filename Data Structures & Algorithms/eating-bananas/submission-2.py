class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        while l <= r:
            m = ((r - l) // 2) + l
            count = 0
            for n in piles:
                count += math.ceil(n/m)
            if count <= h:
                result = min(result, m)
                r = m - 1
            elif count > h:
                l = m + 1
        return result

        