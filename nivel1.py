class Nivel1:
    def __init__(self, pantalla, imagenes):
        self.pantalla = pantalla
        self.imagenes = imagenes
        self.maquinista_hablando = False

        self.tiempo_maquinista = 0
        self.tiempo_gracias = 0

        self.AAA = True  #Para que la imagen de cofre abierto se mantenga una vez que se abre el cofre
        self.BBB = True  #Para que la imagen de cofre vacio se mantenga una vez que se lleva la semilla
        self.letras = ["A", "A", "A", "A"]
        self.abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.planta_ampliada = None
        self.codigo_correcto = "AMTV"
        self.codigo_ingresado = ""
        self.tiempo_cofre_abierto = 0

    def dibujar (self, pantalla_actual):
        if pantalla_actual == "jardin":
            self.pantalla.blit(self.imagenes.jardin, (0, 0))

        elif pantalla_actual == "afuera":
            self.pantalla.blit(self.imagenes.afuera, (0,0))

        elif pantalla_actual == "interior":
            self.pantalla.blit(self.imagenes.interior, (0,0))

        elif pantalla_actual == "cofre":
            self.pantalla.blit(self.imagenes.cofre, (0,0))
            
        elif pantalla_actual == "cofre_desbloqueando":
            self.pantalla.blit(self.imagenes.cofre_zoom, (0,0))

        elif pantalla_actual == "cofre_abierto":
            self.pantalla.blit(self.imagenes.cofre_abierto, (0,0))

        elif pantalla_actual == "cofre_zoom":
            self.pantalla.blit(self.imagenes.cofre_zoom, (0,0))

        elif pantalla_actual == "semilla":
            self.pantalla.blit(self.imagenes.cofre_semilla, (0,0))

        elif pantalla_actual == "cofre_vacio":
            self.pantalla.blit(self.imagenes.cofre_vacio, (0,0))

        elif pantalla_actual == "invernadero":
            self.pantalla.blit(self.imagenes.invernadero, (0,0))

        elif pantalla_actual == "cabina":
            self.pantalla.blit(self.imagenes.maquinista1, (0,0))
            if self.maquinista_hablando:
                self.pantalla.blit(self.imagenes.maquinista2, (0,0))
            else:
                self.pantalla.blit(self.imagenes.maquinista1, (0,0))

        elif pantalla_actual == "gracias":
            self.pantalla.blit(self.imagenes.gracias1, (0,0))

    def siguiente_letra(self, letra):
        indice = self.abecedario.index(letra)
        return self.abecedario[(indice + 1) % len(self.abecedario)]



            




