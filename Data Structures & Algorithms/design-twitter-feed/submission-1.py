from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        h = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId] | {userId}:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                h.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(h)
        while h and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(h)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(h, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)