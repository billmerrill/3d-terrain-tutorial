from utils import *


def generate_cube_points(high_point, low_point):
    """
    From two opposing points, generate the corners of a cube.

    For both surfaces, generate points in clockwise manner
    when viewing the ouside surface.
    """
    h = high_point
    l = low_point
    top = [h, Point(l.x, h.y, h.z), Point(h.x, h.y, l.z), Point(l.x, h.y, l.z)]
    bottom = [l, Point(l.x, l.y, h.z), Point(h.x, l.y, l.z), Point(l.x, l.y, l.z)]
    return top + bottom


def generate_rect_triangles(p0, p1, p2, p3):
    """
    p1 is upper left, points are clockwise,
    looking down at the visibile surfaces.

            0  1
            2  3
    """
    t1 = Triangle(p0, p2, p3)
    t2 = Triangle(p0, p3, p1)
    return [t1, t2]


def generate_cube_triangles(high_point, low_point):
    corners = generate_cube_points(high_point, low_point)
    surfaces = [
        corners[0:3],
        corners[4:7],
        [corners[0], corners[2], corners[7], corners[5]],
        [corners[2], corners[3], corners[4], cornesr[5]],
        [corners[3], corners[1], corners[4], corners[6]],
        [corners[1], corners[0], corners[6], corners[6]],
    ]
    triangles = []
    for s in surfaces:
        triangles.append(generate_rect_triangles(s))

    return triangles
