class Solution:
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l = 0
            r = len(row)-1

            if(row[r] < target):
                continue
            
            while(l <= r):
                mid = l+(r-l)//2
                if(row[mid] == target):
                    return True
                if(row[mid] < target):
                    l = mid+1
                else:
                    r = mid-1
        return False
        