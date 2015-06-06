#inputs.py
import pygame
from pygame.locals import *
from pygame.math import Vector2
import camera

# Booléens qui serviront au déplacement du personnage:
haut = False
bas = False
gauche = False
droite = False
espace = False

# Position de la souris:
sourispos = (0,0)

# Booléens qui serviront à déterminer les clics de souris:
sourisgauche = False
sourisclicgauche = False
sourisdroite = False
sourisclicdroit = False
e = False
r = False
eclic = False
rclic = False
def update():
    global haut, bas, gauche, droite, espace, r, rclic, e, eclic, sourispos, sourisgauche, sourisdroite, sourisclicgauche, sourisclicdroit
    
    key = pygame.key.get_pressed() 

    # On détermine les directions activées par les entrées clavier:
    if key[K_DOWN] or key[K_s]:
        bas = True
    else:bas = False
    
    if key[K_UP] or key[K_w]: 
        haut = True
    else:haut = False
    
    if key[K_LEFT] or key[K_a] or key[K_q]:
        gauche = True
    else:gauche = False
    
    if key[K_RIGHT] or key[K_d]:
        droite = True
    else:droite = False

    if key[K_SPACE] or key[K_UP] or key[K_w] or key[K_z]:
        espace = True
    else:espace = False

    if key[K_e] and not e:
        eclic = True
    else:eclic = False

    if key[K_e]:
        e = True
    else:e = False

    if key[K_r] and not r:
        rclic = True
    else:rclic = False

    if key[K_r]:
        r = True
    else:r = False
    

    # On assigne aux variables "sourisclicgauche" et "sourisclicdroit" la valeur
    # "True" si le joueur à cliqué sur la souris mais que ce n'était pas le cas lors
    # du dernier calcul:
    if not sourisgauche and pygame.mouse.get_pressed()[0]:
        sourisclicgauche = True
    else:
        sourisclicgauche = False

    if not sourisdroite and pygame.mouse.get_pressed()[1]:
        sourisclicdroit = True
    else:
        sourisclicdroit = False

    # On assigne à ces variables l'état des boutons de souris:
    sourisgauche = pygame.mouse.get_pressed()[0]
    sourisdroite = pygame.mouse.get_pressed()[2]

    # On enregistre les coordonnées de la souris relativement à la position de la caméra:    
    sourispos = (pygame.mouse.get_pos()[0]+camera.x, pygame.mouse.get_pos()[1]+camera.y)
    
