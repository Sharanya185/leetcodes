# given n*n 2D matrix ,You have to rotate by 90 degree
# do not use new matrix


class Solution:
    def rotate(self,matrix):
        n=len(matrix)
        #transpose
        for i in range (n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #reverse
        for i in range(n):
            matrix[i].reverse()

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
obj=Solution()
obj.rotate(matrix)
print(matrix)
