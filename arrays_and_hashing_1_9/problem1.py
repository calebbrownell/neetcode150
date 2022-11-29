# Neetcode #1
# Leetcode #217
# URL https://leetcode.com/problems/contains-duplicate/
# Title: Contains Duplicate
#Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:

#Input: nums = [1,2,3,1]
#Output: true
#Example 2:

#Input: nums = [1,2,3,4]
#Output: false
#Example 3:

#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true

from typing import List
import unittest


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False


class Test(unittest.TestCase):

    def test1(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(Solution().containsDuplicate(nums), True)

    def test2(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(Solution().containsDuplicate(nums), False)

    def test3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertEqual(Solution().containsDuplicate(nums), True)
