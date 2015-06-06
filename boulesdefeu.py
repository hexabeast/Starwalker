#boulesdefeu.py
import afficheur
import inputs
import carte
import images
import pygame
import monstres
import musique

#Listes des coordonnées des boules de feu:
x = []
y = []

#Dimensions des boules de feu:
w = 16
h = 16

#Vitesse des boules de feu:
vx = []
vy = []

#Accélération en y à appliquer au monstre:
gravite = 1000

collisionpoint = (w/2, h/2)#Point de collision
mort = [] #Etats des boules de feu
duree = [] #Ages des boules de feu
tempsdevie = 7000 #Durée de vie des boules de feu

#Permet d'intialiser le module "boulesdefeu":
def init():
    global vx,vy, h, w, collisionpoint, x, y, tourne, mort, duree
    x = []
    y = []
    w = 16
    h = 16
    vx = []
    vy = []
    collisionpoint = (w/2, h/2)
    tourne = False
    mort = []
    duree = []
    tempsdevie = 7000

#Permet l'ajout d'une boule de feu aux coordonnées (px,py) avec la direction voulue:
def ajouterboule(px,py, direction):
    global vx,vy, collisionpoint, x, y, mort
    if direction:
        vx.append(350)
    else:
        vx.append(-350)
    vy.append(0)
    x.append(px)
    y.append(py)
    duree.append(pygame.time.get_ticks())
    mort.append(False)

#Permet de supprimer la i-ème boule de feu de la liste:
def retirerboule(i):
    x.pop(i)
    y.pop(i)
    vx.pop(i)
    vy.pop(i)
    duree.pop(i)
    mort.pop(i)

#Fonction retournant le nombre du monstre touché, ou -1 si aucun monstre n'est touché:
def touchemonstre(j):
    global collisionpoint, x, y
    for i in range(len(monstres.x)):
        if not monstres.mort[i] and collisionpoint[0]+x[j]>= monstres.x[i] and collisionpoint[1]+y[j] >= monstres.y[i] and collisionpoint[0]+x[j] <= monstres.x[i]+monstres.w and collisionpoint[1]+y[j] <= monstres.y[i] + monstres.h:
            monstres.vy[i] = 120
            monstres.vx[i] /= 2
            return i
    return -1

#Permet l'affichage des boules de feu et leur mouvement:
def draw(delta):
    global vx,vy,x,y, tourne, img, tempsprecedent, cadence, mort

    for i in range(len(x)-1, -1, -1): #Pour chaque monstre:

        #On applique les lois de Newton dans un cas de chute libre:
        vy[i]-=gravite*delta

        #Si la vitesse négative est trop élevée, on la limite:
        if vy[i]<-gravite/2:
            vy[i] = -gravite/2

        oldx = x[i] #On enregistre la dernière position en x
        x[i] += vx[i]*delta #On applique le mouvement en x
        if collision(i): #Si il y a collision
            x[i] = oldx #On annule le déplacement
            vx[i] = -vx[i]#Et on inverse la vitesse de la boule en x, pour la faire rebondir sur les murs

        oldy = y[i] #On enregistre la dernière position en y
        y[i] -= vy[i]*delta #On applique le mouvement en y
        if collision(i): #Si il y a collision
            y[i] = oldy #On annule le déplacement
            vy[i] = -vy[i] #Et on inverse la vitesse de la boule en y, pour la faire rebondir sur le sol
            
        cible = touchemonstre(i) #On détermine si un monstre est touché par la boule de feu
        afficheur.draw(images.boule, x[i], y[i]) #On affiche la boule

        
        if cible != -1: #Si un monstre est touché
            retirerboule(i) #On supprime la boule
            musique.degats.play()
            monstres.mort[cible] = True # Et on tue le monstre

        #Sinon si la durée de vie de la boule est écoulée, on la supprime:
        elif pygame.time.get_ticks()-duree[i]>tempsdevie or y[i]> carte.h*32+400:
            retirerboule(i)
        
        
#Permet de déterminer si la i-ème boule de feu est en collision avec le terrain:
def collision(i):
    if carte.collision(int((x[i]+collisionpoint[0])/32), int((y[i]+collisionpoint[1])/32)):
        return True
    return False
