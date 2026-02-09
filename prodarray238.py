# PRODUCT EXCEPT SELF
def productExceptSelf(nums):
    n=len(nums)                 # lenth of array
    answer=[1]*n                # crete answer array filled with [1,1,1,1]
    prefix=1
    for i in range(n):
        answer[i]=prefix         
        prefix*=nums[i]          # update prefix by multiplying current number 
    suffix=1
    for i in range(n-1,-1,-1):
        answer[i]*=suffix
        suffix*=nums[i]
    return answer
print(" product is %d",productExceptSelf([2,3,6]))