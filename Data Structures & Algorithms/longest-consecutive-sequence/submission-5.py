class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put everything in the set
        # only start counting if the number is the begining of the sequence

        numbers = set(nums)
        max = 0
        for num in numbers:
            if num - 1 not in numbers:
                sequence = num
                length = 1
                while sequence + 1 in numbers:
                    length += 1
                    sequence += 1
                if length > max:
                    max = length
        
        return max