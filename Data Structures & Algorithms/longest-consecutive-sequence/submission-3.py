class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max = 0

        for num in numbers:
            if num - 1 not in numbers:
                sequence = num
                length = 1
                while sequence + 1 in numbers:
                    sequence += 1
                    length += 1
                if length > max:
                    max = length
        
        return max
        
        