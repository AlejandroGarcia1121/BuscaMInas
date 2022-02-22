#IMPORTAMOS LIBRERIAS

import sys, pygame
from pygame.locals import *

#EJECUTAMOS
pygame.init()

#CREAMOS VENTANA
ventana = pygame.display.set_mode((600, 500))
#TITULO VENTANA
pygame.display.set_caption("BUSCAMINAS UDEA")

#DEFINIMOS COLORES QUE SE VAN A USAR
GRIS = (208, 211, 212 )
GRIS_OSCURO = (179, 182, 183)
GRIS_OSCURO_N = (123, 125, 125)

#DEFINIMOS EL FONDO
ventana.fill(GRIS)

#CREAMOS CUADRILATERO EN LA PANTALLA
pygame.draw.rect(ventana, GRIS_OSCURO, (10, 10, 580, 480))
#CIRCULOS ESQUINAS
pygame.draw.circle(ventana, GRIS_OSCURO_N, (10, 10), 20, 0)
pygame.draw.circle(ventana, GRIS_OSCURO_N, (590, 490), 20, 0)
pygame.draw.circle(ventana, GRIS_OSCURO_N, (10, 490), 20, 0)
pygame.draw.circle(ventana, GRIS_OSCURO_N, (590, 10), 20, 0)


#BUCLE PARA QUE LA VENTANA ESTE SIEMPRE ACTIVA Y SE ACTUALICE
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()