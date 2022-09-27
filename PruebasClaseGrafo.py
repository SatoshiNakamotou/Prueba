import unittest
from ClaseGrafo import *
from VariablesParaPrueba import *


class pruebasArchivo(unittest.TestCase):
    '''Descripcion prueba: Despues se realizar la carga de los grafos, se debe ejecutar el algorimos de dijstra y
        posteriormente determinar el camino mas corto
    '''
    def test_prueba1(self):
        '''Grafo1'''
        TestGrafo1.ReseteoDatos()
        '''Datos deben ser reseteados antes de ejecutar dijkstra, ya que funcion dijkstra ya fue ejecutada
           en el archivo VariablesParaPruebas.py
        '''
        TestGrafo1.Ejecutar_dijkstra('A')
        self.assertEqual(TestGrafo1.DeterminarCaminoASeguir('H'),[['A', 'B', 'C',  'E', 'G', 'H'], 5])

        '''Grafo2'''
        TestGrafo2.ReseteoDatos()
        TestGrafo2.Ejecutar_dijkstra('A')
        self.assertEqual(TestGrafo2.DeterminarCaminoASeguir('I'), [['A', 'D', 'G', 'J', 'I'], 4])

        '''Grafo3'''
        TestGrafo3.ReseteoDatos()
        TestGrafo3.Ejecutar_dijkstra('B')
        self.assertEqual(TestGrafo3.DeterminarCaminoASeguir('L'), [['B', 'A', 'F', 'G', 'L'], 4])

        '''Grafo4'''
        TestGrafo4.ReseteoDatos()
        TestGrafo4.Ejecutar_dijkstra('A')
        self.assertEqual(TestGrafo4.DeterminarCaminoASeguir('L'), [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'], 11])

    def test_pruebaAdaptarGrafoRutaRoja(self):
        '''Para adapar un grafo'''
        '''Observacion : Cuando se adapta un grafo , se eliminan todas los vertices incomptibles al tipo de grafo.
                         Ejemplo : Si se adapta el grafo a un ruta roja, se eliminaran todos los vertices verders
                        y se generaran nuevas aristas entre los vertices adyacentes a los puntos verdes
        '''
        TestGrafo1.adaptarGrafo('R')
        TestGrafo2.adaptarGrafo('R')
        TestGrafo3.adaptarGrafo('R')
        TestGrafo4.adaptarGrafo('R')

        vertices_verdes_grafo1 = 0
        vertices_verdes_grafo2 = 0
        vertices_verdes_grafo3 = 0
        vertices_verdes_grafo4 = 0

        for v in TestGrafo1.ObtenerVertices():
            if  TestGrafo1.ObtenerVertices()[v].get_tipo_tren() == 'V':
                vertices_verdes_grafo1 = vertices_verdes_grafo1+1

        for v in TestGrafo2.ObtenerVertices():
            if  TestGrafo2.ObtenerVertices()[v].get_tipo_tren() == 'V':
                vertices_verdes_grafo2 = vertices_verdes_grafo2+1

        for v in TestGrafo3.ObtenerVertices():
            if  TestGrafo3.ObtenerVertices()[v].get_tipo_tren() == 'V':
                vertices_verdes_grafo3 = vertices_verdes_grafo3+1

        for v in TestGrafo4.ObtenerVertices():
            if  TestGrafo4.ObtenerVertices()[v].get_tipo_tren() == 'V':
                vertices_verdes_grafo4 = vertices_verdes_grafo4+1


        self.assertEqual(vertices_verdes_grafo1, 0)
        self.assertEqual(vertices_verdes_grafo2, 0)
        self.assertEqual(vertices_verdes_grafo3, 0)
        self.assertEqual(vertices_verdes_grafo4, 0)




    def test_pruebaAdaptarGrafoRutaVerde(self):

        TestGrafo1.adaptarGrafo('V')
        TestGrafo2.adaptarGrafo('V')
        TestGrafo3.adaptarGrafo('V')
        TestGrafo4.adaptarGrafo('V')

        vertices_rojos_grafo1 = 0
        vertices_rojos_grafo2 = 0
        vertices_rojos_grafo3 = 0
        vertices_rojos_grafo4 = 0

        for v in TestGrafo1.ObtenerVertices():
            if  TestGrafo1.ObtenerVertices()[v].get_tipo_tren() == 'R':
                vertices_rojos_grafo1 = vertices_rojos_grafo1+1

        for v in TestGrafo2.ObtenerVertices():
            if  TestGrafo2.ObtenerVertices()[v].get_tipo_tren() == 'R':
                vertices_rojos_grafo2 = vertices_rojos_grafo2+1

        for v in TestGrafo3.ObtenerVertices():
            if  TestGrafo3.ObtenerVertices()[v].get_tipo_tren() == 'R':
                vertices_rojos_grafo3 = vertices_rojos_grafo3+1

        for v in TestGrafo4.ObtenerVertices():
            if  TestGrafo4.ObtenerVertices()[v].get_tipo_tren() == 'R':
                vertices_rojos_grafo4 = vertices_rojos_grafo4+1


        self.assertEqual(vertices_rojos_grafo1, 0)
        self.assertEqual(vertices_rojos_grafo2, 0)
        self.assertEqual(vertices_rojos_grafo3, 0)
        self.assertEqual(vertices_rojos_grafo4, 0)



if __name__ == "__main__":
    unittest.main()
