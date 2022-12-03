"""
Neetcode: #7
Leetcode: #36

URL: https://leetcode.com/problems/valid-sudoku/

Title: 36. Valid Sudoku
"""
import unittest
from typing import List
import collections


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Need to check 3 things, row, column, box
        :param board:
        :return:
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):

            for c in range(len(board)):

                if board[r][c] == ".":
                    continue

                if (
                        board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


class Test(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                                    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]), True)

    def test2(self):
        self.assertEqual(self.sol.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                                    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]), False)


if __name__ == "__main__":
    unittest.main()
