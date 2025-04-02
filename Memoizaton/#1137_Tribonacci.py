#using memoization
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        if n==2:
            return 1
        memo=[-1]*(n+1)
        memo[0],memo[1],memo[2]=0,1,1
        def mem(n):
            if memo[n]!=-1:
                return memo[n]
            memo[n]=mem(n-1)+mem(n-2)+mem(n-3)
            return memo[n]
        return mem(n)
#-----------------------------------------------------------
#using state space
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=1:
            return n
        if n==2:
            return 1
        a,b,c=0,1,1
        for _ in range(3,n+1):
            a,b,c=b,c,a+b+c
        return c
        
        
