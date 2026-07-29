import pygame
import sys

jardin = pygame.image.load("visual/lenguas_muertas2.jpg")
invernadero = pygame.image.load("visual/invernadero_adentro.jpg")
cofre = pygame.image.load("visual/cofre_lengua1.jpeg")
cofre_abierto = pygame.image.load("visual/cofre_lengua2.jpeg")
afuera = pygame.image.load("visual/tren_lengua_abierto.png")

jardin = pygame.transform.scale(jardin, (1400, 800))
invernadero = pygame.transform.scale(invernadero, (1400, 800))
cofre = pygame.transform.scale(cofre, (1400, 800))
cofre_abierto = pygame.transform.scale(cofre_abierto, (1400, 800))
afuera = pygame.transform.scale(afuera, (1400, 800))

flecha_centro = pygame.Rect(620, 250, 140, 220)
flecha_centro2 = pygame.Rect(620, 250, 140, 220)

flecha_derecha = pygame.Rect(1220, 280, 180, 220)
flecha_izquierda = pygame.Rect(0, 280, 180, 220)
flecha_abajo = pygame.Rect(620, 430, 120, 140)
flecha_abajo2 = pygame.Rect(620, 430, 120, 140)

pantalla_actual_n1 = "jardin"

def dibujar(pantalla):
    global pantalla_actual_n1

    if pantalla_actual_n1 == "jardin":
        pantalla.blit(jardin,(0,0))
    elif pantalla_actual_n1 == "invernadero":
        pantalla.blit(invernadero,(0,0))
    elif pantalla_actual_n1 == "cofre":
        pantalla.blit(cofre,(0,0))
    elif pantalla_actual_n1 == "cofre_abierto":
        pantalla.blit(cofre_abierto,(0,0))
    elif pantalla_actual_n1 == "afuera":
        pantalla.blit(afuera,(0,0))

def eventos(evento):
    global pantalla_actual_n1

    if evento.type == pygame.MOUSEBUTTONDOWN:

        if pantalla_actual_n1 == "jardin":

            if flecha_centro.collidepoint(evento.pos):
                pantalla_actual_n1 = "invernadero"

            elif flecha_derecha.collidepoint(evento.pos):
                pantalla_actual_n1 = "cofre"

        elif pantalla_actual_n1 == "invernadero":

            if flecha_abajo.collidepoint(evento.pos):
                pantalla_actual_n1 = "jardin"