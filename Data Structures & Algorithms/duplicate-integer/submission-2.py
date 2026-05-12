class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for x in nums:
            if x not in res:
                res.add(x)
            else:
                return True
        return False