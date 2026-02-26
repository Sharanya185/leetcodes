class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] == 0:
                # Shift elements to the right
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]

                # Insert duplicated zero ONLY if index is valid
                if i + 1 < n:
                    arr[i + 1] = 0

                i += 2   # Skip the duplicated zero
            else:
                i += 1
arr=[1,0,2,3,0,4,5]
obj=Solution()
obj.duplicateZeros(arr)
print(arr)