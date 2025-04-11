#Tags: Medium, Prefix_Sum
#problem link: https://leetcode.com/problems/contiguous-array/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum={0:-1}  #sum:index
        sums=0
        max_l=0
        for i,n in enumerate(nums):
            if n:
                sums+=1
            else:
                sums+=-1
            if sums in presum:
                max_l=max(max_l, i- presum[sums])
            else:
                presum[sums]=i
            return max_l

