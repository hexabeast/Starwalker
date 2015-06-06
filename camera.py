#camera.py
import inputs
import joueur
#Coordonnées de la camera:
x = 0
y = 0
#Dimensions du champ de vision la camera (w = largeur, h = longueur):
w = 0
h = 0
#Limites de la caméra (qui seront les limites de la carte)
limx = 0
limy = 0
#Initialisation:
def init(px,py,pw,ph,plimx,plimy):
    global x,y,w,h,limx,limy
    x = px
    y = py
    w = pw
    h = ph
    limx = plimx
    limy = plimy
        
def updateTailleMap(lo,ha):
    global limx,limy
    limx = lo*32
    limy = ha*32
#Fonction permettant de faire bouger la caméra aux coordonnées (px,py)
def mettrePosition(px,py):
    global x,y,w,h,limx,limy
    
    #Si la coordonnée x n'est pas hors limites, on l'applique:
    if px<limx-w and px>0:
        x = px
    #Sinon on place la caméra à l'extremum correspondant:
    elif px<=0:
        x = 0
    elif px>=limx-w:
        x = limx-w
    #Idem qu'avant mais pour y:
    if py<limy-h and py>0:
        y = py
    elif py<=0:
        y = 0
    elif py>=limy-h:
        y = limy-h

#Fonction permettant de déplacer la caméra en la décalant de px en x et py en y:
def mouvement(px,py):
    global x,y
    x+=px
    y+=py
    mettrePosition(x,y)

#Fonction permettant de centrer la caméra vers le joueur:    
def automouvement(delta):     
    mettrePosition( x+(((joueur.x+joueur.w/2)-w/2)-x)*delta*6, y+(((joueur.y+joueur.h/2)-h/2)-y)*delta*6)
