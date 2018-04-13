import unittest

import cube
from utils import Point, Triangle


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
        nw = Point(-20, 1, 19)
        se = Point(18, 1, -17)
        ne = Point(se.x, se.y, nw.z)
        sw = Point(nw.x, nw.y, se.z)

        results = cube.generate_rect_triangles(nw, ne, sw, se)
        expected1 = Triangle(nw, sw, se)
        expected2 = Triangle(nw, se, ne)
        self.assertEqual(results[0], expected1)
        self.assertEqual(results[1], expected2)

    def test_cube_trianges(self):
        high = Point(-20, 16, 19)
        low = Point(18, -15, -17)

        results = cube.generate_cube_trianges(high, low)
        self.assertEqual(len(results), )


        self.assertFalse(True)
