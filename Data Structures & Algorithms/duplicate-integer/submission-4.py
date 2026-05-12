class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we check if the length of nums' set is equal to the length of nums
        return len(set(nums)) != len(nums)