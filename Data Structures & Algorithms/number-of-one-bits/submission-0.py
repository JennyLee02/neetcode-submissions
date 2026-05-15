class Solution:
    def hammingWeight(self, n: int) -> int:
        # AND operation on the LSB and shift right
        count = 0
        for i in range (32):
            if n & 1 == 1:
                count+=1
            n >>= 1
        
        return count
        