# -*- ecoding: utf-8 -*-
# @Author: chiaweiliu
# @Time: 08/31/2022
# @Email:chiaweiliu@ufl.edu
import collections
from collections import defaultdict
class Solution(object):
    def SudokuisValid(self,board):
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    count1[board[i][j]] = count1[board[i][j]] + 1
                    if count1[board[i][j]]>1:
                        print('Duplicate numbers appear in row ',i+1,'and column ',j+1)
                if board[j][i] != '.':
                    count2[board[j][i]] = count2[board[j][i]] + 1
                    if count2[board[j][i]]>1:
                        print('Duplicate numbers appear in row ',j+1,'and column ',i+1)
            for z in count1.values():
                if z > 1:
                    return False
            for z in count2.values():
                if z > 1:
                    return False
            count1.clear()
            count2.clear()

        def squareVaild(x, y):
            nonlocal board
            count3 = collections.defaultdict(int)
            for i in range(3):
                for j in range(3):
                    if board[i + x][j + y] != '.':
                        count3[board[i + x][j + y]] = count3[board[i + x][j + y]] + 1
                for z in count3.values():
                    if z > 1:
                        return False
                return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not squareVaild(i, j):
                    return False
        return True

    def solveSudoku(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    continue
                for c in "123456789":
                    if self.isVaild(board,i,j,c):
                        board[i][j]=c
                        if self.solveSudoku(board):
                            return True
                        board[i][j]='.'
                return False
        return True

    def isVaild(self,board,row,col,c):
        for i in range(9):
            if board[i][col] == c or board[row][i] == c or board[row//3*3+i//3][col//3*3+i%3] == c :
                return False
        return True


    def findEmpty(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    return False
        return True

solve=Solution()
board=[ ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']]

if solve.SudokuisValid(board):
    solve.solveSudoku(board)
    if solve.findEmpty(board):
        print('The solved Sudoku is:')
        h = len(board)
        for i in range(h):
            print(board[i])
    else:
        print("Can't solve sudoku")
else:
    print("Sudoku is wrong")

