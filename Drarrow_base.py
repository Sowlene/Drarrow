#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 
import turtle
import pygame 
import os
#On crée les variables importantes.
franklin = turtle.Turtle() #La tortue.


#La c'est la fenêtre.
#Avec ses paramètres. 
fenetre = Tk()
fenetre.geometry("700x500+300+0")
fenetre.title('Turtle')
fenetre['bg'] = "white"

#Musique maestro.
#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load("Franklin.mp3") # import du fichier
#pygame.mixer.music.play() # on joue le fichier

#La on commence le code technique.

#Le "bienvenu !"
Bienvenue = Label(fenetre, text="Bienvenue dans le jeu de la tortue, \n le but est de diriger Franklin la tortue ! \n", background="white").pack()
#Le label pour la zone de text de la direction.
text1 = Label(fenetre, text="Veuillez indiquer la direction que doit prendre Franklin : \n TD = Droite ou TG = Gauche ou RE = Aller en arrière").pack()
#Récupération de la direction.
Direction = StringVar() 
DirectionWrite = Entry(fenetre, textvariable=Direction, width=6)
DirectionWrite.pack()       	
#Le label pour la seconde zone de text de la direction.
text3 = Label(fenetre, text="Veuillez indiquer les degrés pour la direction choisie:").pack()
#Récupération des degrés.
Angle = StringVar() 
AngleWrite = Entry(fenetre, textvariable=Angle, width=6)
AngleWrite.pack()

#Le label pour la zone de text de la distance.
text2 = Label(fenetre, text="Quelle distance voulez vous que Franklin fasse dans la direction que vous avec choisie ?").pack()
#Récupération de la distance.
Distance = StringVar()
DistanceWrite = Entry(fenetre, textvariable=Distance, width=5)
DistanceWrite.pack()
def reception():
        DirectionRecup = DirectionWrite.get()	#recupération de la valeur saisie
        AngleRecup = AngleWrite.get()           #recupération de la valeur saisie
        DistanceRecup = DistanceWrite.get()	#recupération de la valeur saisie
			
        print (DirectionRecup, AngleRecup, DistanceRecup)
        if DirectionRecup == "TD":
        	franklin.right(int(AngleRecup))
        	franklin.forward(int(DistanceRecup))
        if DirectionRecup == "TG":
        	franklin.left(int(AngleRecup))
        	franklin.forward(int(DistanceRecup))
        if DirectionRecup == "RE":
        	franklin.backward(int(AngleRecup))

def reset():
	print ("Reset effectué")
	franklin.reset()

def penup():
	print("Crayon relevé")
	franklin.up()

def pendown():
	print ("Crayon baissé")
	franklin.down()

def couleur():
        CouleurRecup = CouleurWrite.get()   #recupération de la valeur saisie
        print ("Couleur du trait changée. Couleur choisie :", CouleurRecup, "!")
        franklin.color(CouleurRecup)

def repetition():
        RepetitionRecup = RepetitionWrite.get()   #recupération de la valeur saisie
        print ("Nombre de répétition de l'instruction : ", RepetitionRecup, "fois.")
        for i in range(1,int(RepetitionRecup)):
                reception() #Boucle de répétition

BoutonEnvoie = Button(fenetre, text="Envoyer", command=reception).pack()
BoutonReset = Button(fenetre, text="Reset", command=reset).pack()
BoutonPenUp = Button(fenetre, text="Pen Up", command=penup).pack()
BoutonPenDown = Button(fenetre, text="Pen Down", command=pendown).pack()

#Le label pour le choix de la couleur.
text4 = Label(fenetre, text="Si vous voulez modifier la couleur du trait, veuillez la préciser dans l'encart suivant :").pack()
Couleur = StringVar() 
#Récupération de la couleur.
CouleurWrite = Entry(fenetre, textvariable=Couleur, width=6)
CouleurWrite.pack() 
BoutonEnvoie = Button(fenetre, text="Changer la couleur !", command=couleur).pack()

#Le label pour le choix du nombre de répétition
text5 = Label(fenetre, text="Si vous voulez répéter un nombre de fois votre instruction, préciser ce nombre de fois :").pack()
Repetition = StringVar() 
#Récupération du nombre de répétition
RepetitionWrite = Entry(fenetre, textvariable=Repetition, width=6)
RepetitionWrite.pack()
BoutonEnvoie = Button(fenetre, text="Nombre de répétitions !", command=repetition).pack()

turtle.done()
fenetre.mainloop()

#Solène
