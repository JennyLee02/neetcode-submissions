class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap) key: num value: frequency
        # bucket is list of lists
        # bucket) index is the frequency, and the element is elements with that        frequency

        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []
        
        # [0] * 26, list of lists but we're initialize empty lists

        for i in range(len(nums)):
           hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        for number, frequency in hashmap.items():
            buckets[frequency].append(number)
        # [[], [1], [2], [3]] -> [2,3] ??
        # [[3], [2], [1]]
        # [3] -> to our list
        # [3, 2]
        for b in buckets[::-1]:
            for j in b:
                res.append(j)
            if len(res) == k: 
                return res
            

        