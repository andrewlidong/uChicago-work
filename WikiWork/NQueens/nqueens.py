#!/usr/bin/env python3.4
# nqueens.py
# Output a solution to the n queens problem for given n

""" 

The classic chessboard is comprised of an 8x8 grid. In chess, the queen piece can move up, down, left, right, and diagonally for as many moves as she wants until her path is either blocked by the edge of the board or another piece. In the classic chessboard, you can place at most 8 queens on the board such that none can attack the other.
The problem here is to make a program that, given an NxN board, will output a configuration where there are N queens on the board and none can attack any of the others. Your program should take N as an argument, and you can assume N >= 4 and N is an integer. Although this problem is easy enough to solve for small values of N, the challenge is to make the program run somewhat quickly for large values of N.

This solution is written in Python. It "exploits" a general pattern that gives an explicit solution for any n. This has the advantage of finding a solution quickly, but the disadvantage of giving a perhaps uninteresting solution. Either way, here is the code:


"""


import sys
import math

n = int(sys.argv[1])



def positions(n):
        # Returns a list where the ith element is the number of the row that contains
        # a queen in that column. The layout of the solution is very specific and works
        # for general n > 3.
        pos_by_column = []
        if n % 6 in [0, 4]:
                for i in range(n):
                        pos_by_column.append((2*i + 1) if (2*i < n) else (2*i % n))
        elif n % 6 == 2:
                for i in range(n):
                        pos_by_column.append(((2*i + 3) % n) if (2*i < n)
                                else ((2*i - 2) % n))
        else:
                pos_by_column = positions(n - 1)
                pos_by_column.append(n - 1)

        return pos_by_column



if n < 4:
        print("No solutions exists for n = {}.".format(n))
else:
        layout = positions(n)
        print(layout)

        # Print out a grid for small enough n, for which it looks nice
        if n < 10:
                for i in range(n - 1, -1, -1):
                        output = str(i) + ' '
                        for j in range(n):
                                output += ' '
                                if layout[j] == i:
                                        output += 'Q'
                                else:
                                        output += '*'
                        print(output + '\n')
                print("   " + ' '.join(map(str, range(n))) + '\n')
