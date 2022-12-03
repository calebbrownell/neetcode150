"""
Neetcode: #6
Leetcode: #238

URL: https://leetcode.com/problems/product-of-array-except-self/

Title: 238. Product of Array Except Self
"""
import unittest
from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


class Test(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.productExceptSelf([1, 2, 4, 8]), [64, 32, 16, 8])


if __name__ == "__main__":
    unittest.main()
