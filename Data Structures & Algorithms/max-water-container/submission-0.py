class Solution:
    def maxArea(self, heights: List[int]) -> int:


        start = 0
        end = len(heights) - 1

        max_area = 0 # This will filter negative values. 

        while start < end:
            area = 0
            width = end - start
       

            if heights[start] < heights[end]:
                area = heights[start] * width
                start += 1
            elif heights[start] > heights[end]:
                area = heights[end] * width
                end -= 1
            else:
                area = heights[start] * width    
                start += 1   

            print(area)    

            if max_area < area:
                max_area = area

        return max_area            

        