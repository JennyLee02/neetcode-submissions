from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        # key: count array, value: list of words
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord("a")] += 1
            anagram[tuple(count)].append(i)
        
        return list(anagram.values())
        
            


