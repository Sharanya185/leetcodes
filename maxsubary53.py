def maxSubArray(nums):
    max_sum = nums[0]        # best sum found so far
    current_sum = nums[0]    # best sum ending at current index

    for i in range(1, len(nums)):
        # either start fresh from nums[i] or extend the previous subarray
        current_sum = max(nums[i], current_sum + nums[i])
        # update global maximum
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))   # Output: 6