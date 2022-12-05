"""
Description
"""
from typing import List
import unittest


class Solution:

    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, 1
        while r < len(height):
            if height[r] >= height[l]:
                area += water
                water = 0
                l = r
                r += 1
            elif height[r] < height[l]:
                water += height[r] - height[l]
                r += 1


class Test(unittest.TestCase):
    sol = Solution()

    def test1(self):
        """
        
        """
        self.assertEqual(6, self.sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

    def test2(self):
        """

        """
        pass

    def test3(self):
        """

        """
        pass
