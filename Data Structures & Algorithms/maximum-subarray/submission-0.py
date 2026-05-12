class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        #list splicing, we already use the first index 
        #so 1: means start a new list beginning at index 1
        for x in nums[1:]:
            #take the higher sum between x and current sum
            curSum = max(x, curSum + x)
            #return the larger sum of the two
            maxSum = max(maxSum, curSum)

        return maxSum