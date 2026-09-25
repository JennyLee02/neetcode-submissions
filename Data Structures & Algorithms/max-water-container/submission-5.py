class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1
        maxArea = 0

        while low < high:
            area = min(heights[low], heights[high]) * (high - low)
            if area > maxArea:
                maxArea = area
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return maxArea