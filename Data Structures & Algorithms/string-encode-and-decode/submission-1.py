class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            count = ""
            while s[i] != '#':
                count += s[i]
                i += 1
            result.append(s[i+1 : i +1+ int(count)])
            i += 1 + int(count)
        return result
            

