import unittest
from leetcode.algorithms.p0200_number_of_islands_2 import Solution


class TestNumberOfIslands(unittest.TestCase):
    def test_number_of_islands(self):
        solution = Solution()
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]

        self.assertEqual(3, solution.numIslands(grid))
