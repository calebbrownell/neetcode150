"""
Neetcode: #8
Leetcode: #271

URL: https://leetcode.com/problems/encode-and-decode-strings/

Title: 271 Encode and Decode Strings
"""
import unittest
from typing import List


class Codec:
    @staticmethod
    def encode(strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        encoded = chr(257).join(strs)
        return encoded

    @staticmethod
    def decode(s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        decoded = s.split(chr(257))
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Test(unittest.TestCase):
    sol = Codec()

    def test1(self):
        strs = ["abc", "def" "ghi"]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test2(self):
        strs = [""]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)
