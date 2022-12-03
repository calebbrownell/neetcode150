"""
Neetcode: #5
Leetcode: #347

URL: https://leetcode.com/problems/top-k-frequent-elements/

Title: Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.
"""
import unittest
from typing import List

from collections import deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for i in range(0, len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            l = freq[c]
            l.append(n)
            freq[c] = l

        res = []
        for c in range(len(nums), 0, -1):
            for n in freq[c]:
                res.append(n)
                if len(res) == k:
                    return res




class Test(unittest.TestCase):

    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test2(self):
        self.assertEqual(self.sol.topKFrequent([1], 1), [1])

if __name__ == "__main__":
    unittest.main()