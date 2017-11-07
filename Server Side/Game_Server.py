import socket
import Common
import random

from objects import SudokuSquare
from objects import SudokuGrid
from objects import GameResources


def getSudoku(puzzleNumber=None):
    """This function defines the solution and the inital view.
    Returns two lists of lists, inital first then solution."""
    inital = SudokuGrid.SudokuGrid()
    current = SudokuGrid.SudokuGrid()
    solution = SudokuGrid.SudokuGrid()

    inital.createGrid(27, puzzleNumber)
    current.createGrid(27, puzzleNumber)
    solution.createGrid(81, puzzleNumber)

    return inital, current, solution




# socket creation, binding and listening
s = socket.socket()
host = socket.gethostname()
port = 12346
s.bind((host, port))
s.listen(5)


random_counter = 0  #for creating new files on different client request.

# Endless loop for client reception
while True:
    print("\n\nWaiting For Client Requests....\n\n")
    #print(current.get_Grid())


    c, addr = s.accept()     # Establish connection with client.
    puzzleNumber = int(random.random() * 20000) + 1
    inital, current, solution = getSudoku(puzzleNumber)
    random_counter+=1
    print 'Connection received from ', addr
    # # if l==Common.NewConnection:
    print "Generating New game Session.."
    print "\nRecieved Connection and registered.. ", addr
    i=0
    send_grid=''
    for row in current.get_Grid():
        for col in row:
            send_grid=send_grid+','+str(col)
            #c.send(str(col))
            print(i)
            i+=1

    print(send_grid)
    c.send(send_grid)
    c.close()

    print("yes...")
s.close()