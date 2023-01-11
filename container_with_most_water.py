class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea, idx1, idx2 = 0, 0, len(height) - 1
        while idx1 < idx2:
            base = abs(idx1 - idx2)
            currentArea = base * min(height[idx1], height[idx2])
            maximumArea = max(currentArea, maximumArea)
            if height[idx1] > height[idx2]:
                idx2 -= 1 
            else:
                idx1 += 1
        return maximumArea
