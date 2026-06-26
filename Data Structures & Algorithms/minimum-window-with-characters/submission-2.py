class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        T = {}
        curWindow = {}
        for c in t:
            T[c] = 1 + T.get(c, 0)
        have = 0
        need = len(T)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for c in range(len(s)):
            curWindow[s[c]] = 1 + curWindow.get(s[c], 0)
            if s[c] in T and curWindow[s[c]] == T[s[c]]:
                have += 1
            while have == need:
                if (c - l + 1) < resLen:
                    res = [l, c]
                    resLen = (c - l + 1)
                curWindow[s[l]] -= 1
                if s[l] in T and curWindow[s[l]] < T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""




        