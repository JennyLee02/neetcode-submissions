class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers one each end
        # set max and update only when the maxArea changes
        # area = lower height of two * (high - low)

        low, high = 0, len(heights) - 1
        maxArea = 0
        for _ in range(len(heights)):
            area = min(heights[low], heights[high]) * (high - low)
            if area > maxArea:
                maxArea = area
            if heights[low] < heights[high]:
                low += 1
            elif heights[high] < heights[low]:
                high -= 1
            else:
                low += 1
        
        return maxArea
