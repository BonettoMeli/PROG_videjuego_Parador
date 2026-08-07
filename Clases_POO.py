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

class Imagenes():
    def cargar(self, ruta, ancho, alto):
        imagen = pygame.image.load(ruta)
        return pygame.transform.scale(imagen, (ancho, alto))

    def __init__(self):

        #------- INVENTARIO ------------------------------------------------------
        self.bolso = self.cargar("visual/bolso.png",150,130)
        self.inventario = self.cargar("visual/inventario.png",500,400)

        #-------- CARGA DE NIVELES -----------------------------------------------
        self.nivel1 = self.cargar("visual/Nivel1.jpeg",1400,800)
        self.nivel2 = self.cargar("visual/Nivel2.jpeg",1400,800)
        self.nivel3 = self.cargar("visual/Nivel3.jpeg",1400,800)
        self.nivel4 = self.cargar("visual/Nivel4.jpeg",1400,800)

        #---------- IMAGENES DE CARGA GENERAL ------------------------------------
        self.inicio = self.cargar('visual/Inicio.png',1400,800)
        self.carga = self.cargar('visual/explorando_dimen.png',1400,800)
        self.intro = self.cargar('visual/instrucciones.png',1400,800)
        self.carga2 = self.cargar('visual/carga2.png',1400,800)

        #---------- HISTORIA -----------------------------------------------------
        self.n1 = self.cargar('visual/desde.png',1400,800)
        self.n2 = self.cargar('visual/unico.png',1400,800)
        self.n3 = self.cargar('visual/ruido.png',1400,800)
        self.n4 = self.cargar('visual/persiguen.png',1400,800)
        self.n5 = self.cargar('visual/importancia.jpeg',1400,800)
        self.n6 = self.cargar('visual/noche1.png',1400,800)
        self.n7 = self.cargar('visual/algopaso.png',1400,800)

        self.auto1 = self.cargar('visual/auto_parte11.jpg',490,800)
        self.auto2 = self.cargar('visual/auto_parte22.jpg',490,800)
        self.auto3 = self.cargar('visual/auto_parte3.png',480,800) 

        self.parte2 = self.cargar('visual/paro.png',490,800)
        self.parte3 = self.cargar('visual/paro2.png',925,800)

        self.llegada1 = self.cargar('visual/llegada1.jpg',490,800)
        self.llegada2 = self.cargar('visual/llegada2.jpg',470,800)
        self.llegada3 = self.cargar('visual/llegada3.jpg',490,800)

        self.tren1 = self.cargar("visual/tren1.jpg",490,800)
        self.tren2 = self.cargar("visual/tren2.jpg",490,800)
        self.tren3 = self.cargar("visual/tren3.jpg",490,800)

        self.man = self.cargar("visual/tipo_sentado.jpeg",1400,800)
        self.charla1 = self.cargar("visual/charla1.jpg",1400,800)
        self.charla2 = self.cargar("visual/charla2.jpg",1400,800)
        self.charla3 = self.cargar("visual/charla3.jpg",1400,800)
        self.charla4 = self.cargar("visual/charla4.jpg",1400,800)
        self.charla5 = self.cargar("visual/charla5.jpg",1400,800)
        self.charla6 = self.cargar("visual/charla6.jpeg",1400,800)
        self.charla7 = self.cargar("visual/charla7.PNG",1400,800)
        self.charla8 = self.cargar("visual/charla8.jpeg",1400,800)
        self.charla9 = self.cargar("visual/charla9.png",1400,800)
        self.charla10 = self.cargar("visual/charla10.jpeg",1400,800)
        self.charla11 = self.cargar("visual/charla11.jpeg",1400,800)
        self.maquinista1 = self.cargar("visual/maquinista1.jpg",1400,800)
        self.maquinista2 = self.cargar("visual/maquinista2.jpeg",1400,800)

        #-------------- OBJETOS QUE CONSIGUE EL USUARIO ------------------------------
        self.semilla_transp = self.cargar("visual/semilla_trasparente.png",100,90)
        self.fusible_transp = self.cargar("visual/fusible_transparente.png",100,90)
        self.llave_transp = self.cargar("visual/llave_transparente.png",100,9)

        #---------------- NIVEL UNO --------------------------------------------------------------------------
        self.interior = self.cargar("visual/vagon_vacio.jpeg",1400,800)

        self.jardin = self.cargar("visual/lenguas_muertas2.jpg",1400,800)
        self.invernadero = self.cargar("visual/invernadero_adentro.jpg"),1400,800
        self.cofre = self.cargar("visual/cofre_lengua1.jpeg",1400,800)
        self.cofre_abierto = self.cargar("visual/cofre_lengua2.jpeg",1400,800)
        self.cofre_zoom = self.cargar("visual/cofre_zoom2.jpeg",1400,800)
        self.afuera = self.cargar("visual/tren_lengua_abierto.png",1400,800)
        self.cofre_semilla = self.cargar("visual/cofre_semilla.jpeg",1400,800)
        self.cofre_vacio = self.cargar("visual/cofre_vacio.jpeg",1400,800)
        self.gracias1 = self.cargar("visual/gracias1.jpeg",1400,800)

        #HOJAS DEL INVERNADERO
        self.hoja_A = self.cargar("visual/hoja_A.jpg",600,400)
        self.hoja_M = self.cargar("visual/hoja_M.jpg",600,400)
        self.hoja_T = self.cargar("visual/hoja_T.jpg",600,400)
        self.hoja_V = self.cargar("visual/hoja_V.jpg",600,400)

        #---------------- NIVEL DOS -------------------------------------------------------------------------

        self.camino = self.cargar("visual/tres_caminos.jpeg",1400,800)

        #LIBRO
        self.libro = self.cargar("visual/libro_archivo.jpeg",1400,800)
        self.libro1 = self.cargar("visual/libro1.png",900,500)
        self.libro2 = self.cargar("visual/libro2.png",900,500)
        self.libro3 = self.cargar("visual/libro3.jpeg",900,500)
        self.libro4 = self.cargar("visual/libro4.png",900,500)
        self.libro5 = self.cargar("visual/libro5.png",900,500)

        #TREN
        self.intro_archivo = self.cargar("visual/intro_archivo.jpeg",1400,800)
        self.afuera2 = self.cargar("visual/tren_archivo_afuera.jpg",1400,800)
        self.cabina2 = self.cargar("visual/cabina2.jpeg",1400,800)
        self.cabina2_hablando = self.cargar("visual/cabina2_hablando.jpeg",1400,800)
        self.vagon_archivo = self.cargar("visual/vagon_interior.jpeg",1400,800)
        self.gracias2 = self.cargar("visual/gracias2.jpeg",1400,800)
        self.maquinista_fusible = self.cargar("visual/cabina2_hablando.jpeg",1400,800)
        self.archivo2_viejo = self.cargar("visual/archivo2_viejo.jpeg",1400,800)

        #BIBLIOTECA
        self.puerta = self.cargar("visual/biblioteca_sumergido.jpeg",1400,800)
        self.puerta_zoom = self.cargar("visual/puerta_zoom.jpeg",1400,800)
        self.puerta_abierta1 = self.cargar("visual/puerta_abierta.png",1400,800)
        self.cofre_abierto2 = self.cargar("visual/cofre_abierto2.jpeg",1400,800)
        self.cofre_vacio2 = self.cargar("visual/cofre_vacio2.jpeg",1400,800)
        self.inte_biblio = self.cargar("visual/interior_biblioteca.png",1400,800)
        self.mapa = self.cargar("visual/sala_mapa.jpeg",1400,800)
        self.cofre_archi = self.cargar("visual/cofre_archivo_cerrado.png",1400,800)

        #CASA LLAVE
        self.casa_afuera = self.cargar("visual/casa_afuera.jpeg",1400,800)
        self.casa_adentro = self.cargar("visual/casa_adentro.jpeg",1400,800)
        self.panel = self.cargar("visual/mueble_palancas.jpeg",1400,800)
        self.palanca_arriba = self.cargar("visual/P_arriba.png",270,350)
        self.palanca_abajo = self.cargar("visual/P_abajo.png",250,350)
        self.llave1 = self.cargar("visual/llave_abajo.jpeg",1400,800)
        self.llave2 = self.cargar("visual/sin_llave.jpeg",1400,800)

       
        
        
