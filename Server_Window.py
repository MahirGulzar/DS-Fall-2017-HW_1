print ("This is the server window")
from Tkinter import *

root = Tk()
# class NewWin:
#     def __init__(self, master):
#         self.master = master
#         self.master.withdraw()
        #self.newWindow = Toplevel(self.master)
        # bb = Frame(self.newWindow, width=500, height=500)
        # b4 = Button(self.master, text=" Cancel ", command=lambda: exit(sys))
        # b4.pack()
        # bb.pack()


    # def new_window(self):
    #     self.master.withdraw()
    #     self.newWindow = Toplevel(self.master)
    #     bb = Frame(self.newWindow, width = 200, height = 100)

    # def starters_menu():
        #self.listBox.delete(0, END)
        # starters_menu = open("Player_Name.txt")
        # for line in starters_menu:
        #     line = line.rstrip()
        # listbox1.insert(END, line)
        # listbox1.bind("<ButtonRelease-1>",  add="+")
        # listbox1.bind("<ButtonRelease-1>",  add="+")
        #recipe_menu.add_command(label="Starters, Snacks and Savouries", command=starters_menu)

frame1 = Frame()
frame1.pack()
C = Canvas()
Label(frame1, text="Enter Server Name").grid(row=0, column=0, sticky=W)
nameVar = StringVar()
namSugg = StringVar()
scrollbar = Scrollbar(C, orient=VERTICAL)
#listbox1 = Listbox(frame1, yscrollcommand=scrollbar.set, selectmode=MULTIPLE, width=50, height=6, command = filllistbox())
#with open('Player_Name.txt') as f:
#    lines = f.read().splitlines()
f = open("Player_Name.txt").readlines()
print(f)
listbox = Listbox(root, width=60)
listbox.pack()
fixedlen = 10
for word in f:
    item = word
    print item  # Gives nicely formatted lines
    listbox.insert(END, item)  #Lines are not nicely formatted in listbox

# listbox1.grid(row = 0, column = 0)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)


root.mainloop()