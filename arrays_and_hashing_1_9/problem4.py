"""
Neetcode: #4
Leetcode: #49

URL: https://leetcode.com/problems/group-anagrams/

Title: Group Anagrams
"""

from typing import List
import unittest
import collections


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Each anagram can be thought of as a unique combination of frequencies 
        of letters (ASCII values). For each string in the input array, there
        are two choices: use the sorted string as a key for a dictionary of
        lists where each anagram is in the same list OR use a frequency array
        of size 26 to compare the character frequencies of each string.
        
        First option is O(mlog(m)) * O(n) where m is the number of letters in 
        each string and n is the number of strings.
        
        2nd option is O(m) * O(n) where m is the number of letters in 
        each string and n is the number of strings."""

        # First option

        d = collections.defaultdict(list)
        
        for s in strs:

            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            d[tuple(freq)].append(s)
        return list(d.values())


        # # Second option
        #
        # d = collections.defaultdict(list)
        #
        # for s in strs:
        #     r = sorted(s)
        #     s = ''.join(r)
        #     d[sorted].append(s)
        #
        # return d.values()


class Test(unittest.TestCase):
    """
    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Example 2:
    
    Input: strs = [""]
    Output: [[""]]
    
    Example 3:
    
    Input: strs = ["a"]
    Output: [["a"]]
    """

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
                         self.sol.groupAnagrams(
                             ["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == '__main__':
    unittest.main()
