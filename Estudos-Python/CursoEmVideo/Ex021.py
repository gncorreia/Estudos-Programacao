# Faça um programa em Python que abra e reproduza o audio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('a.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass


