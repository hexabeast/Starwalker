#afficheur.py
import pygame
from pygame.locals import *  # @UnusedWildImport

#Coordonnées de l'afficheur:
x = 0
y = 0

#Polices d'écriture:
font = 0
grosFont = 0

#Variable qui contiendra la fenêtre principale:
window = 0

#On initialise l'afficheur:
def init(px,py):
    global x,y,font,window,grosFont
    x = px
    y = py
    pygame.font.init()
    font = pygame.font.Font("polices/policecarre.ttf", 18)
    grosFont = pygame.font.Font("polices/policecarre.ttf", 32)

#Fonction permettant de donner au module la fenêtre principale:
def mettreWindow(win):
    global window
    window = win

#Fonction permettant de déplacer l'afficheur aux coordonnées (px,py):
def update(px,py):
    global x,y
    x = px
    y = py 

#Fonction permettant d'afficher une texture aux coordonnées (px,py) par rapport à la position de l'afficheur:
def draw(texture,px,py):
    window.blit(texture,(px-x,py-y))

def drawAbs(texture,px,py):
    window.blit(texture,(px,py))

#Fonction permettant d'afficher un texte aux coordonnées (px,py), relativement à l'afficheur ou non:
def drawTexte(text,color,px,py,relative):
    if relative:
        draw(font.render(text, False, (color[0], color[1], color[2])),px,py)
    else:
        window.blit(font.render(text, False, (color[0], color[1], color[2])),(px,py))

#Fonction permettant d'afficher un texte plus petit:
def drawGrosTexte(text,color,px,py,relative):
    if relative:
        draw(grosFont.render(text, False, (color[0], color[1], color[2])),px,py)
    else:
        window.blit(grosFont.render(text, False, (color[0], color[1], color[2])),(px,py))
