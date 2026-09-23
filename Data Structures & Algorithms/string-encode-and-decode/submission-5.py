class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        ptr_1 = 0

        while ptr_1 < len(s):
            ptr_2 = ptr_1
            while s[ptr_2] != '#':
                ptr_2 += 1
            length = int(s[ptr_1:ptr_2])
            start = ptr_2 + 1
            decoded_strs.append(s[start:start+length])
            ptr_1 = start + length

        return decoded_strs
