#main.py
import pygame
from pygame.locals import *

import afficheur #Module permettant d'afficher les textures au bon endroit
import carte #Module contenant le terrain du jeu
import camera #Module permettant de décaler la zone de rendu
import images #Module permettant de charger les images
import inputs #Module gérant les entrées souris et clavier
import joueur #Module gérant le joueur
import monstres #Module gérant les ennemis
import boulesdefeu #Module gérant les boules de feu lancées par le joueur
import interface #Module gérant l'interface
import bonus #Module gérant les bonus ramassables
import cache #Module gérant le cache (rectangle noir) affiché lors du changement de niveau
import musique #Module gérant les sons du jeu

largeur = 960 #Largeur de la fenêtre
hauteur = 600 #Hauteur de la fenêtre

window = pygame.display.set_mode((largeur, hauteur), HWSURFACE | DOUBLEBUF) #Création de la fenêtre

pygame.mixer.pre_init(44100, -16, 1, 512)#Cette ligne permet de rélger un problème de décalage au niveau du son
pygame.init() # Initialisation de pygame
pygame.display.set_caption("Starwalker")#Permet de mettre le titre de la fenêtre
musique.init()

delta = 0.01 #Variable égale au temps entre deux images, servant à adapter la vitesse
#du jeu pour qu'elle soit toujours identique quel que soit le framerate
deltaMultiplieur = 1 #Permettant de modifier le delta (pour ralentir ou accélérer le temps par exemple)
tempsDerniereImage = 0 #Contient le temps écoulé durant le dernier rendu, permet de calculer le delta

images.init() #On charge toutes les textures du jeu

joueur.init() #On initialise le joueur...
monstres.init()#...les monstres...
boulesdefeu.init()#... et les boules de feu.
bonus.init()

niveaux = ["tutoriel", "niveau1", "niveau2", "niveau3", "fin du jeu"]#Liste des niveaux
niveauActuel = 0 #Niveau dans lequel le joueur se trouve actuellement

interface.init() #Initialisation de l'interface (compteurs de bonus)

carte.init(niveaux[niveauActuel],True) #On charge le terrain du jeu depuis un fichier

cache.init(largeur,hauteur,niveaux[niveauActuel])
#On initialise la camera, la centrant sur le joueur et lui mettant les dimensions de la fenêtre:
camera.init(joueur.x,joueur.y,largeur,hauteur,carte.w*32,carte.h*32)

#On initialise l' "afficheur", qui permettra le rendu des textures à l'écran
afficheur.init(0,0)
afficheur.mettreWindow(window)
afficheur.update(camera.x, camera.y)

musiquelancee = False
end = False

def reinitialiserNiveau():#Permet de réinitialiser tout sauf l'état de la carte
    joueur.init()
    monstres.init()
    boulesdefeu.init()
    bonus.init()
    interface.init()

#Boucle principale:
while end is False:

    if pygame.time.get_ticks() > 2400 and not musiquelancee: #On joue la musique 2,4 secondes après le lancement du jeu, si elle n'a pas déjà été lancée
        musique.play()
        musiquelancee = True
    
    #On dessine l'arriere plan sur l'écran pour nettoyer les anciens rendus:
    window.blit(images.arriere[0],(-2,-2))

    #On met à jour les entrées clavier/souris:
    inputs.update()

    #On calcule le delta:
    t = pygame.time.get_ticks()
    delta = (t - tempsDerniereImage) / 1000.0 * deltaMultiplieur
    tempsDerniereImage = t
    #Et on le limite pour éviter d'aller trop vite en cas de problème:
    if delta>0.05: delta = 0.05
    
    for event in pygame.event.get():
        #Si l'utilisateur ferme la fenêtre, on quitte la boucle principale:
        if event.type == QUIT:
            end = True
        

    #On recentre la caméra sur le joueur:
    camera.automouvement(delta)

    bonus.draw(delta)

    #On affiche les monstres:
    monstres.draw(delta)

    #On affiche le joueur en arrière plan s'il est en vie:
    if not joueur.mort: joueur.draw(delta)
    
    #Puis les boules de feu:
    boulesdefeu.draw(delta)

    #Si le joueur tombe trop bas, on réinitialise le jeu:
    if joueur.y > carte.h*32+400 or inputs.rclic:
        reinitialiserNiveau()
        carte.init(niveaux[niveauActuel],False)
        camera.updateTailleMap(carte.w, carte.h)

    #Si le joueur arrive à la fin du niveau
    if joueur.x>carte.w*32+100:

        #Lorsque le joueur arrive à la fin, on commence le fondu vers le prochain niveau
        if not cache.commence:
            niveauActuel+=1
            cache.commencer(niveaux[niveauActuel])

        #Lorsque l'écran est entièrement noir, on passe au niveau suivant en réinitialisant toutes les valeurs.
        if cache.fin:
            reinitialiserNiveau()
            carte.init(niveaux[niveauActuel],True)
            camera.updateTailleMap(carte.w, carte.h)
            cache.commence = False

    #On donne à l'afficheur les coordonnées de la caméra:
    afficheur.update(camera.x, camera.y)
    carte.draw(delta)

    #On affiche le joueur en premier plan s'il est mort:
    if joueur.mort: joueur.draw(delta)

    #On affiche l'interface (les compteurs de bonus)
    interface.draw()

    #On affiche le "cache", le plus souvent transparent mais qui devient noir et affiche le nom du prochain niveau en cas de changement de niveau.
    cache.draw(delta)
    
    #On termine le rendu:
    pygame.display.flip()

#Si on sort de la boucle principale, alors on quitte le programme:
pygame.quit()
