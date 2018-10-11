Projects 2016-2017    --    Development   --    Solène . P

# Drarrow

Manuel d’utilisation de # Drarrow
 
## Configuration
  
  •	Versions :

Python : 3.5 
Pygame : 1.9
Imported module : Tkinter.


### PRÉSENTATION DU JEU	
  
  •	Introduction :

Drarrow à pour but de faire des dessins en fonction de ce que nous lui demandons. 

  •	Guides des commandes :

Le jeu se joue avec un clavier AZERTY et un pavé numérique
 
  o	Les déplacements du curseur:

    -	TD : pour aller à droite.
    -	TG : pour aller à gauche
    -	RE : pour aller tout droit.
    -	Les degrés : Indiquer de combien de degrés le curseur doit tourner dans la direction que vous aurez choisie (Sachant que 360° équivalent à un tour complet)
    -	La distance : Indiquer la distance en pixels que le curseur doit parcourir.
    -	Cliquez sur le bouton « Envoyer »

  o	Effacer la feuille en cours :

    -	Cliquez sur le bouton « Reset »
 
Dans l’encart prévu pour, rentrer la couleur de votre choix (en anglais)

   -	blue	pour	« Bleu »
   -	green	pour	« Vert »
   -	yellow	pour	« Jaune »
   -	red	pour	« Rouge »
   -	pink	pour	« Rose »
   -	brown	pour	« Marron »
   -	black	pour	« Noir »
   -	white	pour	« Blanc »
   -	orange	pour	« Orange »
   -	purple	pour	« Violet »
   -	grey	pour	« Gris »

  o	Répéter l’action :

Dans l’encart prévu juste au dessus du bouton « Nombre de répétition », il vous faudra indiquer le nombre de répétitions souhaitées puis d’appuyer sur le bouton « Nombre de répétitions ! »

_____

##	Technical Documentation

###	MOTEUR GRAPHIQUE	
•	Pourquoi « Pygame » ?

Dans ce contexte, nous n’utilisons pas « Pygame » pour son interface graphique. Nous l’utilisons à fin d’avoir accès au module pour la musique, car sur « Tkinter » il est inexistant, ou incomplet (impossibilité de lire de nombreux formats de fichiers).

•	Pourquoi « Tkinter » ?

« Tkinter » nous sert exclusivement d’interface graphique. C’est un module pré implémenté à Python, donc pas besoin de l’installer contrairement à « Pygame » si vous avez déjà une version de Python. Également, il a l’avantage d’être portable, et donc d’être compatible sur tout les OS.
Pour finir, « Tkinter » couplé à la fonction Turtle.py de python permet de dessiner des formes sur l’interface graphique / page que nous propose « Tkinter ».


###	ALGORITHMES
•	Les déplacements du curseur.

Les déplacement du curseur récupérés par l’action d’appuyer sur le bouton « envoyer », ce bouton permet la récupération des informations rentrées par l’utilisateur dans les trois variables :
-	DirectionWrite qui va devenir DirectionRecup pour l’utiliser.
-	AngleWrite qui va devenir AngleRecup pour l’utiliser.
-	DistanceWrite qui va devenir DistanceRecup pour l’utiliser. Grace aux valeurs récupérées nous allons pouvoir utiliser les fonctions « left », « right », « backward », « toward ».


###	LES FONCTIONNALITÉS	

•	Le « Reset »

Le reset était une des fonctionnalitées à implémenter, il permet de repartir de 0, c’est à dire la page blanche, ce afin de recommencer un dessin.
Cette fonctionnalité est gérée par la fonction reset qui est appelé par le bouton du même nom (BoutonReset).
Lorsque l’utilisateur appuie sur ce bouton, le reset est effectué, et on vois dans la colonne un message approuvant cette action : « Reset effectué »


•	Le Changement de couleur

Le changement de couleur est également une fonctionnalité que le sujet prévoyait comme « obligatoire ».
Dans ce projet, cette dernière marche grâce à la fonction
« couleur » notamment, mais également grâce aux label et zone de récupération de valeur.
Ainsi il suffit de rentrer le nom de la couleur que nous voulons attribuer au pinceau (en anglais) et d’appuyer sur le bouton
« Changer la couleur »; pour que celle-ci change. Dés lors on peux voir en console un message indiquant que la couleur a été modifier, et qu’elle couleur l’utilisateur a choisie.


•	Le stylo baissé ou relevé

De la même manière que le « Reset » et le changement de couleur, cette fonctionnalité était une des fonctionnalités de base du projet. Elle fonctionne de la même manière que le « Reset » c’est à dire, un bouton pour « Lever le stylo » et un bouton pour
« Descendre le style ».
Ces deux boutons appellent la fonction qui leur est propre :

-	Le bouton « PenUp » appel la fonction « penup » qui indique que le crayon doit arrêter d’écrire.
-	Le bouton « PenDown » appel la fonction « pendown » qui contrairement à la précédente indique que le crayon doit se remettre à écrire.


•	La répétition d’une action

La répétition d’une action fonctionne de presque de la même manière que les déplacements du curseur :
-	Un texte pour expliquer ce que nous demandons à l’utilisateur.
-	Un champ de texte vide à remplir par l’utilisateur.
-	La	récupération	de	la	valeur	dans	la	valeur
« RepetitionWrite » puis dans RepetitionRecup.
-	On vois s’afficher un message de confirmation dans la console ( Nombre de répétition de l’instruction : »
Néanmoins la suite diffère une fois la valeur récupérée. En effet à partir de là exécutons « x » fois les valeur rentrée par l’utilisateur grâce à un « for » qui va exécuter plusieurs fois la fonction
« Réception » qui nous permettait d’exécuter ce que l’utilisateur demandais une seul et unique fois en appuyant sur le bouton
« Envoyer »


###	BONUS	

•	La musique

C’est le seul moment ou nous allons utiliser Pygame mais ce n’est pas « visible » à l’œil.
La musique se lance dés le lancement du jeu. Et finie à la fin du morceau (elle n’est pas en boucle), on suppose que la musique de Drarrow est suffisante une seule fois.
