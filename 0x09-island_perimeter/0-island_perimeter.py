#!/usr/bin/python3
"""
A function that returns the perimeter
of the island described in a grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    grid is a list of integers
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally)
    - grid is rectangular, with its width and height not exceeding 100

    The grid is completely surrounded by water
    There is only one island (or nothing)
    The island doesnot have lakes
    """
    perimeter = 0
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])

    for row in range(no_of_rows):
        for col in range(no_of_cols):
            if grid[row][col] != 0:
                perimeter += check_all_side(grid, row, col)

    return perimeter


def check_all_side(grid, row, col):
    """
    Checks all sides of the cell if it is 0 or 1
    It returns the perimeter based on it
    """
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    perimeter = 0

    if row > 0:
        if grid[row - 1][col] == 0:
            perimeter += 1
    else:
        perimeter += 1

    if row < no_of_rows - 1:
        if grid[row + 1][col] == 0:
            perimeter += 1
    else:
        perimeter += 1

    if col > 0:
        if grid[row][col - 1] == 0:
            perimeter += 1
    else:
        perimeter += 1

    if col < no_of_cols - 1:
        if grid[row][col + 1] == 0:
            perimeter += 1
    else:
        perimeter += 1

    return perimeter
