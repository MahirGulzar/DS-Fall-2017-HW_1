from Tkinter import *
import Tkinter as tk
import tkMessageBox
import re
import sys
'''
This is the second user interface code for Sudoku GUI. In this file, the user/player has to provide the server name and
port to enter the sudoku app. The GUI matches the server address with the Game Server. If information provided by the player is correct,
the player can access and enter a game chat.
'''

'''
The create_window() function creates a window.
'''
def create_window():
    window = tk.Toplevel()




server=''
port=''

'''
The openServer() function opens the server window.
'''
def openServer():
    win.withdraw()

global save1

def save1(sname, pname):
    global server
    server = sname.get()
    print ('THis is server address: ',server)

    global port
    port = pname.get()
    print ('This is port number: ', port)


'''
The makeWindow() function creates the GUI interface using Tkinter widgets. All widgets are activated or displayed by calling the pack function,
which is a default function for every widget is called.
'''
def makeWindow () :
    global Sname, Pname
    win = Tk()
    win.title('Sudoku')
    Label(win, text = 'Please provide the following details').pack(pady=30)
    win.geometry('500x400')

    Sname = StringVar()
    Pname = StringVar()


    frame1 = Frame(win)
    name = Entry(frame1, textvariable = Sname)


    label = Label(win, text="Enter Server Address")
    label.pack()
    name.grid(row=0, column=1, sticky=W)


    frame1.pack()
    label2 = Label(win, text="Enter port")
    name1 = Entry(win, textvariable = Pname)
    label2.pack()
    name1.pack()

    # Define a frame
    frame2 = Frame(win, width = 200, height = 300)

    # Define two buttons and each saved inside the framee
    b1 = Button(frame2,text=" Enter ", command = lambda:save1(Sname,Pname))

    #b1 = Button(frame2, text=" Enter ", command=lambda:sav)

    b4 = Button(frame2,text=" Cancel ", command = lambda:exit(sys))

    #Call the pack function to set the visibility of the buttons true
    b1.pack(side=LEFT, padx = 10, pady = 10)
    b4.pack(side=RIGHT, padx=10, pady = 10)

    frame2.pack()
    return win


win = makeWindow()
win.mainloop()



