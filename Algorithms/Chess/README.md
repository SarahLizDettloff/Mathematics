# Chess
This chess program utilizes algebraic notation by providing the user with the potential chess moves on a chess board. <br />
It allows the user to input the chess piece type as well as the coordinates on a chess board to estimate potential moves. <br />
This is written, assuming no other chess pieces are on a board. <br />
<br />
Example of chess board coordinates: 
<br />
<br />
![alt text](http://www.regencychess.co.uk/blog/wp-content/uploads/2012/05/empty-numbered-chess-set.gif)
<br />
(Image from http://www.regencychess.co.uk) <br />

Example: <br />
Output: Type in the name of the piece you want to see the potential moves of. <br />
input: knight <br />
Output: Enter the location of that piece:  <br />
input: d3 <br />
output: ('Possible Knight Moves ', ['b4', 'c5', 'e5', 'f4', 'f2', 'e1', 'c1', 'b2']) <br />

# Installing
This program was created in Python Shell 2.7.11 <br />
To download Python 2.7.11 follow the link below:  <br />
https://www.python.org/downloads/release/python-2711/ <br />
Step 1: Download Python 2.7.11 installer<br />
Step 2: Open IDLE(Python GUI)<br />
Step 3: Save file as .py<br />
Step 4: Run and enjoy!<br />

# Debugging Coverage
1. Fixed Rook
2. Fixed Queen
3. Fixed Bishop
4. Cleaned and reorganized code for King
5. Cleand and reorganized code for Knight
6. Added Pawn features
7. Updated ASCII directory
8. Changed Matrix to global variables
9. Fixed boundaries
10. Added feature to allow only legal chess board positions
11. Added run()
12. Unit Test for Python.py was created and gave false positive results. Revised via advice from Shannon Simpson.
13. Queen positions were revised.
14. Input boundaries for user to only be able to input coordinates of letters a-h, and numbers 1-8.
15. Fixed bug which only allowed lower case piece types to be inputted.

# Works Cited: <br />
David Moeser, ASCII Chess Pieces, http://www.chessvariants.com/d.pieces/ascii.html(1996) <br />
Unit testing, Python standard library, https://docs.python.org/2/library/unittest.html <br />
