class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_ind = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in num_ind:
                return [num_ind[comp],i]
            num_ind[num] = i