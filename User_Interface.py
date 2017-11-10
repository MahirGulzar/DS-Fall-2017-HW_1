###   http://www.openbookproject.net/py4fun/gui/tkPhone.py
from Tkinter import *
import Tkinter as tk

#root = tk.Tk()

def create_window():
    window = tk.Toplevel()


def save(player):
    text = player.get()
    print text
    data = open("Player_Name.txt", "r+")
    f = list(data.read().split())
    print (f)
    for nicknames in f:
        if text in f:
            print "Nick name already exists"
            break
        else:
            data.write(text+"\n")
            print "New name added"
            break



def makeWindow () :
    global nameVar
    win = tk.Tk()
    fname1 = open("Player_Name.txt", "r+")
    frame1 = Frame(master)
    frame1.grid()
    frame1.pack()

    Label(frame1, text="Player Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()

    name = Entry(frame1, textvariable=nameVar)

    name.grid(row=0, column=1, sticky=W)

    
    frame2 = Frame(win)
    frame2.pack()
    b = Button(frame2, text="Save Player", width=15, command=lambda:save(nameVar))
    b1 = Button(frame2,text=" Enter  ", command = create_window)
    b4 = Button(frame2,text=" Cancel ", command = lambda:exit(sys))
    b1.pack(side=LEFT)
    b4.pack(side=LEFT)
    b.pack(side = RIGHT)

    return win




win = makeWindow()
win.mainloop()


