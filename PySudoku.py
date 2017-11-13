from __future__ import print_function
# Imports.....

import sys, os, random, pygame  # Using 3rd Party pygame library
sys.path.append(os.path.join("objects"))
import SudokuSquare
import SudokuGrid
from GameResources import *
import socket
import Common
from Client_Handler import Handler
import Client_Handler

#-----------------------------------------------------------------



import Client_Handler
import select, socket, sys
from pychat_util import Room, Hall, Player
import pychat_util
import threading
import time


#print("hi")

READ_BUFFER = 4096
'''
if len(sys.argv) < 2:
    print("Usage: Python3 client.py [hostname]", file = sys.stderr)
    sys.exit(1)
else:
'''
score=0
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server_connection.connect((sys.argv[1], pychat_util.PORT))
server_connection.connect(('127.0.0.1', pychat_util.PORT))

def prompt():
    print('>', end=" ")

def refresh_query():
    print('doing refresh loop..')
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

        #print(Client_Handler.MainGrid[0][8])
        #print(len(Client_Handler.theSquares))
        # print(len(Client_Handler.MainGrid))
        #Client_Handler.
        for i in range(9):
            for j in range(9):
                # print("New = ",Client_Handler.MainGrid[i][j])
                # print("Old = ",grid[i][j])
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
        #Client_Handler.Refresh_Display(Client_Handler.MainGrid)
    except:
        print('Exception raised..')
    #Client_Handler.Refresh_Display()
   #Client_Handler.current.set_Grid(grid)
    #print(Client_Handler.MainGrid)


    refresh_query()


print ("Connected to server\n")
msg_prefix = ''

socket_list = [sys.stdin, server_connection]

name='mahir'
while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for s in read_sockets:
        if s is server_connection: # incoming message
            msg = s.recv(READ_BUFFER)
            #print(msg)
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
                        msg_prefix = 'name: '+name  # identifier for session list
                        server_connection.sendall(msg_prefix.encode())
                        continue
                        # msg_prefix = 'session:'  # identifier for session list

                    elif 'Oops' in msg.decode():
                        msg_prefix = 'name: ' + name  # identifier for session list
                        server_connection.sendall(msg_prefix.encode())
                        continue
                        #msg_prefix = 'session:'  # identifier for new session
                    elif 'welcomes' in msg.decode() and Client_Handler.inroom is False:
                        print('WElcome...')
                        grid=msg.replace("welcomes: ", "")
                        handle = Client_Handler.Handler()

                        #refreshloop.join()
                        game = threading.Thread(target=handle.Initial_Reception, args=(grid,name,s))
                        refreshloop = threading.Thread(target=refresh_query)
                        game.start()
                        refreshloop.start()
                        game.join()
                        #handle.Initial_Reception(grid,name,s)
                        refreshloop.join()
                        #threading.Thread(target=handle.Initial_Reception,args=(grid,name))

                        print('Coming after welcome..')
                        Client_Handler.inroom=True
                    elif 'selection' in msg.decode():
                        #print('Selection...')
                        msg_prefix = 'session:'  # identifier for new session
                        #Client_Handler.inroom = True
                    elif 'grid: ' in msg:
                        #print('incoming...')
                        #print(msg)
                        grid = msg.replace("grid: ", "")
                        #print(grid)

                    else:
                        msg_prefix = ''

                    if(Client_Handler.inroom is False):
                        prompt()

        else:
            print(Client_Handler.inroom)
            if(Client_Handler.inroom is False):

                print('Waiting for client input... fuck..')
                msg = msg_prefix + sys.stdin.readline()
                server_connection.sendall(msg.encode())
