import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        heapq.heapify(store)
        result = []

        for point in points:
            distance = (point[0] * point[0]) + (point[1] * point[1])
            heapq.heappush(store, (distance, point[0], point[1]))
        
        if store:
            for i in range(k):
                cur = heapq.heappop(store)
                result.append([cur[1], cur[2]])
            return result

        return None