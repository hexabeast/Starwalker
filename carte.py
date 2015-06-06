#carte.py
import images
import afficheur
import monstres
import camera
import joueur
import bonus
from random import randint
import interface

'''La carte est constituée d'une grille nommée "blocs" de w*h cases,
chacune d'entre elles ayant un numéro indiquant
le matériau qui lui est associé'''

blocs = 0
h = 0
w = 0

# Permet de charger la carte à partir d'un fichier:
def Charger(nom, estnouveau):
    global blocs, w, h
    
    f = open("niveaux/"+nom, 'r') # On ouvre le fichier
    
    tblocs = []# On crée une liste de listes de blocs temporaire
    
    for ligne in f:# Pour chaque ligne du fichier
        tblocs.append([]) #On ajoute une liste vide à la liste principale
        for n in ligne.split(","):  #Puis pour chaque nombre n entouré de virgules
            tblocs[len(tblocs)-1].append(int(n)) #On ajoute n à la liste créée 2 lignes au dessus

    f.close()
    
    #On détermine la largeur et la hauteur de la carte par rapport aux informations du fichier:
    h = len(tblocs)
    w = len(tblocs[0])

    #On assigne à la liste de blocs les valeurs de la liste temporaire, en les transformant aléatoirement s'il s'agit
    #de blocs existants en plusieurs exemplaires:
    blocs = [[0 for x in range(h)] for x in range(w)]
    for i in range(len(blocs)):
        for j in range(len(blocs[0])):
            if tblocs[j][i]==1: #Si c'est un bloc gris
                difdessous = j<len(tblocs)-1 and tblocs[j+1][i] != 1 #Variable déterminant si le bloc au dessus est different
                
                if difdessous and i<len(tblocs[0])-1 and tblocs[j][i+1] != 1: blocs[i][j] = 33
                elif difdessous and i>0 and tblocs[j][i-1] != 1 : blocs[i][j] = 34
                else: blocs[i][j] = randint(15,19)
                
            elif tblocs[j][i]==2: #Si c'est un bloc de surface  gris/bleu

                difdroite  = i<len(tblocs[0])-1 and tblocs[j][i+1] != 2 #Variable déterminant si le bloc de droite est different
                difgauche = i>0 and tblocs[j][i-1] != 2 #Variable déterminant si le bloc de gauche est different

                if difdroite and difgauche: blocs[i][j] = 35
                elif difdroite: blocs[i][j] = 31
                elif  difgauche: blocs[i][j] = 32
                else: blocs[i][j] = randint(20,24)
                
            elif tblocs[j][i]==3: #Si c'est un bloc "roche"
                blocs[i][j] = randint(25,29)
                
            elif tblocs[j][i]==5: #Si c'est le point d'apparition du joueur
                joueur.x = i*32
                joueur.y = j*32
                if estnouveau:
                    camera.mettrePosition(i*32,j*32)
                blocs[i][j] = 0
                
            elif tblocs[j][i]==6: #Si c'est un point d'apparition du bonus "bloc"
                bonus.ajouterbloc(i,j)
                blocs[i][j] = 0
                
            elif tblocs[j][i]==7: #Si c'est un point d'apparition du bonus "boule de feu"
                bonus.ajouterfeu(i,j)
                blocs[i][j] = 0
                
            elif tblocs[j][i]==8: #Si c'est un point d'apparition du bonus "pioche"
                bonus.ajoutercasse(i,j)
                blocs[i][j] = 0
                
            elif tblocs[j][i] == 100:   
                interface.ajouterTexte("Appuyez sur E pour utiliser les boules de feu",i*32,j*32)
                blocs[i][j] = 0
                
            elif tblocs[j][i] == 101:
                interface.ajouterTexte("Appuyez sur le clic droit de la souris",i*32,j*32)
                interface.ajouterTexte("pour utiliser les roches de construction",i*32-5,j*32+50)
                blocs[i][j] = 0
                
            elif tblocs[j][i] == 102:
                interface.ajouterTexte("Appuyez sur le clic gauche de la souris",i*32,j*32)
                interface.ajouterTexte("pour utiliser la destruction de roche",i*32+5,j*32+50)
                blocs[i][j] = 0
                
            elif tblocs[j][i] == 104:
                interface.ajouterTexte("Utilisez les touches Q et D ou les fleches pour bouger",i*32,j*32)
                interface.ajouterTexte("Appuyez sur espace ou la fleche du haut pour sauter",i*32,j*32+50)
                interface.ajouterTexte("Si vous etes bloque, appuyez sur R pour reessayer",i*32,j*32+100)
                blocs[i][j] = 0
                
            elif tblocs[j][i] == 4: #Si c'est un point d'apparition d'un monstre
                blocs[i][j] = 0
                monstres.ajoutermonstre(32*i,32*j)
            else:
                blocs[i][j] = tblocs[j][i]
            
def poserRoche(x,y):
    if x>=0 and y>=0 and x<w and y<h:
        if blocs[x][y] == 0:
            blocs[x][y] =  randint(25,29)
            passer = True
            for i in range(len(monstres.x)):
                if monstres.collision(i):
                    passer = False

            if joueur.collision():
                passer = False
                
            if not passer:
                blocs[x][y] = 0
                return False
            else:
                return True
    return False
            

def casserRoche(x,y):
    if x>=0 and y>=0 and x<w and y<h:
        if blocs[x][y] >= 25 and blocs[x][y] < 30:
            blocs[x][y] =  0
            return True
    return False
    
#Permet d'initialiser la carte:
def init(nomNiveau, estnouveau):
    global blocs, w, h
    blocs = 0
    h = 0
    w = 0
    Charger(nomNiveau,estnouveau)

#Permet d'afficher la carte:
def draw(delta):
    global blocs, w, h

    #On détermine les cases à afficher:
    maxx = min(int((camera.x+camera.w)/32)+1,w)
    maxy = min(int((camera.y+camera.h)/32)+1,h)
    minx = max(int((camera.x)/32)-1,0)
    miny = max(int((camera.y)/32)-1,0)

    #Puis on parcourt ces cases:
    for i in range(minx, maxx):
        for j in range(miny, maxy):

            
            if blocs[i][j] == 33:
                afficheur.draw(images.terre[len(images.terre)-2], i*32, j*32)
            elif blocs[i][j] == 34:
                afficheur.draw(images.terre[len(images.terre)-1], i*32, j*32)
            elif blocs[i][j] == 31:
                afficheur.draw(images.herbe[len(images.herbe)-3], i*32, j*32)
            elif blocs[i][j] == 32:
                afficheur.draw(images.herbe[len(images.herbe)-2], i*32, j*32)
            elif blocs[i][j] == 35:
                afficheur.draw(images.herbe[len(images.herbe)-1], i*32, j*32)
            elif blocs[i][j] >= 25:# Si la case est dans la tranche des numéros des blocs de bois, on affiche le bloc correspondant
                afficheur.draw(images.bloc[blocs[i][j]-25], i*32, j*32)
            elif blocs[i][j] >= 20:# Idem pour l'herbe
                afficheur.draw(images.herbe[blocs[i][j]-20], i*32, j*32)
            elif blocs[i][j] >= 15: # Idem pour la terre
                afficheur.draw(images.terre[blocs[i][j]-15], i*32, j*32)
            

            

#Permet de déterminer si le bloc situé aux coordonnées (x,y) est solide:
def collision(x,y):
    if x>= 0 and x<w and y>=0 and y<h: #Si le bloc recherché appartient à la carte:
        #Si son numéro est différent de celui de l'air, alors on retourne que le bloc est solide
        if blocs[x][y] != 0:
            return True
    #Si la case recherchée est hors de la carte mais pas dessous, on retourne qu'il y a collision:
    elif x>=w and y>=0 and y<h:
        return blocs[w-1][y]

    elif y<h:
        return True

    #Si la fonction  n'a toujours pas retourné vrai, alors le bloc recherché est forcément de l'air:
    return False
