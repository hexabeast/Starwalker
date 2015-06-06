#musique.py
import pygame
from pygame.mixer import Sound
poser = 0
casser = 0
degats = 0
sauter = 0
lancer = 0
bonus = 0

def init():
    global poser, casser, sauter, lancer, degats, bonus
    pygame.mixer.init()
    pygame.mixer.music.load("musiques/musique1.mp3")
    poser = Sound("sons/poser.wav")
    casser = Sound("sons/casser.wav")
    sauter = Sound("sons/sauter.wav")
    degats = Sound("sons/degats.wav")
    bonus = Sound("sons/bonus.wav")
    lancer = Sound("sons/lancer.wav")

def play():
    pygame.mixer.music.play(-1)

def fin():
    pygame.mixer.music.fadeout(6000)
