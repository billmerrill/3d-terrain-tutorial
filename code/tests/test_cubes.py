import unittest

from cube import Box, Rectangle
from utils import Point
from stl_canvas import STLCanvas


class RectangleTests(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, 1)

    def test_rectangle(self):
        nw = Point(-20, 1, 19)
        se = Point(18, 1, -17)
        ne = Point(se.x, se.y, nw.z)
        sw = Point(nw.x, nw.y, se.z)

        r1 = Rectangle(nw, sw, se, ne)
        results = r1.get_triangles()

        expected = [
            (nw, sw, se),
            (nw, se, ne),
        ]

        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[1], expected[1])

    def test_box(self):
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

        b1 = Box(n, f)
        results = b1.get_triangles()
        self.assertEqual(len(results), 12)

        self.assertIn((
            Point(f.x, f.y, f.z),
            Point(f.x, f.y, n.z),
            Point(n.x, f.y, f.z),
        ), results)

    def test_rectangle_stl(self):
        nw = Point(-20, 1, 19)
        se = Point(18, 1, -17)
        ne = Point(se.x, se.y, nw.z)
        sw = Point(nw.x, nw.y, se.z)

        r1 = Rectangle(nw, sw, se, ne)
        canvas = STLCanvas()
        canvas.add_shape(r1)
        canvas.write_stl('example_test_rect.stl', make_positive=False)

    def test_cube_stl(self):
        high = Point(-20, 16, 19)
        low = Point(18, -15, -17)
        b1 = Box(low, high)
        canvas = STLCanvas()
        canvas.add_shape(b1)
        canvas.write_stl('example_test_cube.stl', make_positive=False)
