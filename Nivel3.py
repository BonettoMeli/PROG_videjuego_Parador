#nivel3
import pygame

class nivel3:
    def __init__(self, pantalla, imagenes, sonidos, botones):
        self.pantalla = pantalla
        self.imagenes = imagenes
        self.sonidos = sonidos
        self.botones = botones

    def dibujar(self, pantalla_actual):
        if pantalla_actual == "ciudad_invertida":
            self.pantalla.blit(self.imagenes.ciudad_invertida, (0, 0))

        elif pantalla_actual == "flechas_ciudad_invertida":
            self.pantalla.blit(self.imagenes.flechas_ciudad_invertida, (0, 0))

        elif pantalla_actual == "camino1":
            self.pantalla.blit(self.imagenes.camino1, (0, 0))
        elif pantalla_actual == "camino2":
            self.pantalla.blit(self.imagenes.camino2, (0, 0))
        elif pantalla_actual == "camino3":
            self.pantalla.blit(self.imagenes.camino3, (0, 0))
        elif pantalla_actual == "camino4":
            self.pantalla.blit(self.imagenes.camino4, (0, 0))
                               