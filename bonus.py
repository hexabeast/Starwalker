#bonus.py
import afficheur
import pygame
import images
import joueur
import interface
import musique

bonusbloc = []
bonusfeu = []
bonuscasse = []
offy = 2
descendre = True
taille = 16

def init():
    global bonusbloc, bonusfeu, bonuscasse
    bonusbloc = []
    bonusfeu = []
    bonuscasse = []

#Ajoute un bonus "boule de feu"
def ajouterfeu(x,y):
    global bonusfeu
    bonusfeu.append((x,y));

#Ajoute un bonus "Roche"
def ajouterbloc(x,y):
    global bonusbloc
    bonusbloc.append((x,y));

#Ajoute un bonus "Marteau"
def ajoutercasse(x,y):
    global bonuscasse
    bonuscasse.append((x,y));

#Permet l'affichage et le mouvement vertical des bonus
def draw(delta):
    global descendre, bonusbloc, bonusfeu, offy, bonuscasse
    for i in range(len(bonusbloc)-1,-1,-1):
        afficheur.draw(pygame.transform.scale(images.bloc[0], (taille,taille)), bonusbloc[i][0]*32+8, bonusbloc[i][1]*32+offy)
        if collisionJoueur(bonusbloc[i][0],bonusbloc[i][1]):
            interface.bonusbloc+=1
            bonusbloc.pop(i)
            musique.bonus.play()
        
    for i in range(len(bonusfeu)-1,-1,-1):
        afficheur.draw(images.boule, bonusfeu[i][0]*32+8, bonusfeu[i][1]*32+offy)
        if collisionJoueur(bonusfeu[i][0],bonusfeu[i][1]):
            interface.bonusfeu+=1
            bonusfeu.pop(i)
            musique.bonus.play()

    for i in range(len(bonuscasse)-1,-1,-1):
        afficheur.draw(images.casse, bonuscasse[i][0]*32+8, bonuscasse[i][1]*32+offy)
        if collisionJoueur(bonuscasse[i][0],bonuscasse[i][1]):
            interface.bonuscasse+=1
            bonuscasse.pop(i)
            musique.bonus.play()

    if descendre:
        offy+=delta*0.6*(8+max((14-offy)*(offy-2),0))
        if offy>14:
            descendre = False
    else:
        offy-=delta*0.6*(8+max((14-offy)*(offy-2),0))
        if offy<2:
            descendre = True

def collisionJoueur(x,y): #Permet de déterminer si il y a une collision avec le joueur aux coordonnées (x;y)
    minx = joueur.collisionrec[0][0]+joueur.x
    miny = joueur.collisionrec[0][1]+joueur.y
    maxx = joueur.collisionrec[1][0]+joueur.x
    maxy = joueur.collisionrec[1][1]+joueur.y
    x*=32
    y*=32

    if not(x+8>maxx or x+24<minx or y+8>maxy or y+24< miny):
        return True
    return False
        

    
