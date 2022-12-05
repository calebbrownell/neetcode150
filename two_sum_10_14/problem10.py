"""
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

import unittest
from typing import List


class Solution:

    def isPalindrome(self, s: str) -> bool:
        word = self.lowercaseAlphaNumericOnly(s)

        if len(word) < 2:
            return True

        l, r = 0, len(word) - 1
        while r > l:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

    def lowercaseAlphaNumericOnly(self, s: str) -> str:
        res = []
        for c in s:
            if ((ord('a') <= ord(c) <= ord('z')) or
                    (ord('A') <= ord(c) <= ord('Z')) or
                    (ord('0') <= ord(c) <= ord('9'))):
                res.append(c)

        res = ''.join(res)
        return res.lower()


class Test(unittest.TestCase):
    sol = Solution()

    def test_lowercaseAlphaNumericOnly(self):
        self.assertEqual("amanaplanacanalpanama", self.sol.lowercaseAlphaNumericOnly("A man, a plan, a canal: Panama"))

    def test_isPalindrome_short(self):
        self.assertEqual(True, self.sol.isPalindrome("a"))

    def test_isPalindrome(self):
        self.assertEqual(False, self.sol.isPalindrome("abc"))
        self.assertEqual(True, self.sol.isPalindrome("A man, a plan, a canal: Panama"))
