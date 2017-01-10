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
def sum_of_two_sides_greater_than_third(a, b, c):
	if (a + b < c) or (b + c < a) or (a + c < b):
		return False
	return True

def greater_than_zero(a, b, c):
	return all(i > 0 for i in [a, b, c])

def triangle(a, b, c):
	if ( a + b + c == 0 or not greater_than_zero(a, b, c) or not sum_of_two_sides_greater_than_third(a, b, c)):
		raise TriangleError('A very specific bad thing happened')
	if (a == b == c):
		return 'equilateral'
	if (a == b or a == c or b == c ):
		return 'isosceles'
	return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
