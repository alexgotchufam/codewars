# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

from typing import List


def has_valid_corners(field: List[List[int]], i: int, j: int) -> bool:
    """If any corners contains a piece of other ships then return False"""
    ncols = len(field[0])
    # Top left
    ci = i - 1
    cj = j - 1
    if ci >= 0 and cj >= 0 and field[ci][cj] == 1:
        return False
    # Top right
    ci = i - 1
    cj = j + 1
    if ci >= 0 and cj < ncols and field[ci][cj] == 1:
        return False

    return True


def validate_battlefield(field: List[List[int]]) -> bool:
    # 1 battleship 4
    # 2 cruisers 3
    # 3 destroyers 2
    # 4 submarines 1
    # write your magic here
    count_battleship = 0
    count_cruiser = 0
    count_destroyer = 0
    count_submarine = 0
    nrows = len(field)
    ncols = len(field[0])

    count_cells = [[0] * ncols for _ in range(nrows)] # total number of cells of the ship contains this cell
    
    for i in range(nrows):
        for j in range(ncols):
            if field[i][j] == 0:
                continue

            if not has_valid_corners(field, i, j):
                return False

            pi = i - 1
            pj = j - 1
            if pi >= 0 and pj >= 0:
                if count_cells[i][pj] != 0 and count_cells[pi][j] != 0:
                    return False
                
            prev_count = 0
            if pi >= 0 and count_cells[pi][j] != 0:
                prev_count = count_cells[pi][j]
            elif pj >= 0 and count_cells[i][pj] != 0:
                prev_count = count_cells[i][pj]

            if prev_count == 4:
                return False

            count_cells[i][j] = prev_count + 1

            current_count = count_cells[i][j]
            if current_count == 1:
                count_submarine += 1
            elif current_count == 2:
                count_submarine -= 1
                count_destroyer += 1
            elif current_count == 3:
                count_destroyer -= 1
                count_cruiser += 1
            else:
                count_cruiser -= 1
                count_battleship += 1

    return count_battleship == 1 and count_cruiser == 2 and count_destroyer == 3 and count_submarine == 4