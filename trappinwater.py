class Solution:
    def trap(self, height: List[int]) -> int:
        counter = 0
        diff = 0
        for i in range(1,len(height) - 1): 
            if height[i] < height[i - 1]:
                maxi = max(height[i + 1:])
                mini = min(height[i - 1],maxi)
                if height[i] > mini:
                    continue
                diff = mini - height[i]
                counter = counter + diff
                height[i] = height[i] + diff
        return counter
