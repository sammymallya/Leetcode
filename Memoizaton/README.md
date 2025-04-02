# Memoization Problems - LeetCode

This folder contains solutions to LeetCode problems using **memoization** and other optimization techniques. Each problem is briefly explained with its approach to help with quick recall.

---

## [#70 Climbing Stairs](#70_climbing_stairs.py)

**Problem:** Given `n` stairs, you can climb 1 or 2 steps at a time. Find the total number of ways to reach the top.

**THought Process** On trying a few iterations out, We see that the sequence looks very similar to fibonacci sequence except that n=0 and n=1 return 1. 
so we use the same approach here
### **Approaches:**
1. **Memoization:**
   - Use recursion with a `memo` array to store previously computed results.
   - so that when we are calculating higher values, we reduce redundancy.
   - Reduces redundant calculations, making it **O(n) space complexity** and **O(n) time complexity**.
   
2. **State Optimization:**
   - Instead of storing all previous states, use two variables to track the last two computed values.
   - Optimizes space complexity from **O(n) to O(1)** while maintaining **O(n) time complexity**.

[Click to go to problem](https://leetcode.com/problems/climbing-stairs/submissions/1593912093/?envType=problem-list-v2&envId=memoization)

---

More problems will be added soon!

