class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target not in nums:
                return -1
            elif num==target:
                return i
        