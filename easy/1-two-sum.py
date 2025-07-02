# It's a wrong example because it only + the value next to it.
# Such as nums = [3,2,3] will be wrong.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1] == target):
                return [i, i + 1]
