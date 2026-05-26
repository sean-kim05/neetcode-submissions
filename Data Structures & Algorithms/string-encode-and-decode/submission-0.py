class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "*" + i
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            n = i
            while s[n] != "*":
                n += 1
            length = int(s[i:n])
            word = s[n + 1: n + length + 1]
            res.append(word)
            i = n + length + 1
            
        
        return res