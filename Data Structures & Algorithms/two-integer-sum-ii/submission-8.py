class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #linear solution
        #this uses O(1) space because there are no new arrays just two integers
        l = 0
        r = len(numbers)-1
        while l < r:
            #track current sum
            curSum = numbers[l] + numbers[r]
            #if current sum is greater than target lessen it by lowering right index by 1
            if curSum >target:
                r -= 1
            #if current sum is less than the target make it bigger by increasing left index by 1
            elif curSum < target:
                l += 1
            else:
            #we are guaranteed a solution by the question so we only need to return the solution's indices
                return [l+1,r+1]