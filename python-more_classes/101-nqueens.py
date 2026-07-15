#!/usr/bin/python3
"""Solve the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Return True if a queen can be placed at (row, col).

    Args:
        board: list of column positions for each placed row.
        row: the row being considered.
        col: the column being considered.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(board, row, n):
    """Recursively place queens row by row and print each solution.

    Args:
        board: list of column positions for each placed row.
        row: the current row to fill.
        n: the size of the board.
    """
    if row == n:
        print([[r, board[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve([0] * n, 0, n)
