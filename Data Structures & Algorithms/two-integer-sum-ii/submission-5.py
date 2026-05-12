class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force solution#
        #length equal to length of incoming lsit
        length = len(numbers)
        #first pointer is going from 0 to (n-1)
        for i in range(length-1):
            #second pointer is going from 1 to (n)
            for j in range(i+1, length):
                #check if first pointer plus second pointer is equal to the target
                if (numbers[i] + numbers[j] == target):
                    #return first and second index PLUS 1 because it's 1 based index
                    return [i+1,j+1]