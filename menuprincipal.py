# Créé par CHALLUP, le 06/02/2023 en Python 3.7
from tkinter import*
fenetre = Tk()
fenetre.title("Menu principal")
fenetre.geometry('500x600')

texte1 = Label (fenetre, text = "Voici les fonctions à disposition pour ce répertoire :")
texte1.pack()

boutonaffichercontact = Button (fenetre, text = "Afficher un contact")
Button(text="Afficher un contact").pack()

boutonafficherrepertoire = Button (fenetre, text = "Afficher le répertoire")
Button(text="Afficher le répertoire").pack()

boutonrechercher = Button (fenetre, text = "Rechercher dans le répertoire")
Button(text="Rechercher dans le répertoire").pack()

boutonsupprimercontact = Button (fenetre, text = "Supprimer un contact")
Button(text="Supprimer un contact").pack()

boutonquitter = Button (fenetre, text = "Quitter")
Button(text="Quitter").pack()

fenetre.mainloop()