class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # populate hashmap
        # hashmap) key: number value: freq

        hashmap = {}
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        # populate buckets
        # bucket contains buckets where each sub-bucket holds the numbers of corresponding frequency. index of the bucket represents the frequency

        for number, freq in hashmap.items():
            buckets[freq].append(number)

        # put top k into buckets
        for i in buckets[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res


        