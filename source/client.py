import socket
import sys
import threading

class Client:
    
    # permet la connection entre le programme et le drone 
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 8889))

    def config(self,ip,port):
        try:
            self.sock.connect((ip,port))
            self.addr=(ip,port)
        except socket.error as msg:
            print("Couldn't connect with the socket-server: %s\n terminating program" % msg)
            sys.exit(1)
        print("Connexion on {}".format(port))
        
        load_thread = threading.Thread(target=self.recevoir, daemon=True)
        load_thread.start()
        
    def envoyer(self,message):
        print("envoi de " + message)
        self.sock.sendto(message.encode('utf-8'),self.addr)

    def recevoir(self):
        while True:
            reponse, adresse = self.sock.recvfrom(512)
            print("réception de " + reponse.decode())
