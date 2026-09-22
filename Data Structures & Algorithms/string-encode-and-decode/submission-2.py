class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        ptr_1 = 0

        while ptr_1 < len(s):
            ptr_2 = ptr_1

            while s[ptr_2] != '#':
                ptr_2 += 1
            
            length = int(s[ptr_1 : ptr_2])
            start = ptr_2 + 1
            res.append(s[start:start + length])
            ptr_1 = start + length
        
        return res