import socket
import Common
import random
import threading

from objects import SudokuSquare
from objects import SudokuGrid
from objects import GameResources


# client_threads=[]
#
# def getSudoku(puzzleNumber=None):
#     # """This function defines the solution and the inital view.
#     # Returns two lists of lists, inital first then solution."""
#     inital = SudokuGrid.SudokuGrid()
#     current = SudokuGrid.SudokuGrid()
#     solution = SudokuGrid.SudokuGrid()
#
#     inital.createGrid(27, puzzleNumber)
#     current.createGrid(27, puzzleNumber)
#     solution.createGrid(81, puzzleNumber)
#
#     return inital, current, solution
#
#
# def Client_Reception(c,addr):
#     puzzleNumber = int(random.random() * 20000) + 1
#     inital, current, solution = getSudoku(puzzleNumber)
#     print 'Connection received from ', addr
#     print "Generating New game Session.."
#     print "\nRecieved Connection and registered.. ", addr
#     i = 0
#     send_grid = ''
#     for row in current.get_Grid():
#         for col in row:
#             send_grid = send_grid + ',' + str(col)
#             # c.send(str(col))
#             print(i)
#             i += 1
#
#     print(send_grid)
#     c.send(send_grid)
#     # c.close()
#     text = c.recv(1024)
#     print(text,'from',addr)
#
#
# # socket creation, binding and listening
# s = socket.socket()
# host = socket.gethostname()
# port = 12345
# s.bind((host, port))
# s.listen(5)
#
#
#
# # Endless loop for client reception
# while True:
#     print("\n\nWaiting For Client Requests....\n\n")
#     #print(current.get_Grid())
#
#
#
#     c, addr = s.accept()     # Establish connection with client.
#     client_threads.append(threading.Thread(target=Client_Reception, args=(c,addr)))
#     client_threads[-1].start()
#     #client_threads[-1].join()
#     #Client_Reception(c,addr)
#     # puzzleNumber = int(random.random() * 20000) + 1
#     # inital, current, solution = getSudoku(puzzleNumber)
#     # print 'Connection received from ', addr
#     # print "Generating New game Session.."
#     # print "\nRecieved Connection and registered.. ", addr
#     # i=0
#     # send_grid=''
#     # for row in current.get_Grid():
#     #     for col in row:
#     #         send_grid=send_grid+','+str(col)
#     #         #c.send(str(col))
#     #         print(i)
#     #         i+=1
#     #
#     # print(send_grid)
#     # c.send(send_grid)
#     # # c.close()
#     # text=c.recv(1024)
#     # print(text)
#     #
#     # print("yes...")
# s.close()




#--------------------------------------------------------------------------------------------------------




import select, socket, sys, pdb
from pychat_util import Hall, Room, Player
import pychat_util
import future_builtins
import future



READ_BUFFER = 4096

#host = sys.argv[1] if len(sys.argv) >= 2 else ''
host = '127.0.0.1'
listen_sock = pychat_util.create_socket((host, pychat_util.PORT))

hall = Hall()
connection_list = []
connection_list.append(listen_sock)

while True:
    # Player.fileno()
    read_players, write_players, error_sockets = select.select(connection_list, [], [])
    print("Waiting for Connections")
    for player in read_players:
        if player is listen_sock: # new connection, player is a socket
            new_socket, add = player.accept()
            new_player = Player(new_socket)
            connection_list.append(new_player)
            hall.welcome_new(new_player)

        else: # new message
            msg = player.socket.recv(READ_BUFFER)
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(player, msg)
            else:
                player.socket.close()
                connection_list.remove(player)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)



