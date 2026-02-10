#given 2 sorted arrays
#merge them


class Solution:
    def merge(self,num1,m,num2,n):
        i=m-1      #pointer to num1
        j=n-1      # pointer to num2
        k=m+n-1     #pointer toend of num1
        
        while i>=0 and j>=0:
            if num1[i]>num2[j]:
                num1[k]=num1[i]
                i-=1
            else:
                num1[k]=num2[j]
                j-=1
            k-=1

        while j>=0:
            num1[k]=num2[j]
            j-=1
            k-=1
        return num1

num1=[1,2,3,0,0,0]   
num2=[4,5,6]
m=3
n=3
obj=Solution()
obj.merge(num1,m,num2,n)
print(num1)