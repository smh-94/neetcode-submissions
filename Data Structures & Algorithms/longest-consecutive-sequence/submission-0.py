class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set conversion is O(n)
        numSet = set(nums)
        #track longest sequence
        longest = 0

        for x in nums:
            #check if x is the start of a sequence
            if (x-1) not in numSet:
                #reset when x is a new sequence
                length = 0
                #check if current num is in set
                while (x+length) in numSet:
                    #as length grows we check if consecutive nums in set
                    length += 1
                longest = max (length, longest)
        return longest