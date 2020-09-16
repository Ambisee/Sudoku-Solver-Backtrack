# Sudoku Solver (Backtrack Algorithm)

<b>Language : Python 3.8</b>           

# Package Used
- tkinter.filedialog
- os

# Description

Solving a sudoku puzzle might take you a lot of time, depending on the difficulty of the puzzle. This code can help you with all the stress that you might have accumulated while
solving a particular sudoku puzzle. It utilizes the backtracking algorithm to go through all of the possibilities and reached a solution that fulfills the winning condition of
your particular arrangement of sudoku. With the help of the {tkinter.filedialog} module, you can browse a text file that contains a sudoku board and the code will use it as an
input to generate a solution.

P.S. The text file you browsed must be in the same format shown in the "Board.txt" file :
<ul>
     <li>Create 9 rows of list with 8 commas for each list in the text file</li>
     <li>Fill in a number in between those commas (0 for empty, 9 numbers for each list)</li>
</ul>
