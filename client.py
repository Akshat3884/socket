####################################################################
# Import socket module and 
# Threading for running multiple pieces of code at the same time
####################################################################

import socket    
import threading          
  
# Create a socket object  
s = socket.socket()          
  
# Define the port on which you want to connect  
port = 12345                
  
# connect to the server on local computer  
s.connect(('192.168.25.60', port))  

# Taking the username of the user
# and sending it to the server
name = input("Enter a username: ")
s.send(bytes(name,'utf-8'))

# For Recieving thanks for connecting at the begining
print(s.recv(1024).decode())

# Defining func for handeling incoming messages 
# From the server
def incoming_messages():
    incoming_message = s.recv(1024).decode()
    
    if new_message == incoming_message+"\n":
        print("")
    else:
        # Printing the recieved input on another signal 
        print(incoming_message+"\n")

#####################################################################
# main loop to run forever
# Taking input and giving it to the server
while True:
    try:
        # Taking the Main input from the client 
        message = input("> ")
        # Tweaking the input and sending it to the server
        new_message = f"{name} SENT : " + message

        sent_message = s.send(new_message.encode())

        recieving_thread = threading.Thread(target=incoming_messages)
        recieving_thread.start()
            
    except:
        print("There was an error while sending the message")
        print("Please check if the server is running ")
        s.close()
        break
