'''
42. Trapping Rain Water
Solved
Hard
Topics
premium lock iconCompanies

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        l_m= height[l]
        r_m = height[r]
        w = 0

        while l < r:
            if l_m < r_m:
                l +=1
                l_m = max(l_m, height[l])
                w += l_m - height[l]
            else:
                r -= 1
                r_m = max(r_m, height[r])
                w+=r_m - height[r]
        return w
