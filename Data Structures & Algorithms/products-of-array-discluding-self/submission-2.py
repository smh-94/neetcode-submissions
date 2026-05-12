class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        temp = 1

        #left to right pass
        for i in range(len(nums)):
            res[i] *=  temp
            temp *=nums[i]
            #[1,2,3,4]
            #[1,1,2,6]

        #reset temp
        temp = 1

        #right to left pass
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * temp
            temp *= nums[i]
        return res
