# implementing 3-tier structure: Hall --> Room --> Clients;
# 14-Jun-2013

import socket, pdb
import future_builtins
import future

MAX_CLIENTS = 30
PORT = 12345
QUIT_STRING = '<$quit$>'
NEW_SESSION = '<new>'

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

def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print "Now listening at ", address
    return s

class Hall:
    def __init__(self):
        self.rooms = {} # {room_name: Room}
        self.room_player_map = {} # {playerName: roomName}

    def welcome_new(self, new_player):
        #new_player.socket.sendall(b'Welcome to pychat.\nPlease tell us your name:\n')
        self.list_rooms(new_player)

    def list_rooms(self, player):
        
        if len(self.rooms) == 0:
            msg = 'Oops, no active rooms currently. Create your own!\n' \
                + 'Write room name..\n'
            player.socket.sendall(msg.encode())
        else:
            msg = 'Listing current rooms choose a room as number ...\n'
            for room in self.rooms:
                msg += room + ": " + str(len(self.rooms[room].players)) + " player(s)\n"
            player.socket.sendall(msg.encode())
    
    def handle_msg(self, player, msg):
        
        instructions = b'Instructions:\n'\
            + b'[<list>] to list all rooms\n'\
            + b'[<join> room_name] to join/create/switch to a room\n' \
            + b'[<manual>] to show instructions\n' \
            + b'[<quit>] to quit\n' \
            + b'Otherwise start typing and enjoy!' \
            + b'\n'

        print player.name + " says: " + msg
        if "name:" in msg:
            name = msg.split()[1]
            player.name = name
            print "New connection from:", player.name
            player.socket.sendall('selection')

        elif "session:" in msg:
            same_room = False
            if len(msg.split()) >= 2: # error check
                room_name = msg.split()[1]
                if player.name in self.room_player_map: # switching?
                    if self.room_player_map[player.name] == room_name:
                        player.socket.sendall(b'You are already in room: ' + room_name.encode())
                        same_room = True
                    else: # switch
                        old_room = self.room_player_map[player.name]
                        self.rooms[old_room].remove_player(player)
                if not same_room:
                    if not room_name in self.rooms: # new room:
                        new_room = Room(room_name)
                        self.rooms[room_name] = new_room
                    self.rooms[room_name].players.append(player)
                    self.rooms[room_name].welcome_new(player)

                    self.room_player_map[player.name] = room_name
                    #player.socket.sendall(self.r)
            else:
                player.socket.sendall(instructions)

        elif "<list>" in msg:
            self.list_rooms(player) 

        elif "<manual>" in msg:
            player.socket.sendall(instructions)
        
        elif "<quit>" in msg:
            player.socket.sendall(QUIT_STRING.encode())
            self.remove_player(player)

        elif "u:" in msg:
            # player.socket.sendall(QUIT_STRING.encode())
            # self.remove_player(player)
            coordinate_string = msg.replace("u:", "")
            coordinate_list = coordinate_string.split(',')
            # coordinate_list_int =[]
            # for i in range(3):
            #     coordinate_list_int[i]=int(coordinate_list[i])
            #
            # for room in self.rooms:
            #     for player in self.rooms[room].players:
            #         room.current.setNum(coordinate_list_int[0], coordinate_list_int[1], coordinate_list_int[2])
            #         room.




        else:
            # check if in a room or not first
            if player.name in self.room_player_map:
                self.rooms[self.room_player_map[player.name]].broadcast(player, msg.encode())
            else:
                msg = 'You are currently not in any room! \n' \
                    + 'Use [<list>] to see available rooms! \n' \
                    + 'Use [<join> room_name] to join a room! \n'
                player.socket.sendall(msg.encode())
    
    def remove_player(self, player):
        if player.name in self.room_player_map:
            self.rooms[self.room_player_map[player.name]].remove_player(player)
            del self.room_player_map[player.name]
        print "Player: " + player.name + " has left\n"

    
class Room:
    def __init__(self, name):
        self.players = [] # a list of sockets
        self.name = name

        initial,current,solution = getSudoku()
        self.gameObject = current
        self.grid = current.get_Grid()

    def welcome_new(self, from_player):
        i=0
        send_grid=''
        for row in self.grid:
            for col in row:
                send_grid=send_grid+','+str(col)
                #c.send(str(col))
                print(i)
                i+=1
        msg = "welcomes: " + send_grid
        #print(msg)
        for player in self.players:
            player.socket.sendall(msg.encode())

    # def broadcast_grid(self):
    #

    def broadcast(self, from_player, msg):
        msg = from_player.name.encode() + b":" + msg
        for player in self.players:
            player.socket.sendall(msg)

    def remove_player(self, player):
        self.players.remove(player)
        leave_msg = player.name.encode() + b"has left the room\n"
        self.broadcast(player, leave_msg)

class Player:
    def __init__(self, socket, name = "new"):
        socket.setblocking(0)
        self.socket = socket
        self.name = name

    def fileno(self):
        return self.socket.fileno()
