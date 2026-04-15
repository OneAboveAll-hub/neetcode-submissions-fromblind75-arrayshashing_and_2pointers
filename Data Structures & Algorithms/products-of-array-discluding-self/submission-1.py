class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np
        i = 0
        new_list = []
        for i in range(len(nums)):
            new_list.append( np.prod(np.delete(nums,i),dtype=int) if nums[i] == 0 else np.prod(nums,dtype=int)//nums[i])

        return new_list