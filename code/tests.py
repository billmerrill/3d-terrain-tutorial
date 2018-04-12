import unittest

import cube
from utils import *


class CubeTests(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, 1)

    def test_cube(self):
        n = Point(1, 2, 3)
        f = Point(10, 20, 30)

        expected_points = [
            (n.x, n.y, n.z),
            (f.x, n.y, n.z),
            (n.x, n.y, f.z),
            (f.x, n.y, f.z),
            (f.x, f.y, f.z),
            (n.x, f.y, f.z),
            (f.x, f.y, n.z),
            (f.x, f.y, f.z),
        ]

        results = cube.generate_cube_points(n, f)
        self.assertEqual(len(expected_points), len(results))
        for p in results:
            self.assertIn(p, expected_points)

    def test_rect_triangles(self):
        self.assertFalse(True)

    def test_cube_trianges(self):
        self.assertFalse(True)
