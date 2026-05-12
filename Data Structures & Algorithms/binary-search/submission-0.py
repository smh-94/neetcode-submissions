class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l != r:
            #[1,2,3,4,5,6,7]
            #target = 3
            #[4] > 3
            #2 < 3
            if nums[(l + r) // 2] is target:
                return ((l+r) // 2)
            elif nums[(l+r)//2] > target:
                r = (l+r) // 2
            elif nums[(l+r) // 2] < target:
                l = (l + r) // 2 + 1
        return -1