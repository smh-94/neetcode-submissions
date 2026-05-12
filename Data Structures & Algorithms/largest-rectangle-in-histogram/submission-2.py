class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Time Complexity: O(n)
        #   Each bar is pushed and popped from the stack at most once.
        #
        # Space Complexity: O(n)
        #   Stack can store up to n bars in the worst case.

        maxArea = 0

        # Monotonic increasing stack
        # Each element is a pair: (start_index, height)
        stack = []

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):

            # This will track how far left the current height can extend
            start = i

            # If the current height is smaller than the height at the top of the stack,
            # we can no longer extend rectangles with the taller height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # Calculate area using the popped height
                # Width = current index - starting index of that height
                maxArea = max(maxArea, height * (i - index))

                # Update start to the leftmost index of the popped bar
                start = index

            # Push the current bar with the earliest index it can extend to
            stack.append((start, h))

        # Process any remaining bars in the stack
        # These bars extend to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
