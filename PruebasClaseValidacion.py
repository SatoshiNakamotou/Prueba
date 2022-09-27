import unittest
from ClaseValidacion import *
from VariablesParaPrueba import *
''' Prueba valida que la lectura del archivo, listado de vertice y listado de aristas realizados por la validación
    sean iguales a los que se encuentra en el archivo VariablesParaPrueba.py
'''
class pruebasArchivo(unittest.TestCase):
    def test_eliminarSaltolinea(self):
        self.assertEqual(archivo1.eliminarSaltolinea(),Lectura_vertices_ruta1)
        self.assertEqual(archivo2.eliminarSaltolinea(),Lectura_vertices_ruta2)
        self.assertEqual(archivo3.eliminarSaltolinea(),Lectura_vertices_ruta3)
        self.assertEqual(archivo4.eliminarSaltolinea(),Lectura_vertices_ruta4)

    def test_obtenerListadoVertices(self):
        self.assertEqual(archivo1.obtenerListadoVertices(), vertices_ruta1)
        self.assertEqual(archivo2.obtenerListadoVertices(), vertices_ruta2)
        self.assertEqual(archivo3.obtenerListadoVertices(), vertices_ruta3)
        self.assertEqual(archivo4.obtenerListadoVertices(), vertices_ruta4)

    def test_obtenerListadoAristas(self):

        self.assertEqual(archivo1.obtenerListadoAristas(), aristas_ruta1)
        self.assertEqual(archivo2.obtenerListadoAristas(), aristas_ruta2)
        self.assertEqual(archivo3.obtenerListadoAristas(), aristas_ruta3)
        self.assertEqual(archivo4.obtenerListadoAristas(), aristas_ruta4)



if __name__ == "__main__":
    unittest.main()


