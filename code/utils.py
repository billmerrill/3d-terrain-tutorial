from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
Triangle = namedtuple('Triangle', ['a', 'b', 'c'])


def nppoint(np_array):
    return Point(np_array[0], np_array[1], np_array[2])
