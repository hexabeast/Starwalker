#images.py
import pygame

#Variables qui contiendront les textures:
herbe = []
terre = []
bloc = []
joueur = []
monstre = 0
boule = 0
casse = 0
arriere = []

#Permet de charger les texture en les redimensionnant si besoin:
def init():
    global herbe, terre, bloc, joueur, monstre, boule, arriere, casse

    arriere.append(pygame.image.load("images/arriere.png").convert_alpha())
    arriere.append(pygame.transform.scale(pygame.image.load("images/arrieretoiles.png").convert_alpha(), (1000, 700)))
    
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu1.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu2.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu3.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu4.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu5.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleuCote.png").convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/blocBleuCote.png"),True,False).convert_alpha(), (32, 32)))
    herbe.append(pygame.transform.scale(pygame.image.load("images/blocBleu2Cote.png").convert_alpha(), (32, 32)))
	
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGris1.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGris2.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGris3.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGris4.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGris5.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.image.load("images/blocGrisCote.png").convert_alpha(), (32, 32)))
    terre.append(pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/blocGrisCote.png"),True,False).convert_alpha(), (32, 32)))
    
    bloc.append(pygame.transform.scale(pygame.image.load("images/bloc.png").convert_alpha(), (32, 32)))
    bloc.append(pygame.transform.scale(pygame.image.load("images/bloc2.png").convert_alpha(), (32, 32)))
    bloc.append(pygame.transform.scale(pygame.image.load("images/bloc3.png").convert_alpha(), (32, 32)))
    bloc.append(pygame.transform.scale(pygame.image.load("images/bloc4.png").convert_alpha(), (32, 32)))
    bloc.append(pygame.transform.scale(pygame.image.load("images/bloc5.png").convert_alpha(), (32, 32)))

    #Le personnage du joueur est constitué de plusieurs textures, afin d'être animé:
    joueur.append(pygame.transform.scale(pygame.image.load("images/Persobougepas.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso1.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso2.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso3.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso4.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso5.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso6.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso7.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso8.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso4.png").convert_alpha(), (40, 60)))
    joueur.append(pygame.transform.scale(pygame.image.load("images/Perso3.png").convert_alpha(), (40, 60)))
    monstre = (pygame.transform.scale(pygame.image.load("images/monstre.png").convert_alpha(), (32, 32)))
    boule = (pygame.transform.scale(pygame.image.load("images/boule.png").convert_alpha(), (16, 16)))
    casse = (pygame.transform.scale(pygame.image.load("images/casse.png").convert_alpha(), (16, 16)))
