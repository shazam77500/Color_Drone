from tkinter import *
from client import Client
from video import Video
from grille import Grille
from tkinter import ttk
from ttkthemes import ThemedTk
import time


class Drone:
    # __________fenetre_principale__________
    def __init__(self):
        self.drone = ThemedTk(theme="yaru")
        self.drone.geometry('970x780')
        self.drone.title("Contrôleur de drone")
        
        
        self.init_socket()
        self.init_video()
        self.init_button()

#__________initialisation des boutons__________

        self.drone.bind('<Up>', self.direction_haute)
        self.drone.bind('<Down>', self.direction_basse)
        self.drone.bind('<Left>', self.direction_gauche)
        self.drone.bind('<Right>', self.direction_droite)
        self.drone.bind('<Shift_L>', self.rotation_drone_gauche)
        self.drone.bind('<Shift_R>', self.rotation_drone_droite)
        self.drone.bind('<Control_L>', self.direction_avant)

        self.drone.mainloop()

# ___________configuration_socket__________
    def init_socket(self):
        self.client = Client()
        self.client.config('192.168.10.1', 8889)
        self.client.envoyer('command') #permet d'activer les commandes
        self.client.envoyer('streamon') #permet d'activer la vidéo du drone
        
# __________bouton_commande__________
    def init_button(self):
      
        bouton_decollage = ttk.Button(
            self.drone, text='Décollage', command=self.decollage).grid(row=0, column=0)
        bouton_atterrissage = ttk.Button(
            self.drone, text='Atterrissage du drone', command=self.atterrissage_drone).grid(row=0, column=1)
        bouton_batterie = ttk.Button(self.drone, text="Batterie", command=self.batterie).grid(row=0, column=4)
        bouton_photo = ttk.Button(self.drone, text='Photo',
                              command=self.photo_moyenne).grid(row = 0, column=3)

# ____________video_drone___________
    def init_video(self):
        self.player = Video(self.drone, "udp://192.168.10.1:11111") #permet la réception de la vidéo drone
        self.player.place(x=0, y=50)
        self.player.play()

# ___________commande_drone___________
    def photo_moyenne(self): #permet de faire la moyenne des pixels de chaque parcelle de l'image
        moyennes = self.player.sauvegarde_img()
        Grille(moyennes)
        
    def config(self, ip, port):
        self.client.config(ip, port)

    def decollage(self):
        self.client.envoyer('takeoff')
        
    def batterie(self):
        self.client.envoyer('battery?')

    def rotation_drone_gauche(self, valeur):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "0", "0", "-10"))

    def rotation_drone_droite(self, valeur):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "0", "0", "10"))

    def atterrissage_drone(self):
        return self.client.envoyer('land')

    def direction_arriere(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "-10", "0", "0"))

    def direction_avant(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "10", "0", "0"))

    def direction_basse(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "0", "-10", "0"))

    def direction_gauche(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("-10", "0", "0", "0"))

    def direction_droite(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("10", "0", "0", "0"))

    def direction_haute(self, event):
        return self.client.envoyer('rc {} {} {} {}'.format("0", "0", "10", "0"))


# __________affichage__________
fenetre = Drone()
