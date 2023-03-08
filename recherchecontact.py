# Créé par CHALLUP, le 30/01/2023 en Python 3.7

from tkinter import*

def fonction():
    print(recherche.get())

fenetre = Tk()
fenetre.title("Recherche contact")
fenetre.geometry('300x50')

recherche = Entry(fenetre)
recherche.pack()
bouton = Button(text="Rechercher", command=fonction).pack()

fenetre.mainloop()