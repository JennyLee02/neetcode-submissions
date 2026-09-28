class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26

        # we want index of the array to represent each alphabet using ord()
        # element at each index will represent the frequency

        for i in range(len(s)):
            if len(s) != len(t):
                return False
            countS[ord(s[i]) - ord('a')] += 1
            countT[ord(t[i]) - ord('a')] += 1
        
        return countS == countT

