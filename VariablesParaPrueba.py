'''Las variables declaradas en este archivo son solo para ejecucion de pruebas'''
from ClaseGrafo import *
from ClaseValidacion import *

ruta1 = 'C:\\Users\\super\\Desktop\\Proyectos en Python\\EjemplosParaPrueba\\Prueba1.txt'
ruta2 = 'C:\\Users\\super\\Desktop\\Proyectos en Python\\EjemplosParaPrueba\\Prueba2.txt'
ruta3 = 'C:\\Users\\super\\Desktop\\Proyectos en Python\\EjemplosParaPrueba\\Prueba3.txt'
ruta4 = 'C:\\Users\\super\\Desktop\\Proyectos en Python\\EjemplosParaPrueba\\Prueba4.txt'

archivo1 = ValidacionAchivo(ruta1)
archivo2 = ValidacionAchivo(ruta2)
archivo3 = ValidacionAchivo(ruta3)
archivo4 = ValidacionAchivo(ruta4)

'''Vertices de las rutas'''

vertices_ruta1 = [['A','C'] , ['B','R'] , ['C','C'] , ['D','V'] , ['E','R'] , ['F','V'] , ['G','C'] , ['H','C']]
vertices_ruta2 = [['A','C'],['B','C'], ['C','V'], ['D','C'], ['E','C'] , ['F','C'], ['G','V'] , ['H','C'] , ['I','R'],
                  ['J','R']]
vertices_ruta3 = [['A','C'],['B','C'],['C','C'],['D','V'],['E','R'],['F','R'],['G','V'],['H','V'],['I','C'],['J','C'],['K','C'],['L','C']]
vertices_ruta4 = [['A','C'],['B','R'],['C','R'],['D','V'],['E','R'],['F','C'],['G','R'],['H','C'],['I','V'],['J','V'],
                  ['K','C'],['L','R'],['M','C']]


'''Aristas de las rutas'''

aristas_ruta1 =[['A', 'B'], ['B', 'C'], ['C', 'D'], ['C', 'E'], ['D', 'F'],['E', 'G'], ['F', 'G'], ['G', 'H']]
aristas_ruta2 =[['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['C', 'E'], ['D', 'G'], ['E', 'F'], ['F', 'H'], ['G', 'J'], ['H', 'I'], ['I', 'J']]
aristas_ruta3 =[['A', 'B'], ['A', 'F'], ['B', 'C'], ['C', 'E'], ['C', 'D'], ['D', 'I'], ['E', 'F'], ['F', 'H'], ['F', 'G'], ['G', 'L'], ['H', 'J'], ['H', 'I'], ['I', 'K'], ['J', 'K'], ['K', 'L']]
aristas_ruta4 =[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['F', 'G'], ['G', 'H'], ['H', 'I'], ['I', 'J'], ['J', 'K'], ['K', 'L'], ['L', 'M']]

'''Lectura de los archivos'''

Lectura_vertices_ruta1 =    ['Vertice(A)(C)', 'Vertice(B)(R)','Vertice(C)(C)','Vertice(D)(V)','Vertice(E)(R)',
                            'Vertice(F)(V)','Vertice(G)(C)','Vertice(H)(C)','AgregarCamino(A,B)',
                            'AgregarCamino(B,C)','AgregarCamino(C,D)','AgregarCamino(C,E)','AgregarCamino(D,F)',
                            'AgregarCamino(E,G)','AgregarCamino(F,G)','AgregarCamino(G,H)','CaminoBuscado(A,H,C)']






Lectura_vertices_ruta2 = [  'Vertice(A)(C)', 'Vertice(B)(C)', 'Vertice(C)(V)', 'Vertice(D)(C)', 'Vertice(E)(C)',
                            'Vertice(F)(C)', 'Vertice(G)(V)',  'Vertice(H)(C)', 'Vertice(I)(R)', 'Vertice(J)(R)',
                            'AgregarCamino(A,B)', 'AgregarCamino(A,C)', 'AgregarCamino(A,D)', 'AgregarCamino(B,C)',
                            'AgregarCamino(C,E)', 'AgregarCamino(D,G)', 'AgregarCamino(E,F)', 'AgregarCamino(F,H)',
                            'AgregarCamino(G,J)', 'AgregarCamino(H,I)', 'AgregarCamino(I,J)', 'CaminoBuscado(A,I,R)']



Lectura_vertices_ruta3 =    ['Vertice(A)(C)', 'Vertice(B)(C)', 'Vertice(C)(C)', 'Vertice(D)(V)', 'Vertice(E)(R)',
                            'Vertice(F)(R)', 'Vertice(G)(V)', 'Vertice(H)(V)', 'Vertice(I)(C)', 'Vertice(J)(C)',
                            'Vertice(K)(C)', 'Vertice(L)(C)', 'AgregarCamino(A,B)', 'AgregarCamino(A,F)',
                            'AgregarCamino(B,C)', 'AgregarCamino(C,E)', 'AgregarCamino(C,D)', 'AgregarCamino(D,I)',
                            'AgregarCamino(E,F)', 'AgregarCamino(F,H)', 'AgregarCamino(F,G)', 'AgregarCamino(G,L)',
                            'AgregarCamino(H,J)', 'AgregarCamino(H,I)', 'AgregarCamino(I,K)', 'AgregarCamino(J,K)',
                            'AgregarCamino(K,L)', 'CaminoBuscado(B,L,V)']

Lectura_vertices_ruta4 =[   'Vertice(A)(C)', 'Vertice(B)(R)', 'Vertice(C)(R)', 'Vertice(D)(V)', 'Vertice(E)(R)',
                            'Vertice(F)(C)', 'Vertice(G)(R)', 'Vertice(H)(C)', 'Vertice(I)(V)', 'Vertice(J)(V)',
                            'Vertice(K)(C)', 'Vertice(L)(R)', 'Vertice(M)(C)', 'AgregarCamino(A,B)', 'AgregarCamino(B,C)',
                            'AgregarCamino(C,D)', 'AgregarCamino(D,E)', 'AgregarCamino(E,F)', 'AgregarCamino(F,G)',
                            'AgregarCamino(G,H)', 'AgregarCamino(H,I)', 'AgregarCamino(I,J)', 'AgregarCamino(J,K)',
                            'AgregarCamino(K,L)', 'AgregarCamino(L,M)', 'CaminoBuscado(A,L,R)']



'''Instancia grafos para prueba'''
TestGrafo1 = Grafica()
TestGrafo2 = Grafica()
TestGrafo3 = Grafica()
TestGrafo4 = Grafica()


'''Carga TestGrafo1'''
for vertice in vertices_ruta1:
    TestGrafo1.agregarVertice(vertice[0],vertice[1])
for arista in aristas_ruta1:
    TestGrafo1.agregarNuevaArista(arista[0],arista[1],1)


'''Carga TestGrafo2'''
for vertice in vertices_ruta2:
    TestGrafo2.agregarVertice(vertice[0],vertice[1])
for arista in aristas_ruta2:
    TestGrafo2.agregarNuevaArista(arista[0],arista[1],1)

'''Carga TestGrafo3'''
for vertice in vertices_ruta3:
    TestGrafo3.agregarVertice(vertice[0],vertice[1])
for arista in aristas_ruta3:
    TestGrafo3.agregarNuevaArista(arista[0],arista[1],1)

'''Carga TestGrafo4'''
for vertice in vertices_ruta4:
    TestGrafo4.agregarVertice(vertice[0],vertice[1])
for arista in aristas_ruta4:
    TestGrafo4.agregarNuevaArista(arista[0],arista[1],1)





