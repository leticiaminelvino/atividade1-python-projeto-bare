"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 21:
Faça um programa Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame
pygame.mixer.init()
pygame.mixer.music.load('jogomario.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
