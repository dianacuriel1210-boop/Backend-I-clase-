from p5 import *
from models import *
#Nombre: Valdez Curiel Diana
#Grupo: 06DPRMA
#Materia: Backend I
#Docente: Armando Guetierrez
#Matricula: 2403230163
#Fecha de entrega: 10 de junio 2026


MAX_WIDTH = 800
MAX_HEIGHT = 700

ventana = None


def setup():
    global ventana

    size(MAX_WIDTH, MAX_HEIGHT)

    ventana = Ventana()


def draw():
    background(220)

    ventana.dibujar()


run()