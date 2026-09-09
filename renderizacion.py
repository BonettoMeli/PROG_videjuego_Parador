import pygame


class PantallaEscalable:

  def __call__(self, *args, **kwds):
    return self.ventana_real

  def __init__(self, ancho_base, alto_base, dimensiones_reales):
    # Dimensiones lógicas (en las que diseñas el juego, ej: 800x600)
    self.ancho_base = ancho_base
    self.alto_base = alto_base

    # Crear la ventana real del sistema
    self.ventana_real = pygame.display.set_mode(dimensiones_reales)

    # Calcular los factores de escala
    self.actualizar_escala(dimensiones_reales)

  def actualizar_escala(self, nuevas_dimensiones):
    """Recalcula los factores de escala si la pantalla cambia de tamaño."""
    self.ancho_real, self.alto_real = nuevas_dimensiones
    self.escala_x = self.ancho_real / self.ancho_base
    self.escala_y = self.alto_real / self.alto_base

  def blit(self, superficie, posicion):
    """Versión modificada de blit que escala la imagen y su posición automáticamente."""
    x, y = posicion

    # 1. Escalar la posición
    pos_escalada = (int(x * self.escala_x), int(y * self.escala_y))

    # 2. Escalar la imagen/objeto al tamaño correspondiente
    ancho_nuevo = int(superficie.get_width() * self.escala_x)
    alto_nuevo = int(superficie.get_height() * self.escala_y)
    superficie_escalada = pygame.transform.scale(
        superficie, (ancho_nuevo, alto_nuevo)
    )

    # 3. Dibujar en la pantalla real
    self.ventana_real.blit(superficie_escalada, pos_escalada)

  def fill(self, color):
    """Redirige el llenado de color a la ventana real."""
    self.ventana_real.fill(color)

  # Puedes agregar aquí otros métodos de Pygame que uses, como get_size o blits
  def get_size(self):
    return (self.ancho_base, self.alto_base)