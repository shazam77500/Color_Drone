from tkinter import *
from traitement import Traitement
from tkinter import ttk
from ttkthemes import ThemedTk

class Grille:
    
    def __init__(self, moyennes):

        self.grille = ThemedTk(theme="yaru")
        self.grille.title("Grille d'arrosage")
        self.grille.geometry('1000x458')

#__________initialisation_de_la_legende__________
        legende_non_champ = ttk.Label(self.grille, text="Cette parcelle ne correspond pas au champ")
        legende_non_champ.place(x=700, y=100)
        
        Canvas(self.grille, width=10, height=10, bg='grey').place(x=680, y=105)

        legende_ne_pas_arroser = ttk.Label(self.grille, text="Cette parcelle n'est pas à arroser")
        legende_ne_pas_arroser.place(x=700, y=150)
        
        Canvas(self.grille, width=10, height=10, bg='green').place(x=680, y=155)
        
        legende_arroser_un_peu = ttk.Label(self.grille, text="Cette parcelle est à arroser un peu")
        legende_arroser_un_peu.place(x=700, y=200)
        
        Canvas(self.grille, width=10, height=10, bg='yellow').place(x=680, y=205)

        legende_arroser = ttk.Label(self.grille, text="Cette parcelle est à arroser")
        legende_arroser.place(x=700, y=250)
        
        Canvas(self.grille, width=10, height=10, bg='red').place(x=680, y=255)

        self.application_traitement(moyennes)
        
        self.grille.mainloop()     
        

    def application_traitement(self, moyennes):   
        row = 0
        column = 0
        
        for result in moyennes: #construction de carrés de couleurs représentant les 12 moyennes
                  
            if result >= 140:
                Canvas(self.grille, width=150, height=150, bg='grey').grid(row = row, column =column)
            elif result < 140 and result > 90:
                Canvas(self.grille, width=150, height=150, bg='green').grid(row= row ,column=column)
            elif result < 90 and result > 50:
                Canvas(self.grille, width=150, height=150, bg='yellow').grid(row=row, column=column)
            else:
                Canvas(self.grille, width=150, height=150, bg='red').grid(row=row, column=column)

        
            if column <= 2: # permet de faire le saut de lignes après 4 carrés 
                column += 1
            else:
                row +=1
                column = 0
                            



