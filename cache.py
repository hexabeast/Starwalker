#cache.py
import afficheur
import pygame
import musique

texte = ""
tempsDebut = 0
attente = 500
fin = False
commence = False
opacite = 1.0 #Définit l'opacité du cache noir
opaciteTexte = 0 #Définit l'opacité du texte
rectangle = 0 #Rectangle qui contiendra les dimensions du cache noir
largeur = 0 #Largeur de la fenetre
hauteur = 0 #Hauteur de la fenetre
findujeu = False

def init(w,h,text):
    global rectangle, tempsDebut, largeur, hauteur
    largeur = w
    hauteur = h
    texte = text
    mettreTexte(text)
    rectangle = pygame.Surface((w+4,h+4))
    rectangle.fill((0,0,0))
    tempsDebut = pygame.time.get_ticks()-attente
    
#Initialise l'opacification du cache en vue du changement de niveau
def commencer(text):
    global fin, tempsDebut, opacite, opaciteTexte, commence, findujeu

    if text == "fin du jeu":
        findujeu = True
        musique.fin()
    
    mettreTexte(text)
    fin = False
    commence = True
    tempsDebut = pygame.time.get_ticks()
    opacite = 0
    opaciteTexte = 0

#Permet de définir le texte à afficher en fonction du nom du niveau
def mettreTexte(text):
    global texte
    if text=="tutoriel" or text=="fin du jeu":
        texte = text
    else:    
        texte = text[:len(text)-1]+" "+text[len(text)-1]

#Permet l'affichage et la mise à jour du cache
def draw(delta):
    global texte, fin,findujeu, tempsDebut, opacite, opaciteTexte, largeur, hauteur, rectangle
    if tempsDebut+attente*6>pygame.time.get_ticks() or findujeu:

        ### Fondu du rectangle
        if not fin and tempsDebut+attente*3<pygame.time.get_ticks() and not findujeu:
            fin = True

        if opacite<1 and tempsDebut+attente*3>pygame.time.get_ticks():
            opacite+=delta/(attente/1000)
            if opacite>1:opacite=1

        if opacite>0 and tempsDebut+attente*5<pygame.time.get_ticks() and not findujeu:
            opacite-=delta/(attente/1000)
            if opacite<0:opacite=0
        ###

        #Application de l'opacité sur le rectangle
        rectangle.set_alpha(opacite*255)

        # Affichage du rectangle(cache)
        afficheur.drawAbs(rectangle,-2,-2)

        ### Fondu du texte
        if tempsDebut+attente<pygame.time.get_ticks() and (tempsDebut+5*attente>pygame.time.get_ticks() or findujeu):
            if opaciteTexte<1 and tempsDebut+attente*3>pygame.time.get_ticks():
                opaciteTexte+=delta/(attente/1000)
                if opaciteTexte>1:opaciteTexte=1

            if opaciteTexte>0 and tempsDebut+attente*4<pygame.time.get_ticks() and not findujeu:
                opaciteTexte-=delta/(attente/1000)
                if opaciteTexte<0:opaciteTexte=0
            taille = afficheur.grosFont.size(texte)
            afficheur.drawGrosTexte(texte,(opaciteTexte*255,opaciteTexte*255,opaciteTexte*255),largeur/2-taille[0]/2, hauteur/2-taille[1]/2, False)
        ###
