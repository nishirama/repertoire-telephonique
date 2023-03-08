# Créé par CHALLUP, le 16/01/2023 en Python 3.7
from tkinter import*

def lecture(n):
    fichier=open('repertoire.txt','r')
    for i in range(n):
        ligne=fichier.readline()
        ligne=ligne.strip('\n')
    fichier.close()
    return ligne

def affiche(ligne):
    i=0
    while ligne[i]!=":":
        i=i+1
    j=i+1
    while ligne[j]!=":":
        j=j+1
    print("Nom: "+ligne[i+1:j])
    k=j+1
    while ligne[k]!=":":
        k=k+1
    print("Prénom: "+ligne[j+1:k])
    print("Téléphone: "+ligne[k+1:])



fichier=open('repertoire.txt','a')
fichier.write("Iverson:Allen:0658359402\n")
fichier.write("Bird:Larry:0662881930\n")
fichier.write("Jordan:Michael:0675664645\n")
fichier.write("O'Neal:Shaquille:0622943100\n")
fichier.write("Kidd:Jason:0666375477\n")
fichier.write("Chamberlain:Wilt:0646142106\n")
fichier.write("Russell:Bill:0659973128\n")
fichier.write("Rodman:Denis:0633978911\n")
fichier.write("Pippen:Scottie:0623944615\n")
fichier.write("Magic-Johnson:Earvin:0634528691\n")
fichier.close()

fichier=open('repertoire.txt','r')
contenu=fichier.read()
fichier.close()
print(contenu)

affiche(lecture(2))
