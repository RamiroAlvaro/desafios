"""
Dado uma matriz 2D de tamanho m x n que representa um mapa de 1s (terra) e 0s (água), retorne o número de ilhas.
Uma ilha é cercada por agua e formada por terras conectadas horizontalmente ou verticalmente.
Você pode assumir que todas as 4 bordas do mapa estão cercadas por água.

Input: grid = [
  [1, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]
Output: 1


Example 2:
Input: grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]
Output: 3


"""
from typing import List

ISLAND = 2
LAND = 1


def process_island(i: int, j: int, grid: List[List]) -> None:
    try:
        if grid[i][j] == LAND:
            grid[i][j] = ISLAND
            process_island(i - 1, j, grid)
            process_island(i + 1, j, grid)
            process_island(i, j - 1, grid)
            process_island(i, j + 1, grid)
    except IndexError:
        return


def island(grid: List[List]) -> int:
    result = 0

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == LAND:
                result += 1
                process_island(i, j, grid)

    return result


assert island([
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]) == 1
assert island([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]) == 3
