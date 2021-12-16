#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    throw_error_if_any_side_is_not_positive(a, b, c)
    throw_error_if_sum_of_two_sides_less_than_third(a, b, c)

    if a != b and b != c and a != c:
        return 'scalene'
    elif a == b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'


def throw_error_if_any_side_is_not_positive(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError


def throw_error_if_sum_of_two_sides_less_than_third(a, b, c):
    x, y, z = sorted([a, b, c])

    print(x, y, z)

    if x + y <= z:
        raise TriangleError


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
