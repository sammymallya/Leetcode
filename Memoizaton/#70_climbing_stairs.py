#code using memoization:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        memo=[-1]*(n+1)
        memo[0],memo[1]=1,1
        def fib(n):
            if memo[n]!=-1:
                return memo[n]
            memo[n]=fib(n-1)+fib(n-2)
            return memo[n]
        return fib(n)

#-----------------------------------------------------------
#code using state optimization:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=1:
            return 1
        a,b=1,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b
