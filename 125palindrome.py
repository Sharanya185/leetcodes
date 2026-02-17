#Given a string determine if its palindrome considering only the alphanumerics values and ignoring the cases
# Solution using the 2 pointer approach


class Solution:
    def palindrome(self,s):
        left=0   
        right=len(s)-1
        while left<right:
           while left<right and not s[left].isalnum():
              left+=1
           while left<right and not s[right].isalnum():
              right-=1
           if s[left].lower()!=s[right].lower():
              return False
           left+=1
           right-=1
        return True
s="A man,a plan,a canal:Panama"
obj=Solution()
res=obj.palindrome(s)
print(res)
            