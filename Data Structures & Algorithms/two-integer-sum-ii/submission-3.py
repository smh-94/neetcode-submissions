class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #length equal to length of incoming lsit
        length = len(numbers)
        for i in range(length-1):
            for j in range(i+1, length):
                if (numbers[i] + numbers[j] == target):
                    return [i+1,j+1]