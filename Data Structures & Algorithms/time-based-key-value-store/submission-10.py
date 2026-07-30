class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = 0
        r = len(self.store[key]) - 1
        temp = ""
        while l <= r:
            m = ((r - l)//2) + l
            if self.store[key][m][1] == timestamp:
                return self.store[key][m][0]
            if self.store[key][m][1] > timestamp:
                r = m - 1
            else:
                if self.store[key][m][1] <= timestamp:
                    temp = self.store[key][m][0]
                l = m + 1
                
        
        return temp
