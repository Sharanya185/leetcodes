# check whether the given strings are valid anagrams

class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        count=[0]*26     # to storethe counts of a to z
        for i in range (len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1

        for c in count:
            if c!=0:
                return False
            
        return True
s="car"
t="rat"
obj=Solution()
res=obj.isAnagram(s,t)
print(res)
