class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n+1)
        for i in range(n + 1):
            lsb = i
            for j in range (32):
                if lsb & 1 == 1:
                    count[i] += 1
                lsb >>= 1
        
        return count
