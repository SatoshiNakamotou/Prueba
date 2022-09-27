from ClaseValidacion import *
from ClaseGrafo import *
'''Clase carga de archivo : recibe una validación de archivo y realiza la carga en los grafos'''

class Carga():
    def __init__(self ,archivo,grafo):
        self.archivo = archivo
        self.grafo = grafo
        self.cargarArchivo()
        self.agregarNuevoVertice()
        self.agregarNuevasAristas()

    def cargarArchivo(self):
        self.archivo.eliminarSaltolinea()
        self.archivo.obtenerListadoVertices()
        self.archivo.validarVertices()
        self.archivo.obtenerListadoAristas()
        self.archivo.validarAristas()
        self.archivo.obtenerCaminoBuscado()
        self.archivo.validarCaminoBuscado()
        self.archivo.validacionArchivoCompleto()
        self.archivo.CerrarArchivo()

    def agregarNuevoVertice(self):
        for vertice in self.archivo.get_vertice():
            self.grafo.agregarVertice(vertice[0], vertice[1])

    def agregarNuevasAristas(self):
        for vertice in self.archivo.get_aristas():
            self.grafo.agregarNuevaArista(vertice[0], vertice[1],1)





