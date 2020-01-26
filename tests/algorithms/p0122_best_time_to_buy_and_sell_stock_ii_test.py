import unittest
from leetcode.algorithms.p0122_best_time_to_buy_and_sell_stock_ii \
    import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        solution = Solution()

        self.assertEqual(7, solution.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, solution.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, solution.maxProfit([7, 6, 4, 3, 1]))
