from Tkinter import *
import Tkinter as tk
import re

def create_window():
    window = tk.Toplevel()

def openServer():
    win.withdraw()
    win.newWindow = Toplevel(win.bind("Server_Window.py"))
    #data = open("Server_Window.py")
    #f = data.read().split()
    #print (f)


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

def namesuggestion ():
     print "Hello"




def makeWindow () :
    global nameVar, namSugg
    win = Tk()
    win.title('Sudoku')
    Label(win, text = 'Welcome to Sudoku World').pack(pady=30)
    win.geometry('500x400')

    # read the data file into a listbox1
    fin = open("Player_Name.txt", "r")
    chem_list = fin.readlines()
    fin.close()
    # strip the trailing newline char
    chem_list = [chem.rstrip() for chem in chem_list]


    frame1 = Frame(win)
    frame1.pack()
    C = Canvas()
    Label(frame1, text="Player Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    namSugg = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    frame2 = Frame(win, width = 200, height = 100)
    scrollbar = Scrollbar(frame2, orient = VERTICAL)
    # listbox1 = Listbox(win, yscrollcommand=scrollbar.set, selectmode = MULTIPLE, width = 50, height = 6)
    # #listbox1.grid(row = 0, column = 0)
    # scrollbar.config(command = listbox1.yview)
    # scrollbar.pack(side = RIGHT, fill = Y)
    f = open("Player_Name.txt").readlines()
    print(f)

    listbox = Listbox(win, width=60)
    scrollbar.pack(side=LEFT, fill=Y)
    scrollbar.config(command=listbox.yview)
    #scrollbar.config(command = listbox.yview)
    #scrollbar.config(command=listbox.yview)
    #scrollbar.pack(side = RIGHT, fill = Y)
    listbox.pack()
    fixedlen = 10
    for word in f:
        item = word
        print item  # Gives nicely formatted lines
        listbox.insert(END, item)  # Lines are not nicely formatted in listbox

    # listbox1.grid(row = 0, column = 0)

    #************************************
    # Defining entry widget for the listbox
    entr1 = Entry(win, width = 50, bg = 'yellow')
    entr1.insert(0, 'Select a name from the List')
    #entr1.grid(row = 1, column = 0)
    #entr1.bind('<Return>', set_list)
    #entr1.bind('<Double-1>', set_list)



    C.pack(pady=40)

    b = Button(C, text="Save Player", command=lambda:save(nameVar))
    b1 = Button(C,text=" Enter  ", command = lambda :openServer())
    b4 = Button(C,text=" Cancel ", command = lambda:exit(sys))

    b1.pack(side=LEFT, padx = 20)
    b.pack(side = LEFT,padx = 20)
    b4.pack(side=RIGHT, padx=20)


    #listbox1.insert(END,"Player Name Suggestion")
    #listbox1.pack(side=LEFT, fill=BOTH, expand=1)
    frame2.pack()
    return win


win = makeWindow()
win.mainloop()


