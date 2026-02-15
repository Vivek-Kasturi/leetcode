class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        target = n * n
        
        while num <= target:
            # 1. Left -> Right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # 2. Top -> Bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # 3. Right -> Left
            if top <= bottom:
                for j in range(right, left - 1, -1):   # FIXED: backward loop
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            
            # 4. Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):   # FIXED: upward loop
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
