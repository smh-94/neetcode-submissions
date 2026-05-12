class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #treat the matrix as a one dimensional array.
        height = len(matrix)
        length = len(matrix[0])
        l = 0
        r = (height * length) - 1
        
        while l <= r:
            #needs to update mid before we check
            mid = (l + r) // 2
            mid_list = mid // length #should output correct row
            mid_point = mid % length #should output corect indice

            if  matrix[mid_list][mid_point] == target:
                return True
            elif matrix[mid_list][mid_point] < target:
                #moving the index over by 1 because we already checked it
                l = mid + 1
            else:
                r = mid - 1
        return False
