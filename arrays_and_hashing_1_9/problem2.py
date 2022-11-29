"""
Neetcode: #2
Leetcode: #242

URL: https://leetcode.com/problems/valid-anagram/

Title: Valid Anagram

Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
import unittest


class Solution:

    def validAnagram(self, s, t):
        """
        Trying to find if t is an anagram of s. This means that t and s have the same # of the same
        characters. To check we will create a dictionary for each, mapping the number of characters
        to the particular character key. The number of a particular character will be increased as
        duplicate characters are found.
        """
        mapS = {}
        mapT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0)
            mapT[t[i]] = mapT.get(t[i], 0)

        if mapS == mapT:
            return True

        return False


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(s.validAnagram("anagram", "nagaram"), True)

    def test2(self):
        s = Solution()
        self.assertEqual(s.validAnagram("rat", "car"), False)


if __name__ == '__main__':
    unittest.main()
