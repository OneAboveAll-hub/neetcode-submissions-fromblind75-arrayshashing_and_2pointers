class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[-n:]+nums[:-n]
        return min(nums)