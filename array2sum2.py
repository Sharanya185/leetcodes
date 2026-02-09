# find 2 numbers in the array that add up to a specific target
#we are using brute force idea
#use 2loops to check all pairs that add up to target

def twosum(nums,target):
    seen={}                       #dict to store the number and its index
    for i,num in enumerate(nums):  # enumerate is used to get into the loops
        complement=target-num      #which num is needed to get target 
        if complement in seen:
            return [seen[complement],i] #found the pair
        seen[num]=i                     # if not found store the current index and the number for future use
    return []                             #if no soln is found
nums=[2,7,11,15]
target=18
result=twosum(nums,target)
print(result)
