class Solution:
    def groupanagram(self,str):
        hashmap={}
        for word in str:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1

            key=tuple(count)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(word)
        return list(hashmap.values())
str=["eat","tea","bat","tab","hy","wow"]
obj=Solution()
res=obj.groupanagram(str)
print(res)