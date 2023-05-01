import av
import threading
import tkinter as tk
from PIL import ImageTk, Image, ImageOps
import os
from traitement import Traitement

class Video(tk.Label):
    def __init__(self, master, adresse):
        super(Video, self).__init__(master)
        self.adresse = adresse
        self.imgtk1 = None
        self.imgtk2 = None

    def connexion(self): # permet de lire une image de l'afficher tout en lisant en même temps l'image suivante
        with av.open(self.adresse) as container:
            un = False
            while True:
                try:
                    frame = next(container.decode(video=0))
                    img = frame.to_image()                     

                    if un:
                        self.imgtk1 = ImageTk.PhotoImage(img)
                        self.config(image=self.imgtk1)
                        un = False
                    else:
                        self.imgtk2 = ImageTk.PhotoImage(img)
                        self.config(image=self.imgtk2)
                        un = True

                except Exception as e:
                    break

    def sauvegarde_img(self): # permet de sauvegarder une image précise lorsque le bouton photo est activé
        save_img = self.imgtk1
        new_file_name = "photo_drone.png"
        imgpil = ImageTk.getimage( save_img )
        imgpil.save( os.path.join("/tmp", new_file_name), "PNG" )
        imgpil.close() 

        analyse = Traitement(os.path.join("/tmp", new_file_name), 240, new_file_name, "/tmp/", "/tmp/")
        moyennes = analyse.tile()
        
        return moyennes
    
    def play(self): # activation de la vidéo du drone
        load_thread = threading.Thread(target=self.connexion, daemon=True)
        load_thread.start()
