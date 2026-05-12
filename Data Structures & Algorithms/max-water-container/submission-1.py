class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0
        l = 0
        r = len(heights)-1

        while l < r:
            curMax = min(heights[l],heights[r]) * (r-l)
            if curMax > sol:
                sol = curMax
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                r -= 1
        return sol