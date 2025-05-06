#Tags: Medium, Two_Pointer
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        right=n-1
        left=0
        area=[]
        while left <=right:
            area.append(min(height[left],height[right])*(right-left))
            if height[left] <height[right]:
                left+=1
            else:
                right-=1
        return max(area)
        