#Tags: Easy
#problem link:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(str(x)[::-1]!= str(x)):
            return False
        return True
        