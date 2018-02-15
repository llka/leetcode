"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

    Input: 16
    Returns: True
Example 2:

    Input: 14
    Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        low = 1;
        high = num;
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
        """
        :type num: int
        :rtype: bool
        """
