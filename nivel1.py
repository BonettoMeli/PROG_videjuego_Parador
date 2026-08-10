class Nivel1:
    def __init__(self, pantalla, imagenes, sonidos):
        self.pantalla = pantalla
        self.imagenes = imagenes
        self.sonidos = sonidos

        self.maquinista_hablando = False
        self.tiempo_maquinista = 0
        self.tiempo_gracias = 0
        self.maquinista_gracias1_son_reproduciendo = False

    def dibujar (self, pantalla_actual):
        if pantalla_actual == "jardin":
            self.pantalla.blit(self.imagenes.jardin, (0,0))

        elif pantalla_actual == "afuera":
            self.pantalla.blit(self.imagenes.afuera, (0,0))

        elif pantalla_actual == "interior":
            self.pantalla.blit(self.imagenes.interior, (0,0))

        elif pantalla_actual == "cofre":
            self.pantalla.blit(self.imagenes.cofre, (0,0))
            
        elif pantalla_actual == "cofre_desbloqueado":
            self.pantalla.blit(self.imagenes.cofre_desbloqueado, (0,0))

        elif pantalla_actual == "cofre_zoom":
            self.pantalla.blit(self.imagenes.cofre_zoom, (0,0))

        elif pantalla_actual == "invernadero":
            self.pantalla.blit(self.imagenes.invernadero, (0,0))

        elif pantalla_actual == "cabina":
            self.pantalla.blit(self.imagenes.cabina, (0,0))
            if self.maquinista_hablando:
                self.pantalla.blit(self.imagenes.maquinista2, (0,0))
            else:
                self.pantalla.blit(self.imagenes.maquinista1, (0,0))

        elif pantalla_actual == "gracias":
            self.pantalla.blit(self.imagenes.gracias, (0,0))