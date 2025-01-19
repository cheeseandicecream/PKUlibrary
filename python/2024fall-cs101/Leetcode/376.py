class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==2:
            if nums[0]==nums[1]:
                return 1
            return 2
        i = 1
        while i < len(nums) -1:
            if nums[i-1]>=nums[i]>=nums[i+1] or nums[i-1]<=nums[i]<=nums[i+1] :
                del nums[i]
                continue
            i+=1
        if nums[0]==nums[1]:
                return 1
        return len(nums)