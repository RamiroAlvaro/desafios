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

VISITED = 2


def process_island(i: int, j: int, grid: List[List]) -> None:
    try:
        if grid[i][j] == 1:
            grid[i][j] = VISITED
            process_island(i - 1, j, grid)
            process_island(i + 1, j, grid)
            process_island(i, j - 1, grid)
            process_island(i, j + 1, grid)
    except IndexError:
        return


def island(grid: List[List]) -> int:
    result = 0

    for i, _ in enumerate(grid):
        for j, value in enumerate(grid[i]):
            if value == 1:
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
