import unittest
from leetcode.algorithms.p0218_the_skyline_problem \
    import Solution


class TestTheSkylineProblem(unittest.TestCase):
    def test_the_skyline_problem(self):
        solution = Solution()
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                     [15, 20, 10], [19, 24, 8]]
        skyline = [[2, 10], [3, 15], [7, 12], [12, 0],
                   [15, 10], [20, 8], [24, 0]]

        self.assertListEqual(skyline, solution.getSkyline(buildings))
