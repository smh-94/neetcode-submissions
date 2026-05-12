class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for x in nums:
            if x not in newSet:
                newSet.add(x)
            else:
                return True
        return False