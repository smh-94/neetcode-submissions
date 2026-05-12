class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            #early exit optimization
            if nums[l] < nums[r]:
                #min returns the minimum between two integers
                res = min(res, nums[l])
                break
            #normal midpoint calculation
            m = (l + r) // 2
            #takes the minimum between the mid and res before throwing away half the array
            res = min(res, nums[m])
            #updating pointers
            #we add / subtract one because we already checked that mid point.
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res