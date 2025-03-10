#20] valid parentheses problem:
#brute force approach
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        flag=0
        for i in s:
            if i in {'(','{','['}:
                stack.append(i)
                flag=1
            elif i in {')','}',']'} and len(stack)==0:
                return False
            else:
                if i==')':
                    if stack[-1]=='(':
                        flag=1
                        stack.pop(-1)
                    else:
                        return False
                elif i=='}':
                    if stack[-1]=='{':
                        flag=1
                        stack.pop(-1)
                    else:
                        return False
                elif i==']':
                    if stack[-1]=='[':
                        flag=1
                        stack.pop(-1)
                    else:
                        return False
        if stack==[] and flag==1:
            return True
        else:
            return False
""" in this approach ive first used a ton of if elses and conditions to rule out the edge cases.
this makes the approach inefficient. Instead of using so many if conditions i can use a dictionary to simplify
my solution"""     
#Dict approach:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict={')':'(', '}':'{', ']':'['}
        for i in s:
            if i in dict.values():
                stack.append(i)    
            elif i in dict.keys() and len(stack)==0:
                return False
            else:
                if i in dict.keys() and stack[-1]!= dict[i]:
                    return False
                else:
                    stack.pop(-1)
        if stack ==[]:
            return True
        else:
            return False    
                


                   

                


        