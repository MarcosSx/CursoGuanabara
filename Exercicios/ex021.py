# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# DEU RUIM
from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()

parar = input('a')
