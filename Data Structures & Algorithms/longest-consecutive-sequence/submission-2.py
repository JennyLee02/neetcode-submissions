class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all = set()
        max = 0
        
        for i in range(len(nums)):
            all.add(nums[i])
        for i in range(len(nums)):
            if nums[i] - 1 not in all:
                sequence = nums[i]
                count = []
                count.append(sequence)
                while sequence + 1 in all:
                    count.append(sequence + 1)
                    sequence += 1
                if len(count) > max:
                    max = len(count)
        
        return max