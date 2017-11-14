# REPORT

**Team:**
* Mahir gulzar: B79641
* Prabhant Singh: B79623
* Frozan Maqsoodi: B79640

### Prerequisites:
1. Python2.7
2. Pygame : The best way to install pygame is with the pip tool (which is what python uses to install packages). Note, this comes with python in recent versions. We use the --user flag to tell it to install into the home directory, rather than globally. 
Pip install pygame --user


## User Manual

1. To run the game you have to first initialize the game server called server.py by writing python server.py in the current terminal (Note: remember that the game works on python 2.7.x so do not execute it in python 3.x i.e. do not start the server by python3 server.py, if default python is 3.x then please try python2 server.py to start the server )
2. The game begins by running the python script Gamestart.py. 
3. A new window will open up - enter any player name in this window if joining for the first time, else enter your previous player name. The game saves the list of all players
4. There will be few suggestions to enter the name you can either choose from a name from suggested list or enter a new name.
5. After entering the name you need to provide the server address and port number to connect to the server 
6. After entering the address and port number,  you have two choices: either join an existing game (currently open)  room or create another game room
7. If you want to start a new game then create a new game room else you can join any existing game room (note that the number of players will be written on the side of the name of game room)
8. The game begins as soon as you enter the room. See section (Sudoku Rules) if you are unfamiliar with the game rules, otherwise provide the correct answers in the empty sudoku grid.
9. The game operates on race condition so you need to guess the correct answer in a short time.
10. Note that for every correct answer the reward is 1 point and for every incorrect answer there will be a penalty of -1 point 


Sudoku Rules

1. The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.
2. The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.
3. The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, must also contain the numbers 1-9, without repetition or omission.
4. Every puzzle has just one correct solution.

