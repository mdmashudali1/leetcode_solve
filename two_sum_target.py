class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # Dictionary to store numbers and their indices
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index  # Store index of the current number
        
        return []  # Return empty list if no solution is found

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]