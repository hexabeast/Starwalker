#carte.py
import afficheur
import inputs
import carte
import images
import pygame
import monstres
import boulesdefeu
import interface
import musique

#Coordonnées du joueur:
x = 64
y = 128

#Dimensions du joueur:
w = 40
h = 60

#Vitesse du joueur:
vx = 0
vy = 0

#Accélération en y à appliquer au joueur:
gravite = 1200

vitesse = 300

collisionrec= [] #Rectangle de collisions
tourne = False #Variable déterminant si le joueur est retourné
img = 0 #Image actuelle du joueur (servant pour l'animation des mouvements)
tempsprecedent = 0 #Dernier changement d'image
cadence = 50 #Cadence de changement d'image en ms
mort = False #Etat du joueur
gagne = False


#Permet d'intialiser le module "joueur":
def init():
    global vx,vy, w, h, collisionrec, x, y, tourne, img, tempsprecedent, cadence, mort, gagne
    x = 64
    y = 128
    w = 40
    h = 60
    collisionrec= []
    tourne = False
    img = 0
    tempsprecedent = 0
    cadence = 50
    mort = False
    gagne = False
    
    collisionrec.append((10,15))
    collisionrec.append((w-10,h-1))

#Permet de déterminer si le joueur touche un monstre
def touchemonstre():
    global collisionrec, x, y
    minx = collisionrec[0][0]+x
    miny = collisionrec[0][1]+y
    maxx = collisionrec[1][0]+x
    maxy = collisionrec[1][1]+y
    for i in range(len(monstres.x)):
        #Si le joueur et le monstre se superposent, et si le monstre n'est pas mort, on retourne "True"
        if not (monstres.mort[i] or minx > monstres.x[i] + monstres.w or maxx < monstres.x[i] or miny > monstres.y[i] + monstres.h or maxy < monstres.y[i]):
            musique.degats.play()
            return True
    return False

#Permet l'affichage et le déplacement du joueur:
def draw(delta):
    global vx,vy,x,y, tourne,vitesse, gagne, img, tempsprecedent, cadence, mort

    #On applique les lois de Newton dans un cas de chute libre:
    vy-=gravite*delta

    #Si la vitesse négative est trop élevée, on la limite:
    if vy<-gravite*2/3:
        vy = -gravite*2/3

    if (inputs.droite or gagne) and not mort:
        vx = vitesse
    elif inputs.gauche and not mort:
        vx = -vitesse
    elif not mort:
        vx = 0

    oldx = x #On enregistre la dernière position en x
    x += vx*delta #On applique le mouvement en x
    if collision() and not mort and not gagne: #Si il y a collision et que le joueur n'est pas mort/n'a pas gagné
        x = oldx #On annule le déplacement

    oldy = y #On enregistre la dernière position en y
    y -= vy*delta #On applique le mouvement en y
    if collision() and not mort: #Si il y a collision
        y = oldy #On annule le déplacement
        if inputs.espace and vy<0: #Si espace est pressée, on fait sauter le personnage
            vy = vitesse*2
            musique.sauter.play()
        else:vy = 0 #Sinon on annule sa vitesse en y

    if vy > 0:
        img = len(images.joueur)-1
    elif vy < -50:
        img = len(images.joueur)-2
    elif vx != 0:
        if pygame.time.get_ticks()-tempsprecedent>cadence:
            tempsprecedent = pygame.time.get_ticks()
            img+=1
            if img>len(images.joueur)-3:
                img = 1
    else:
        img = 0
    
    if vx>0:
        tourne = False
    elif vx<0:
        tourne = True

    #Si le joueur appuie sur E et qu'il peut lancer une boule de feu, il en lance une
    if inputs.eclic and not (mort or gagne) and interface.bonusfeu>0:
        boulesdefeu.ajouterboule(x+w/2, y+h/2, not tourne)
        interface.bonusfeu-=1
        musique.lancer.play()

    #Si le joueur clique droit et qu'il peut poser un blox, il en pose un
    if inputs.sourisdroite and not (mort or gagne) and interface.bonusbloc>0:
        if carte.poserRoche(int(inputs.sourispos[0]/32), int(inputs.sourispos[1]/32)):
            interface.bonusbloc-=1
            musique.poser.play()

    #Si le joueur clique gauche et qu'il peut casser un bloc, il en casse un
    if inputs.sourisgauche and not (mort or gagne) and interface.bonuscasse>0:
        if carte.casserRoche(int(inputs.sourispos[0]/32), int(inputs.sourispos[1]/32)):
            interface.bonuscasse-=1
            musique.casser.play()
            
    if not mort and touchemonstre():
        mort = True
        vx = 60
        vy = 400

    if int(x/32)>=carte.w-15:
        gagne = True
        
    afficheur.draw(pygame.transform.flip(images.joueur[img],tourne,False), x, y)

#Permet de déterminer si le joueur est en collision avec le terrain:
def collision():
    #On détermine le rectangle de blocs touchant le joueur
    minx = (int)((x+collisionrec[0][0])/32)
    miny = (int)((y+collisionrec[0][1])/32)
    maxx = (int)((x+collisionrec[1][0])/32)
    maxy = (int)((y+collisionrec[1][1])/32)

    #Puis on parcours toutes les cases du rectangle
    for i in range(minx, maxx+1):
        for j in range(miny, maxy+1):
            # Et si un case est solide, on renvoie qu'il y a eu collision:
            if carte.collision(i,j):
                return True
    return False
