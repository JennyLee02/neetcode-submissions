class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]

        # populate hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        # populate buckets
        for number, freq in hashmap.items():
            buckets[freq].append(number)
        # put k elements in the res list
        for b in buckets[::-1]:
            for j in b:
                res.append(j)
                if len(res) == k:
                    return res
