# search in Rotated sorted array



def search(nums,target):
    l,r=0,nums[len]-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        if nums[l]<=nums[m]:
            if nums[l]<=target<nums[m]:
                r=m-1
            else:
                l=m+1
        else:
            if nums[m]<target<=nums[r]:
                l=m+1
            else:
                r=m-1
    return -1
nums=[15,18,2,3,6,12]
target=3
search(nums,target)
