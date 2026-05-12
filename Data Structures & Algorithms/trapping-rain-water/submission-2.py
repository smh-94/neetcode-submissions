class Solution:
    def trap(self, height: List[int]) -> int:
        #edge case
        if not height:
            return 0
        suum = 0
        #additional vars to track the max height of a pool of water
        maxL = height[0]
        maxR = height[-1]
        l = 0
        r = len(height)-1

        while l < r:
            #increment left if left is smaller
            if maxL < maxR:
                l+=1
                #update max height
                maxL = max(maxL, height[l])
                #calculate water that is trapped
                suum += maxL - height[l]
            else:
                #same as above but from the right
                r-=1
                maxR = max(maxR,height[r])
                suum += maxR - height[r]

        return suum