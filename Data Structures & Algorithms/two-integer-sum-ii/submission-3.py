class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers on each end and increment/decrement based on if the sum is bigger/ smaller than the target

        ptr_1 = 0
        ptr_2 = len(numbers) - 1

        while ptr_1 < ptr_2:
            if numbers[ptr_1] + numbers[ptr_2] == target:
                return [ptr_1+1, ptr_2+1]
            elif numbers[ptr_1] + numbers[ptr_2] > target:
                ptr_2 -= 1
            else:
                ptr_1 += 1
            