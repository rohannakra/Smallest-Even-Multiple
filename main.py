# https://leetcode.com/problems/smallest-even-multiple/

def smallest_even_multiple(n):
    return n if n % 2 == 0 else n*2

print(smallest_even_multiple(5))
print(smallest_even_multiple(6))

# -------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2
