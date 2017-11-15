
from Tkinter import *
import tkMessageBox as messagebox
import Tkinter as tk
import sys
#import Sudoku_Client

'''
This is the user interface code for Sudoku GUI. It asks for a player name first and saves the player name
in a txt file. If a player has already saved his/her name, the player can select his/her name from a listbox appearing
in the main window.
'''

UserName=''

def create_window():

    window = tk.Toplevel()

'''
The openServer functions executes, when the player name is accepted. It opens a new python window where the player need to specify
the server address and port number.
'''
def openServer(player):
    global UserName
    #execfile('/Server Side/Game_Server.py')
    #execfile('GUI2.py')
    #print player.get()
    UserName = player.get()
    print(UserName)
    #Sudoku_Client.name = player.get()
    #execfile('Sudoku_Client.py')


def openclient(player):
    print player.get()
    Sudoku_Client.name = player.get()
    execfile('Sudoku_Client.py')
'''
The save function saves a new player name. It also checks if a name already exists and avoids adding duplicate player name.
'''

def save(player):
    text = player.get()
    data = open('Player_Name.txt',"r+")
    f = list(data.read().split())
    #print (f)
    for nicknames in f:
        if text in f:
            print ("Nickname already exists")
            messagebox.showinfo('Error','Nickname already exists')
            break
        else:
            data.write(text+"\n")
            print ("New name added")
            break
    #print (nicknames)
    return text

'''
The makeWindow() function creates the GUI interface using Tkinter widgets. All widgets are activated or displayed by calling the pack function,
which is a default function for every widget is called.
'''

def makeWindow():
    global nameVar, namSugg
    win = Tk()
    win.title('Sudoku')
    Label(win, text = 'Welcome to Sudoku world').pack(pady = 30)
    win.geometry('500x400')

    frame1 = Frame(win)
    frame1.pack()
    C = Canvas()
    Label(frame1, text = 'Player Name').grid(row = 0, column = 0, sticky = W)
    nameVar = StringVar()
    namSugg = StringVar()

    name = Entry(frame1, textvariable = nameVar)
    name.grid(row = 0, column = 1, sticky = W)

    frame2 = Frame(win, width = 200, height = 100)
    scrollbar = Scrollbar(win)
    scrollbar.pack(side = RIGHT, fill = Y)

    listbox = Listbox(frame2, yscrollcommand = scrollbar.set)
    f = open('Player_Name.txt').readlines()
    for word in f:
        item = word
        listbox.insert(END, item)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar.config(command = listbox.yview)

    C.pack(pady = 40)
    b = Button(C, text = 'Save Player', command = lambda:save(nameVar))
    b1 = Button(C, text = 'Enter', command = lambda:openServer(nameVar))
    b4 = Button(C, text = 'Cancel', command = lambda:exit(sys))
    b.pack(side = LEFT, padx = 20)
    b1.pack(side = LEFT, padx = 20)
    b4.pack(side = RIGHT, padx = 20)
    frame2.pack()
    namep= nameVar.get()
    print namep
    return win,namep





win,s = makeWindow()
print s
win.mainloop()

