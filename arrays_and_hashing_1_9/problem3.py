"""
Neetcode: #3
Leetcode: #1

URL: https://leetcode.com/problems/two-sum/

Title: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""
import unittest
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Since we are looking for a combination of two numbers, we are looking for corresponding
        matches. We can use a lookup map to store the matches for future recall.
        """

        matches = {}
        for i,n in enumerate(nums):
            diff = target - n
        
            if diff in matches:
                return [matches[diff], i]
            else:
                matches[n] = i
                




class Test(unittest.TestCase):
    """
    Example 1:
    
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:
    
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
    Example 3:
    
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    def setUp(self):
        self.sol = Solution()
        
    def test1(self):
        self.assertEqual(self.sol.twoSum([2,7,11,15], 9), [0,1])

    def test2(self):
        self.assertEqual(self.sol.twoSum([3,2,4], 6), [1,2])

    def test3(self):
        self.assertEqual(self.sol.twoSum([3,3], 6), [0,1])


if __name__ == '__main__':
    unittest.main()
