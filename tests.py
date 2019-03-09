import unittest
from lama import change, change_tiles_normal, change_tiles_special, construct_str, check_solved


class LightOutTest(unittest.TestCase):
    def test_change(self):
        self.assertEqual([[0]], change([[1]], (0, 0)))
        self.assertEqual([[1]], change([[0]], (0, 0)))
        self.assertEqual([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],
                         change([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],
                                (2, 3)))

    def test_change_tiles_normal(self):
        simple_changes = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        simple_changes2 = [[1, 1, 1], [1, 0, 1], [1, 1, 0]]
        simple_changes3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        complex_changes = [[1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]

        self.assertEqual([[0, 0, 1], [0, 1, 1], [1, 1, 1]], change_tiles_normal(simple_changes, (0, 0)),
                         "Error at changing the upper-left corner tile")
        self.assertEqual([[0, 1, 0], [0, 1, 0], [1, 1, 1]], change_tiles_normal(simple_changes, (0, 2)),
                         "Error at changing the upper-right corner tile")
        self.assertEqual([[0, 1, 0], [1, 1, 0], [0, 0, 1]], change_tiles_normal(simple_changes, (2, 0)),
                         "Error at changing the lower-left corner tile")
        self.assertEqual([[0, 1, 0], [1, 1, 1], [0, 1, 0]], change_tiles_normal(simple_changes, (2, 2)),
                         "Error at changing the lower-right corner tile")
        self.assertEqual([[1, 0, 1], [0, 1, 0], [1, 0, 0]], change_tiles_normal(simple_changes2, (1, 1)),
                         "Error at changing a surrounded tile")
        self.assertEqual([[0, 0, 0], [1, 0, 1], [1, 1, 1]], change_tiles_normal(simple_changes3, (0, 1)),
                         "Error at changing a top-side verge-tile")
        self.assertEqual([[0, 0, 0], [1, 1, 1], [0, 0, 0]], change_tiles_normal(simple_changes3, (2, 1)),
                         "Error at changing a bottom-side verge-tile")
        self.assertEqual([[1, 0, 0], [0, 0, 1], [1, 0, 0]], change_tiles_normal(simple_changes3, (1, 0)),
                         "Error at changing a left-side verge-tile")
        self.assertEqual([[1, 0, 1], [0, 1, 0], [1, 0, 1]], change_tiles_normal(simple_changes3, (1, 2)),
                         "Error at changing a right-side verge-tile")
        self.assertEqual(complex_changes, change_tiles_normal(
            [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]], (2, 3)),
                         "Error at changing a surrounded tile")

    def test_change_tiles_special(self):
        special_changes = [[1, 0, 0], [0, 0, 1], [1, 0, 1]]

        self.assertEqual([[0, 1, 1], [1, 1, 0], [1, 0, 1]], change_tiles_special(special_changes, (1, 2)),
                         "Error at special-change")

    def test_construct_str(self):
        self.assertEqual("0", construct_str([[0]]))
        self.assertEqual("1", construct_str([[1]]))
        self.assertEqual("1 0 1\n1 1 0\n0 0 0", construct_str([[1, 0, 1], [1, 1, 0], [0, 0, 0]]))
        self.assertEqual("1 0 0 0 0\n0 1 0 0 0\n0 0 1 0 0\n0 0 0 1 0\n0 0 0 0 1", construct_str(
            [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))

    def test_check_won(self):
        simple_won = [[0]]
        simple_lost = [[1]]
        complex_won = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        complex_lost = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

        self.assertEqual(True, check_solved(simple_won))
        self.assertEqual(False, check_solved(simple_lost))
        self.assertEqual(True, check_solved(complex_won))
        self.assertEqual(False, check_solved(complex_lost))


if __name__ == '__main__':
    unittest.main()
