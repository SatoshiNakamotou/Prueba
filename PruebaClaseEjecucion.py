import unittest
from VariablesParaPrueba import *
from ClaseCarga import *
from ClaseEjecucion import *
grafo1 = Grafica()
grafo2 = Grafica()
grafo3 = Grafica()
grafo4 = Grafica()

'''La clase carga debe recibir un Grafo vacio'''

carga1 = Carga(archivo1,grafo1)
carga2 = Carga(archivo2,grafo2)
carga3 = Carga(archivo3,grafo3)
carga4 = Carga(archivo4,grafo4)


Ejecucion1 = EjecucionAlgoritmo(carga1)
Ejecucion2 = EjecucionAlgoritmo(carga2)
Ejecucion3 = EjecucionAlgoritmo(carga3)
Ejecucion4 = EjecucionAlgoritmo(carga4)



class pruebasArchivo(unittest.TestCase):


    def test_Ejecucion_Dijkstra(self):
        '''Despues de ejecutar Dijkstra, se debe verificar la ruta mas corta'''

        Ejecucion1.Ejecutar()
        Ejecucion2.Ejecutar()
        Ejecucion3.Ejecutar()
        Ejecucion4.Ejecutar()

        '''Rutas mas cortas( Se puede validar mirando grafo)'''

        r1 = [['A', 'B', 'C',  'E', 'G', 'H'], 5]
        r2 = [['A', 'D', 'J', 'I'], 3]
        r3 = [['B', 'A', 'G', 'L'], 3]
        r4 = [['A', 'B', 'C', 'E', 'F', 'G', 'H', 'K', 'L'], 8]

        self.assertEqual(Ejecucion1.ruta,r1)
        self.assertEqual(Ejecucion2.ruta,r2)
        self.assertEqual(Ejecucion3.ruta,r3)
        self.assertEqual(Ejecucion4.ruta,r4)

if __name__ == "__main__":
    unittest.main()






