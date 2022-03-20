import unittest
import sorting


class BubbleSortTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sorting = sorting.Sorting()

    def test_sort_empty_list(self):
        self.assertEqual([], self.sorting.bubble_sort([]))

    def test_sort_list_with_a_single_value(self):
        self.assertEqual([1], self.sorting.bubble_sort([1]))

    def test_sort_numeric_list(self):
        self.assertEqual([1, 2, 3], self.sorting.bubble_sort([2, 3, 1]))

    def test_sort_non_unique_list(self):
        self.assertEqual([0, 1, 2, 2, 3, 4, 5, 5], self.sorting.bubble_sort([5, 2, 3, 4, 5, 1, 0, 2]))

    def test_sort_list_with_negative_values(self):
        self.assertEqual([-3, -1, 0, 0, 3, 4], self.sorting.bubble_sort([4, 0, 0, -1, -3, 3]))

    def test_sort_alphabetic_list(self):
        self.assertEqual(['A', 'Y', 'a', 'c', 'd', 'd'], self.sorting.bubble_sort(['Y', 'A', 'a', 'd', 'c', 'd']))

    def test_sort_floats(self):
        self.assertEqual([1E-30, 1E-5, 1, 1, 1, 1.001], self.sorting.bubble_sort([1.00, 1, 1.001, 1.000, 1E-5, 1E-30]))


if __name__ == '__main__':
    unittest.main()
