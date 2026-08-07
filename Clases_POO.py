import pygame
import sys

class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.pantalla = pygame.display.set_mode((1400,800))
        pygame.display.set_caption("Videojuego: ¨EL PARADOR¨")
        self.pantalla_actual = "inicio"

    def obtener_pantalla(self):
        return self.pantalla

    def ejecutar(self):
        print("el juego comenzo")

class Inventario():
    def __init__(self):
        self.abierto = False
        self.objetos = []
        self.objeto_seleccionado = None

class Boton():
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)

    def collidepoint(self,pos):
        return self.rect.collidepoint(pos)

    def dibujar(self, pantalla, color=(255,0,0), grosor=2): #boton_jugar.dibujar(pantalla)
        pygame.draw.rect(pantalla, color, self.rect, grosor)