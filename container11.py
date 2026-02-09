# conatiner with most water

class Solution:
    def maxarea(self,height:list[int])->int:
        left,right=0,len(height)-1
        max_area=0
        while left<right:
            width=right-left
            current_height=min(height[left],heigt[right])
            area=width*current_height
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area

