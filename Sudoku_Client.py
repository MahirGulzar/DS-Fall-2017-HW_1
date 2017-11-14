from __future__ import print_function

import sys, os
import pygame               # Must install pygame for this module to work (see Manual)
sys.path.append(os.path.join("objects"))
sys.path.append(os.path.join("Server Side"))
sys.path.append(os.path.join("Client Side"))
from GameResources import *
import Client_Handler
import select, socket, sys
import pychat_util
import threading
import time


#-----------------------------------------------------------------

'''
Sudoku Client script handles the initial server connection 
and resolves the protocols. When the client is assigned a room
and a game this script runs two threads:

1- For continous reception of Grid Updation from server
2- Game Logic and GUI of Client Handler
'''



READ_BUFFER = 4096
score=0
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_connection.connect(('127.0.0.1', pychat_util.PORT))



"""
A recursive method running under reception thread
to recive continous updated grid from server.
"""

def refresh_query():
    #print('doing refresh loop..')
    time.sleep(1)
    msg='refresh:'
    try:
        server_connection.sendall(msg.encode())
        msg = server_connection.recv(READ_BUFFER)
        self_grid = msg.replace("grid: ", "")
        grid = []
        li = []
        string_grid = self_grid.split(',')
        for element in string_grid:

            # print(element.strip())
            element = element.strip()
            if (element.strip() == 'None'):
                li.append(None)
            elif (len(element.strip()) > 0):
                li.append(int(element))
                # li.append(1)

            if (len(li) == 9):
                grid.append(list(li))
                li = []

        for i in range(9):
            for j in range(9):
                if(Client_Handler.MainGrid[i][j] is not grid[i][j]):
                    print("Old = ",Client_Handler.MainGrid[i][j])
                    print("New = ",grid[i][j])
                    x= 9*(i)
                    y= x+j
                    Client_Handler.theSquares[y].change(grid[i][j])
                    print('i  and j = ',i,j)
                    print('location = %d'%y)
                    print('number = ',grid[i][j])
        Client_Handler.MainGrid = grid
    except:
        print('')


    refresh_query()


#------------------------------------------------------------------------------------------------------


def prompt():
    print('>', end=" ")



print ("Connected to server\n")
msg_prefix = ''                                 # msg prefix is appended as signature term for server
socket_list = [sys.stdin, server_connection]
name='prabs2'


"""
Initial connection and protocol resolution from client side
is handled in this loop
"""
while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for s in read_sockets:
        if s is server_connection: # incoming message
            msg = s.recv(READ_BUFFER)
            if not msg:
                print ("Server down!")
                sys.exit(2)
            else:
                if msg == pychat_util.QUIT_STRING.encode():
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                else:
                    sys.stdout.write(msg.decode())
                    if 'Listing current rooms' in msg.decode():
                        msg_prefix = 'name: '+name  # Send user name to server
                        server_connection.sendall(msg_prefix.encode())
                        continue

                    elif 'Oops' in msg.decode():
                        msg_prefix = 'name: ' + name  # Send user name to server
                        server_connection.sendall(msg_prefix.encode())
                        continue

                    elif 'welcomes' in msg.decode() and Client_Handler.inroom is False:
                        #print('WElcome...')
                        grid=msg.replace("welcomes: ", "")      # replace signature term with empty and
                        handle = Client_Handler.Handler()       # Client Handler Handle class object

                        # Threads to operate client's reception and game GUI
                        game = threading.Thread(target=handle.Initial_Reception, args=(grid,name,s))
                        refreshloop = threading.Thread(target=refresh_query)
                        game.start()
                        refreshloop.start()
                        game.join()
                        refreshloop.join()

                        Client_Handler.inroom=True

                    elif 'selection' in msg.decode():

                        msg_prefix = 'session:'  # identifier for new session

                    elif 'grid: ' in msg:

                        grid = msg.replace("grid: ", "") # identifier for grid

                    else:
                        msg_prefix = ''

                    if(Client_Handler.inroom is False):
                        prompt()

        else:
            #print(Client_Handler.inroom)
            if(Client_Handler.inroom is False):

                #print('Waiting for client input...')
                msg = msg_prefix + sys.stdin.readline()
                server_connection.sendall(msg.encode())
