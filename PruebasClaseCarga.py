import unittest
from ClaseCarga import *
from ClaseGrafo import *
from VariablesParaPrueba import *
'''La data necesaria para ejecutar esta prueba se encuentra en el archivo VariablesParaPrueba.py'''

grafo1 = Grafica()
grafo2 = Grafica()
grafo3 = Grafica()
grafo4 = Grafica()

carga1 = Carga(archivo1, grafo1)
carga2 = Carga(archivo2, grafo2)
carga3 = Carga(archivo3, grafo3)
carga4 = Carga(archivo4, grafo4)

class pruebasArchivo(unittest.TestCase):


    def test_ValidarVertices(self):
        '''Observacion1 : En esta prueba se validará que los vertices de los grafos de prueba
                         sean iguales a los vertices que hay en los grafos de carga

           Observacion2 : para este caso no es necesario realizar un prueba unitaria para
                          Validar aristas, ya que estas se encuentran en una lista en los vertices
                          y esta prueba valida que ambos grafos tengan las mismas arista y vertices
        '''


        for v in carga1.grafo.ObtenerVertices():
            self.assertEqual(carga1.grafo.ObtenerVertices()[v].__eq__(TestGrafo1.ObtenerVertices()[v]),True)
        for v in carga2.grafo.ObtenerVertices():
            self.assertEqual(carga2.grafo.ObtenerVertices()[v].__eq__(TestGrafo2.ObtenerVertices()[v]),True)
        for v in carga3.grafo.ObtenerVertices():
            self.assertEqual(carga3.grafo.ObtenerVertices()[v].__eq__(TestGrafo3.ObtenerVertices()[v]),True)
        for v in carga4.grafo.ObtenerVertices():
            self.assertEqual(carga4.grafo.ObtenerVertices()[v].__eq__(TestGrafo4.ObtenerVertices()[v]),True)


if __name__ == "__main__":
    unittest.main()




