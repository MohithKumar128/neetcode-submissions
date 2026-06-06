class Solution:
        def maxArea(self, heights: List[int]) -> int:
                left=0
                right=len(heights)-1
                max_area=0
                while(left<right):
                        area=abs(left-right)*min(heights[left],heights[right])
                        if area>max_area:
                                max_area=area
                                
                        else:
                             if heights[left]<heights[right]:
                                left+=1
                             else:
                                right-=1
                return max_area


                