# --- Modules --- #
from tkinter import *
from tkinter import filedialog
import os

# --- Functions --- #
# Create Board
def createBoard():
    board = []
    board.append([5,0,0,0,0,0,4,2,0])
    board.append([0,0,2,6,8,0,9,0,5])
    board.append([0,0,7,0,5,0,0,8,0])
    board.append([0,8,5,4,0,9,1,0,0])
    board.append([7,0,4,0,0,2,0,9,8])
    board.append([2,1,0,0,3,0,0,0,4])
    board.append([4,7,0,8,0,1,2,0,0])
    board.append([0,0,1,0,0,0,3,4,0])
    board.append([0,2,0,3,0,5,8,7,0])
    return board

# Create Custom Board
def createCustomBoard():
    window = Tk()
    window.withdraw()
    
    file = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("Text File", "*.txt"), ("All File Types", "*.*")))
    with open(file, "r") as f:
        lines = f.readlines()

    window.quit()

    board = []
    for line in lines:
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace("\n", "")

        line_list = line.split(",")
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        board.append(line_list)

    return board

# Print Board
def printBoard(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("----------------------")
        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")
            if column == 8:
                print(board[row][column])
            else:
                print(board[row][column],end=" ")

# Check Empty
def findEmpty(board):
    empty = []
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                empty.append((row, column))
    return empty

# Check Validity
def valid(board, row, column, number):
    # Check Row
    for i in range(len(board[0])):
        if board[row][i] == number and column != i:
            return False

    # Check Column
    for i in range(len(board)):
        if board[i][column] == number and row != i:
            return False

    # Check Box
    box_x = column // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == number and (i, j) != (row, column):
                return False

    return True

# Check If Board Solved
def completed(board):
    for row in range(len(board)):
        if 0 in board[row]:
            return False
    return True

# Solve The Sudoku
def solve(board):
    empties = findEmpty(board)
    l_index = 0
    while not completed(board):
        number = board[empties[l_index][0]][empties[l_index][1]]
        number += 1
        while not valid(board, empties[l_index][0], empties[l_index][1], number) and number <= 9:
            number += 1
            if number > 9:
                break
        
        if number > 9:
            board[empties[l_index][0]][empties[l_index][1]] = 0
            l_index -= 1
        else:
            board[empties[l_index][0]][empties[l_index][1]] = number
            l_index += 1
    printBoard(board)

def main():
    run = True
    while run:
        # Solve Board
        os.system('cls')
        mode = input("Enter '1' for solving premade board or '2' for custom file board : ")
        while mode not in [str(1), str(2)]:
            mode = input("Enter 1 for solving premade board or 2 for custom file board : ")

        os.system('cls')
        if mode == str(1):
            board = createBoard()
            printBoard(board)
            print("\\")
            print("/")
            print("\\")
            print("/")
            print("\\")
            print("/")
            solve(board)
        else:
            try:
                board = createCustomBoard()
                printBoard(board)
                print("\\")
                print("/")
                print("\\")
                print("/")
                print("\\")
                print("/")
                solve(board)
            except (AttributeError, FileNotFoundError):
                print("Error ! Please select the text file that contains the appropriate board.")
                pass

        # Retry
        ret = input("Enter '1' for retry or '2' to quit : ")
        while ret not in [str(1), str(2)]:
            ret = input("Enter '1' for retry or '2' to quit : ")
        if ret == str(1):
            run = True
        else:
            os.system('cls')
            run = False
                        
if __name__ == "__main__":
    main()
