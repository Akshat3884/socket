# first of all import the socket library  
import socket              
import threading

s = socket.socket()          

port = 12345                 
s.bind(('localhost', port))       
clients = []   
nicknames = []
# print ("socket binded to %s" %(port))  
#   
s.listen(5)      

print("[SERVER] Server is ready to accept connections")   

# Functions are here
def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

def handle_client(client):
    while True:    
        try:
            message = client.recv(1024).decode()
            broadcast(f'{message}\n')
        except:
            clients.remove(client)
            client.close()
            nicknames.remove(nicknames[clients.index(client)])
            break


# defining a function to recieve clients
def receive_clients():
    while True:
        client , addr = s.accept()
        name = client.recv(1024).decode()

        clients.append(client)
        nicknames.append(name)
        active = len(clients)

        # Printing the name and ip of the connected client
        # NoOne is going to read ServerSide text
        print(f"{name} has connected with ip: ", addr)
        print(f"No. of Active Connections : {active}")

        # Broadcasting to all clients about connected person 
        broadcast(f"[SERVER] {name} Has Connected!!\n")
        broadcast(f"[SERVER] Welcome to this Chat Server {name}\n")
        broadcast(f"[SERVER] NO. of Active connections : {active}\n")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_clients()


    

