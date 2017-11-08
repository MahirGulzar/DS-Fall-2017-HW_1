import SudokuSquare
import SudokuGrid
from GameResources import *
import socket
import select
import Common
import threading
import Buffer_Handler


current=None
MainGrid=[]
pygame.init()
size = width, height = 400, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
board, boardRect = load_image("SudokuBg.png")
boardRect = boardRect.move(10, 80)
s = socket.socket()
host = socket.gethostname()


class Handler:
    """A class to handle server send and recieve data"""


    def Update_Grid(self, grid):

        global current
        current = SudokuGrid.SudokuGrid()

        current.set_Grid(grid)

        return current

    def Modify_Grid(self,yLoc, xLoc,event):

        global current
        current.setNum(yLoc, xLoc, event)
        current.printGrid()

        return current

    def Initial_Reception(self,s):



        print("Awaiting Server Request/...")

        resp = s.recv(1024)
        grid = []
        li = []
        string_grid = resp.split(',')
        for element in string_grid:

            #print(element.strip())
            element = element.strip()
            if (element.strip() == 'None'):
                li.append(None)
            elif (len(element.strip()) > 0):
                li.append(int(element))
                # li.append(1)

            if (len(li) == 9):
                grid.append(list(li))
                li = []

        global MainGrid
        MainGrid = grid

        Start(MainGrid)

    def Send_Key_Update(self):

        s.sen



#------------------------------------------------------





def Refresh_Display(current):
    # handle = Handler()
    theSquares = []
    initXLoc = 10
    initYLoc = 80
    startX, startY, editable, number = 0, 0, "N", 0
    for y in range(9):
        for x in range(9):
            if x in (0, 1, 2):  startX = (x * 41) + (initXLoc + 2)
            if x in (3, 4, 5):  startX = (x * 41) + (initXLoc + 6)
            if x in (6, 7, 8):  startX = (x * 41) + (initXLoc + 10)
            if y in (0, 1, 2):  startY = (y * 41) + (initYLoc + 2)
            if y in (3, 4, 5):  startY = (y * 41) + (initYLoc + 6)
            if y in (6, 7, 8):  startY = (y * 41) + (initYLoc + 10)
            number = current.getNum(y, x)
            if number != None:
                editable = "N"
            else:
                editable = "Y"
            theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

    currentHighlight = theSquares[0]
    currentHighlight.highlight()

    screen.blit(background, (0, 0))
    screen.blit(board, boardRect)
    # screen.blit(logo, logoRect)
    pygame.display.flip()

    # load_music("PySudokuTheme1.ogg")

    theNumbers = {pygame.K_0: "0", pygame.K_1: "1", pygame.K_2: "2",
                  pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5",
                  pygame.K_6: "6", pygame.K_7: "7", pygame.K_8: "8",
                  pygame.K_9: "9", pygame.K_SPACE: "", pygame.K_BACKSPACE: "",
                  pygame.K_DELETE: ""}

def Start(grid):
    global background
    global screen
    global size
    global board
    global boardRect

    handle = Handler()
    theSquares = []
    initXLoc = 10
    initYLoc = 80
    startX, startY, editable, number = 0, 0, "N", 0
    for y in range(9):
        for x in range(9):
            if x in (0, 1, 2):  startX = (x * 41) + (initXLoc + 2)
            if x in (3, 4, 5):  startX = (x * 41) + (initXLoc + 6)
            if x in (6, 7, 8):  startX = (x * 41) + (initXLoc + 10)
            if y in (0, 1, 2):  startY = (y * 41) + (initYLoc + 2)
            if y in (3, 4, 5):  startY = (y * 41) + (initYLoc + 6)
            if y in (6, 7, 8):  startY = (y * 41) + (initYLoc + 10)
            number = handle.Update_Grid(grid).getNum(y, x)
            if number != None:
                editable = "N"
            else:
                editable = "Y"
            theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

    currentHighlight = theSquares[0]
    currentHighlight.highlight()

    screen.blit(background, (0, 0))
    screen.blit(board, boardRect)
    # screen.blit(logo, logoRect)
    pygame.display.flip()

    # load_music("PySudokuTheme1.ogg")

    theNumbers = {pygame.K_0: "0", pygame.K_1: "1", pygame.K_2: "2",
                  pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5",
                  pygame.K_6: "6", pygame.K_7: "7", pygame.K_8: "8",
                  pygame.K_9: "9", pygame.K_SPACE: "", pygame.K_BACKSPACE: "",
                  pygame.K_DELETE: ""}

    while 1:
        # Refresh_Display(Client_Handler.current)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for x in theSquares:
                    if x.checkCollide(mousepos):
                        currentHighlight.unhighlight()
                        currentHighlight = x
                        currentHighlight.highlight()
            if event.type == pygame.KEYDOWN and event.key in theNumbers:
                currentHighlight.change(theNumbers[event.key])
                print "[ %s, %s ]" % currentHighlight.currentLoc()
                xLoc, yLoc = currentHighlight.currentLoc()
                handle.Modify_Grid(yLoc, xLoc, theNumbers[event.key])
                # current.setNum(yLoc, xLoc, theNumbers[event.key])
                # current.printGrid()

        for num in theSquares:
            num.draw()
        pygame.display.flip()
        # clock.tick(60)

def Establish_Connection(port,handle):

    s.connect((host, port))
    #s.bind()
    handle.Initial_Reception(s)
