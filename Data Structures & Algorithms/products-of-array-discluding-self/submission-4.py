class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            j = -i -1
            prefix[i] = left
            suffix[j] = right
            left *= nums[i]
            right *= nums[j]
        
        return [l*r for l, r in zip(prefix, suffix)]