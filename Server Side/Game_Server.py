import socket
import Common
import random
import threading

from objects import SudokuSquare
from objects import SudokuGrid
from objects import GameResources




#--------------------------------------------------------------------------------------------------------




import select, socket, sys, pdb
from pychat_util import Hall, Room, Player
import pychat_util
import future_builtins
import future



READ_BUFFER = 4096

host = '127.0.0.1'
listen_sock = pychat_util.create_socket((host, pychat_util.PORT))

hall = Hall()
connection_list = []
connection_list.append(listen_sock)

while True:

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



