#!/usr/bin/python3
import sys
"""N Queens problem"""


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position (row, col) on the board.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check for queens in the upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    print_solutions(solutions)


def backtrack(board, row, solutions):
    """
    Backtracking function to place queens on the board.
    """
    if row == len(board):
        solutions.append([''.join(row) for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = '.'


def print_solutions(solutions):
    """
    Print all the solutions to the N Queens problem.
    """
    for solution in solutions:
        for row in solution:
            print(row)
        print()


def main():
    """
    Main function to handle command line arguments and solve the N Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number greater or equal to 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == '__main__':
    main()
