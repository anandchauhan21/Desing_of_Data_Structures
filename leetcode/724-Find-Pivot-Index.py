class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l_t = 0
        for i in range(len(nums)):
            r_t = t - l_t - nums[i]
            if r_t == l_t:
                return i
            l_t += nums[i]
        return -1
