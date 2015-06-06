#interface.py
import afficheur
import images
import pygame

bonusbloc = 0
bonusfeu = 0
bonuscasse = 0

textes = []

def init():
    global bonusbloc, bonusfeu, bonuscasse, textes
    bonusbloc = 0
    bonusfeu = 0
    bonuscasse = 0
    textes = []

def ajouterTexte(texte, x, y):
    textes.append([texte,x,y])

def draw():
	#On affiche les textes du tutoriel:
    for i in range(len(textes)):
        afficheur.drawGrosTexte(textes[i][0],(255,255,255),textes[i][1],textes[i][2],True)
    
	#On affiche le nombre de bonus restant en haut à gauche de l'écran
    afficheur.drawAbs(pygame.transform.scale(images.bloc[0], (16,16)),20,20)
    afficheur.drawTexte("x "+str(bonusbloc),(255,255,255),40, 18, False)
    afficheur.drawAbs(images.boule,20,45)
    afficheur.drawTexte("x "+str(bonusfeu),(255,255,255),40, 43, False)
    afficheur.drawAbs(images.casse,20,70)
    afficheur.drawTexte("x "+str(bonuscasse),(255,255,255),40, 68, False)

