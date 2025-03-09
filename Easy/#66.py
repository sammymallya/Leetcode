#problem 66 leetcode:Plus One
#problem link: https://leetcode.com/problems/plus-one/
#time complexity: O(n) as each conversion step takes one bit or digit at a time so the max time cmplexity is O(n)
#space complexity:O(n) as each step created new strings and int , and each storage takes O(n) so 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #ans=[]
        return  list(map(int,str(int("".join(map(str,digits))) +1)))
        """ans=list(map(int,l))
        return ans"""
            
        