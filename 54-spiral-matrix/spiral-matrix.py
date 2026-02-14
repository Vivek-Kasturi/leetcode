class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1

        while top<=bottom and left<=right:
            #top row
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top+=1

            #right column
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1

            if top<=bottom:
                #travel bottom row
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -=1
            if left<=right:
                #travel left column
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res