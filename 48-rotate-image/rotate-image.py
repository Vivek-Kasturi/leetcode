class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        #layer by layer
        for layer in range(n//2):
            first=layer
            last=n-1-layer
            for i in range(first, last):
                offset = i-first
                top=matrix[first][i] #saving top
                matrix[first][i] = matrix[last - offset][first] #left to top
                matrix[last - offset][first] = matrix[last][last - offset] #bottom to left
                matrix[last][last - offset] = matrix[i][last] #right to bottom
                matrix[i][last] = top #top to right
        