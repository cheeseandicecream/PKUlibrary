class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        def spin(matrix,ans,x,y):
            if x >= m//2 and y >= n//2:
                return ans
            for i in range(x,m-x):
                ans.append(matrix[y][i])
            for j in range(y+1,n-y):
                ans.append(matrix[j][m-x-1])
            for i in range(m-x-2,x-1,-1):
                ans.append(matrix[n-y-1][i])
            for j in range(n-y-2,y-1,-1):
                ans.append(matrix[j][x])
            spin(matrix,ans,x+1,y+1)
        spin(matrix, ans,0,0)
        return ans