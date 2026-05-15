class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min and max speed
        left, right = 1, max(piles)
    
        while left < right:
            mid = (left + right) // 2
            hour = sum(math.ceil(p / mid) for p in piles)
            if hour > h:
                # Too slow: increase the speed
                left = mid + 1
            else:
                right = mid
            
        return right
