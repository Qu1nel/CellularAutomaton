import unittest

from src.game.cell import Cell


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cell1 = Cell(coord=(5, 4))
        self.cell2 = Cell(coord=(4, 5), alive=True)

    def test_cell_is_dead(self) -> None:
        """Checking if the cell is dead"""
        self.assertFalse(self.cell1.alive)

    def test_cell_is_alive(self) -> None:
        """Checking if the cell is live"""
        self.assertTrue(self.cell2.alive)

    def test_get_coord(self) -> None:
        """Case getting coord from cell"""
        self.assertEqual(self.cell1.coord, (5, 4))
        self.assertEqual(self.cell2.coord, (4, 5))

        self.assertIsInstance(self.cell1.coord, tuple)
        self.assertIsInstance(self.cell2.coord, tuple)

        self.assertIsNot(self.cell1.copy(), self.cell1)
        self.assertIsNot(self.cell1.copy(), self.cell1.copy())

    def test_str_cell(self) -> None:
        """Case check str cell"""
        self.assertIsInstance(str(self.cell1), type(str(self.cell2)))


if __name__ == '__main__':
    unittest.main()
