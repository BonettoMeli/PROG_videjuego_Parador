#nivel3
import pygame

class nivel3:
    def __init__(self, pantalla, imagenes, sonidos, botones, Juego):
        self.pantalla = pantalla
        self.imagenes = imagenes
        self.sonidos = sonidos
        self.botones = botones
        self.juego = Juego

        self.tiempo_maquinista3 = 0
        self.tiempo_gracias3 = 0
        self.tiempo = 0
        self.tiempo_escena_sin_brujula = 0
        

    def dibujar(self, pantalla_actual):
        if pantalla_actual == "ciudad_invertida":
            self.pantalla.blit(self.imagenes.ciudad_invertida, (0, 0))
        elif pantalla_actual == "tren_afuera":
            self.pantalla.blit(self.imagenes.tren_afuera, (0, 0))
        elif pantalla_actual == "tren_adentro":
            self.pantalla.blit(self.imagenes.tren_adentro, (0, 0))
        elif pantalla_actual == "maquinista1":
            if self.juego.maquinista3_intro_son_reproduciendo:
                    self.pantalla.blit(self.imagenes.maquinista2_n3, (0, 0))
            else:
                self.pantalla.blit(self.imagenes.maquinista1_n3, (0, 0))

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
        elif pantalla_actual == "camino5":
            self.pantalla.blit(self.imagenes.camino5, (0, 0))
        elif pantalla_actual == "camino6":
            self.pantalla.blit(self.imagenes.camino6, (0, 0))
        elif pantalla_actual == "camino7":
            self.pantalla.blit(self.imagenes.camino7, (0, 0))
        elif pantalla_actual == "camino8":
            self.pantalla.blit(self.imagenes.camino8, (0, 0))
        elif pantalla_actual == "escena_brujula":
            self.pantalla.blit(self.imagenes.camino_brujula, (0, 0))
        elif pantalla_actual == "escena_sin_brujula":
            self.pantalla.blit(self.imagenes.camino_sin_brujula, (0, 0))
