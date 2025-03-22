# #1356: Sort Integers by The Number of 1 Bits
link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=company&envId=jpmorgan&favoriteSlug=jpmorgan-three-months
## Explanation
The `sortByBits` function sorts an array of integers based on the number of 1-bits in their binary representation. If two numbers have the same number of 1-bits, they are sorted by their value.
### Approach
1. **Counting 1-bits Efficiently**:
   - The `count_ones` function uses bitwise operations to count the number of 1-bits in an integer. This is efficient because it reduces the number of bits to be checked in each iteration.
2. **Dictionary for Caching**:
   - A dictionary `dic` is used to store the count of 1-bits for each number in the array. This avoids recalculating the count for the same number multiple times, improving efficiency.
3. **Sorting**:
   - The array is first sorted using Python's built-in `sorted` function with a custom key that sorts based on the number of 1-bits.
   - A nested loop is then used to ensure that numbers with the same number of 1-bits are sorted by their value.
### Efficiency Highlights
- **Bitwise Operations**: Using `x &= x - 1` to count 1-bits is a well-known efficient technique.
- **Caching with Dictionary**: Storing the 1-bit counts in a dictionary reduces redundant calculations.
- **Custom Sorting**: Leveraging Python's efficient sorting algorithms with a custom key function.
Overall, the approach balances readability and efficiency by using bitwise operations and caching results.