class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndices = list()
        prev = dict()
        for i, x in enumerate(nums):
            diff = target - x
            if diff in prev:
                return [prev[diff],i]
            prev[x] = i