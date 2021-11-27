class Solution:
    def trap(self, height: List[int]) -> int:
        counter = 0 // calculate nu of pits to trap water
        diff = 0
        for i in range(1,len(height) - 1): 
            if height[i] < height[i - 1]: // if current is  greater than previous  dont go further 
                maxi = max(height[i + 1:]) // find the max in the list form current + 1
                mini = min(height[i - 1],maxi) // Compare current and max
                if height[i] > mini: // if current is greater than mini don't go further
                    continue
                diff = mini - height[i] // else find diff bet mini and current 
                counter = counter + diff // add pit  gadda 
                height[i] = height[i] + diff //set current to fully filled then need not to check to right
        return counter
