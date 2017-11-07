import socket
import Common

# socket creation, binding and listening
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

random_counter = 0  #for creating new files on different client request.

# Endless loop for client reception
while True:
    print("\n\nWaiting For Client Requests....\n\n")

    c, addr = s.accept()     # Establish connection with client.

    random_counter+=1
    print 'Connection received from ', addr
    # # if l==Common.NewConnection:
    print "Generating New game Session.."
    print "\nRecieved Connection and registered.. ", addr
    c.send('Client game regisration Done..!')
    c.close()

    print("yes...")
s.close()