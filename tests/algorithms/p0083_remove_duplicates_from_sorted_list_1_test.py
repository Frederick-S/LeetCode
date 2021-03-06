import unittest
from leetcode.algorithms.p0083_remove_duplicates_from_sorted_list_1 \
    import Solution, ListNode
from .list_helper import convert_linked_list_to_list


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    def test_remove_duplicates_from_sorted_list(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(1)
        c = ListNode(2)
        d = ListNode(3)
        e = ListNode(3)
        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertListEqual(
            [1, 2, 3],
            convert_linked_list_to_list(solution.deleteDuplicates(a)))
