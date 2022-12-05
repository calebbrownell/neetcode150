"""
Description
"""
from typing import List
import unittest


class Solution:

    def maxArea(self, height: List[int]) -> int:
        # area = width * height
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l+=1
            elif height[r] < height[l]:
                r-=1
        return maxArea




class Test(unittest.TestCase):
    sol = Solution()

    def test1(self):
        """
        
        """
        self.assertEqual(49, self.sol.maxArea([1,8,6,2,5,4,8,3,7]))

    def test2(self):
        """

        """
        self.assertEqual(24, self.sol.maxArea([1,3,2,5,25,24,5]))


    def test3(self):
        """

        """
        pass
