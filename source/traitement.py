import cv2 as cv
from PIL import Image
from itertools import product
import os
import colorsys

class Traitement:

    def __init__(self, image, d, nom_image, chemin_image, chemin_sortie):
        self.img = cv.imread(image) #permet d'importe l'image
        self.d= d                   #nombre de pixel de l'image
        self.filename=nom_image     #nom de l'image de depart
        self.dir_in=chemin_image    #lieu où l'image de depart est stockée
        self.dir_out=chemin_sortie  #chemin de sortie des images

    
    def moyenne(self, fichier):
        new_img = cv.imread(fichier)
        w, h, c = new_img.shape
        
        x = 0
        y = 0
        total_couleur = 0
        
        for x in range(w):
            for y in range(h):
                pixel = new_img[x,y]
                
                rouge, vert, bleu = pixel[0], pixel[1], pixel[2]
                hls = colorsys.rgb_to_hls(rouge/255, vert/255, bleu/255)
                
                total_couleur += hls[0]*360
                
        moyenne = total_couleur / (w * h)

        return moyenne
    
    def tile(self): # Permet de diviser l'image en plus petit image de même taille
        result_moyenne = []
        name, ext = os.path.splitext(self.filename)
        img = Image.open(os.path.join(self.dir_in, self.filename))
        w, h = img.size

        grid = product(range(0, h-h%self.d, self.d), range(0, w-w%self.d, self.d))
        for i, j in grid:
            box = (j, i, j+self.d, i+self.d)
            new_img = img.crop(box)
            
            out = os.path.join(self.dir_out, f'{name}_{i}_{j}{ext}')
            new_img.save(out)
            
            m = self.moyenne(out)
        
            result_moyenne.append(m)
        return result_moyenne
        
    






