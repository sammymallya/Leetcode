#Tags: Easy, Sliding_Window

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             if abs(i-j)<=k:
        #                 return True
        # return False
        num_indices={}
        for i,num in enumerate(nums):
            if num in num_indices and abs(i-num_indices[num] <=k):
                return True
            num_indices[num]=i #update last seen index
        return False
        