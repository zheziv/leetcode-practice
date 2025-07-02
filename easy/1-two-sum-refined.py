class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # Use a dictionary to store numbers and their indices
        # dict is the equivalent of a hashmap in other languages like Java
        for i, num in enumerate(nums):
            # target = complement + num
            # Solved as complement = target - num
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            # If not found, store the current num and its index
            num_map[num] = i
