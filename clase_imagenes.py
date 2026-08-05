import pygame

class Imagenes_Juego:
    def __init__(self, ruta, ancho=None, alto=None):
        self.imagen = pygame.image.load(ruta)

        if ancho is not None and alto is not None:
            self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))

    def obtener(self):
        return self.imagen