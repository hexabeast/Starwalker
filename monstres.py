#monstres.py
import afficheur
import inputs
import carte
import images
import pygame


#Listes des coordonnées des monstres:
x = []
y = []

#Dimensions des monstres:
w = 32
h = 32

#Vitesse des monstres:
vx = []
vy = []

#Accélération en y à appliquer au monstre:
gravite = 800

vitesse = 200

collisionrec= [] #Rectangle de collisions
tourne = False #Variable déterminant si le monstre est retourné
mort = [] #Etat des monstres

#Permet d'intialiser le module "monstres":
def init():
    global vx,vy, h, w, collisionrec, x, y, tourne, img, tempsprecedent, cadence, mort
    x = []
    y = []
    w = 32
    h = 32
    vx = []
    vy = []
    collisionrec= []
    tourne = False
    mort = []

    collisionrec.append((3,5))
    collisionrec.append((w-3,h-1))

#Permet l'ajout d'un monstre aux coordonnées (px,py):
def ajoutermonstre(px,py):
    global vx,vy, collisionrec, x, y, mort, vitesse
    mort.append(False)
    vx.append(vitesse)
    vy.append(0)
    x.append(px)
    y.append(py)

#Permet de supprimer le i-ème monstres de la liste:
def retirermonstre(i):
    x.pop(i)
    y.pop(i)
    vx.pop(i)
    vy.pop(i)
    mort.pop(i)

#Permet l'affichage des monstres et leur mouvement:
def draw(delta):
    global vx,vy,x,y, tourne, img, tempsprecedent, cadence, mort

    for i in range(len(x)-1,-1,-1):
        #On applique les lois de Newton dans un cas de chute libre:
        vy[i]-=gravite*delta

        #Si la vitesse négative est trop élevée, on la limite:
        if vy[i]<-gravite/1.5:
            vy[i] = -gravite/1.5

        oldx = x[i] #On enregistre la dernière position en x
        x[i] += vx[i]*delta #On applique le mouvement en x
        if collision(i) and not mort[i]: #Si il y a collision et que le monstre n'est pas mort
            x[i] = oldx #On annule le déplacement
            vx[i] = -vx[i]#Et on inverse la vitesse du monstre, pour le faire aller dans l'autre sens

        oldy = y[i] #On enregistre la dernière position en y
        y[i] -= vy[i]*delta #On applique le mouvement en y
        if collision(i) and not mort[i]: #Si il y a collision et que le monstre n'est pas mort
            y[i] = oldy #On annule le déplacement
            vy[i] = 0 #Et on remet la vitesse en y à 0
            
            cy = int((y[i]+10+h)/32)
            coldroite = not carte.collision(int((x[i]+w+5)/32),cy)
            colgauche = not carte.collision(int((x[i]-5)/32),cy)
                
            if not (coldroite and colgauche):
                if (coldroite and vx[i]>0) or (colgauche and vx[i]<0):
                    vx[i] = -vx[i]
     
        #Si la vitesse est positive, le monstre regarde à droite, sinon il regarde à gauche:
        if vx[i]>0:
            tourne = False
        else:
            tourne = True

        #On affiche le monstre, orienté dans la bonne direction:
        afficheur.draw(pygame.transform.flip(images.monstre, tourne, False), x[i], y[i])

        #Si le monstre est trop bas, on le supprime:
        if y[i]> carte.h*32+400:
            retirermonstre(i)

#Permet de déterminer si le i-ème monstre est en collision avec le terrain:
def collision(i):
    #On détermine le rectangle de blocs touchant le monstre:
    minx = (int)((x[i]+collisionrec[0][0])/32)
    miny = (int)((y[i]+collisionrec[0][1])/32)
    maxx = (int)((x[i]+collisionrec[1][0])/32)
    maxy = (int)((y[i]+collisionrec[1][1])/32)

    #Puis on parcours toutes les cases du rectangle
    for i in range(minx, maxx+1):
        for j in range(miny, maxy+1):
            # Et si un case est solide, on renvoie qu'il y a eu collision:
            if carte.collision(i,j):
                return True
    #Sinon on renvoie qu'il n'y en a pas eu:
    return False
