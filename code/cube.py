import numpy

from utils import Point, Triangle
from stl_canvas import STLCanvas

from indicies import PX, PY, PZ


class Triangle:
    """
    A single triangles

    A
    |\
    | \
    +--\
    B   C
    """

    def __init__(self, PtA, PtB, PtC):
        self.points = [PtA, PtB, PtC]

    def get_triangles(self):
        return self.points


class Rectangle:
    """
    A Single Rectangle

    A         D
    +---------+
    |         |
    +---------+
    B         C
    """

    def __init__(self, PtA, PtB, PtC, PtD):
        self.points = [PtA, PtB, PtC, PtD]

    def __getitem__(self, x):
        return self.points[x]

    def get_triangles(self):
        return [(self.points[0], self.points[1], self.points[2]),
                (self.points[0], self.points[2], self.points[3])]

class Box:
    """
    A Single Rectangular Prism

    far
    +-------+
    |\       \
    | \       \
    |  +-------+
    \  |       |
     \ |       |
      \+-------+
               near

    +Y
    |
    |
    |---- +X
     \
      \
       +Z
    """
    def __init__(self, near, far):
        self.near = near
        self.far = far

    def get_triangles(self):
        top = Rectangle((self.far[PX], self.far[PY], self.far[PZ]),
                        (self.far[PX], self.far[PY], self.near[PZ]),
                        (self.near[PX], self.far[PY], self.near[PZ]),
                        (self.near[PX], self.far[PY], self.far[PZ]))

        bottom = Rectangle((self.far[PX], self.near[PY], self.near[PZ]),
                           (self.far[PX], self.near[PY], self.far[PZ]),
                           (self.near[PX], self.near[PY], self.far[PZ]),
                           self.near)

        sides = []
        sides.append(Rectangle(top[0], bottom[1], bottom[0], top[1]))
        sides.append(Rectangle(top[1], bottom[0], bottom[3], top[2]))
        sides.append(Rectangle(top[2], bottom[3], bottom[2], top[3]))
        sides.append(Rectangle(top[3], bottom[2], bottom[1], top[0]))

        triangles = top.get_triangles()
        triangles.extend(bottom.get_triangles())
        for s in sides:
            triangles.extend(s.get_triangles())

        return triangles


def output_cube_stl(filename, triangles):
    canvas = STLCanvas()
    canvas.add_triangles(cube_triangles)
    # canvas.write_ascii_stl(filename, make_positive=False)
    canvas.write_stl(filename, make_positive=False)
