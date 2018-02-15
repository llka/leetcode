"""
https://leetcode.com/problems/arithmetic-slices/description/
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        if n < 3:
            return 0
        slices = 0
        curDslices = 0
        for i in range(0, n - 2):
            d1 = A[i + 1] - A[i]
            d2 = A[i + 2] - A[i + 1]
            if d1 == d2:
                curDslices = curDslices + 1
                slices = slices + curDslices
            else:
                curDslices = 0
        return slices
