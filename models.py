from clases import *

class Ventana:

    def __init__(self):

        self.cuadrado_base = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=50,
            height=60,
            x=100,
            y=100,
            relleno="#BE1FCC"
        )

        self.vidrio1 = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=15,
            height=15,
            x=105,
            y=105,
            relleno="#45E30B"
        )

        self.vidrio2 = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=15,
            height=15,
            x=130,
            y=105,
            relleno="#214F69"
        )

        self.vidrio3 = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=15,
            height=15,
            x=105,
            y=130,
            relleno="#5B5C20"
        )

        self.vidrio4 = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=15,
            height=15,
            x=130,
            y=130,
            relleno="#790C43"
        )

        self.base = Cuadrado(
            borde_color="#000000",
            borde_grosor=2,
            width=50,
            height=10,
            x=100,
            y=160,
            relleno="#786873"
        )

    def dibujar(self):
        self.cuadrado_base.dibujar()
        self.vidrio1.dibujar()
        self.vidrio2.dibujar()
        self.vidrio3.dibujar()
        self.vidrio4.dibujar()
        self.base.dibujar()