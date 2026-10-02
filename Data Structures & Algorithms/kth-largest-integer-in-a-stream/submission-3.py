import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        n = len(nums)
        heapq.heapify(self.nums) 
        for i in range(n - k):
            heapq.heappop(nums)    

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            result = heapq.heappop(self.nums)
            heapq.heappush(self.nums, result)
            return result
        elif len(self.nums) == self.k:
            result = heapq.heappop(self.nums)
            heapq.heappush(self.nums, result)
            return result
        else:
            return None

