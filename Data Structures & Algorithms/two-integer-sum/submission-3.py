class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: element value: index of the element
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
