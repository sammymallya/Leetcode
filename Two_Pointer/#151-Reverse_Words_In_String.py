#Tags: Medium, Two_Pointer
#problem : #151- Reverse Words in a String, link= https://leetcode.com/problems/reverse-words-in-a-string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        ans=' '.join(s[::-1])
        return ans
        