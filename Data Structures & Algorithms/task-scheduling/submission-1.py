import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [-c for c in count.values()]
        heapq.heapify(h)

        time = 0
        q = collections.deque()

        while h or q:
            time += 1

            if h:
                c = 1 + heapq.heappop(h)
                if c != 0:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        return time