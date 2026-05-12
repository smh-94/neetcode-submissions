class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n #we default to 0 because we are going backwards
        stack = [] #to store indices

        #move backwards through the array
        for i in range(n-1,-1,-1):
            # Pop indices with temperatures less than or equal to current
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i #next warmer day index difference

            stack.append(i)
        return res