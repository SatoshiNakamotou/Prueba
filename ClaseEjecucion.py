'''La ejecucion del archivo debe recibir una carga'''
from ClaseCarga import *
class EjecucionAlgoritmo():
    def __init__(self,carga):
        '''Recibe una carga de archivo'''
        self.carga = carga
        self.verticeInicial = carga.archivo.get_caminoBuscado()[0]
        self.verticeFinal = carga.archivo.get_caminoBuscado()[1]
        self.colorRuta = carga.archivo.get_caminoBuscado()[2]
        self.ruta = []

    def Ejecutar(self):
        if self.colorRuta == 'C':
            '''Si el color de camino es C , solo se debe ejecutar Dijkstra'''
            self.carga.grafo.Ejecutar_dijkstra(self.verticeInicial)
            self.ruta = self.carga.grafo.DeterminarCaminoASeguir(self.verticeFinal)
        elif self.colorRuta == 'R':
            '''
                Si el color de camino es R , Se debe adaptar grafo a ruta roja y 
                posteriormente se debe ejecutar Dijkstra
                
            '''
            self.carga.grafo.adaptarGrafo('R')
            self.carga.grafo.Ejecutar_dijkstra(self.verticeInicial)
            self.ruta = self.carga.grafo.DeterminarCaminoASeguir(self.verticeFinal)

        elif self.colorRuta == 'V':
            '''
            
                Si el color de camino es V , Se debe adaptar grafo a ruta verde y 
                posteriormente se debe ejecutar Dijkstra
            
            '''
            self.carga.grafo.adaptarGrafo('V')
            self.carga.grafo.Ejecutar_dijkstra(self.verticeInicial)
            self.ruta = self.carga.grafo.DeterminarCaminoASeguir(self.verticeFinal)

        else:
            print("Color de ruta ingresada para busqueda no es valida")

    def MostrarRuta(self):
        color_ruta = ''
        if self.colorRuta == 'V':
            color_ruta = 'Verde'
        if self.colorRuta == 'R':
            color_ruta = 'Roja'
        if self.colorRuta == 'C':
            color_ruta = 'Comun'

        mensaje = 'La ruta que se debe seguir desde '
        mensaje = mensaje +str(self.verticeInicial)
        mensaje = mensaje + ' Hasta el vertice '
        mensaje = mensaje +str(self.verticeFinal) + ' '
        mensaje = mensaje + 'Tomando la ruta de color '
        mensaje = mensaje + color_ruta
        mensaje = mensaje + ' es la siguiente : '
        ruta = ''

        for i in range(len(self.ruta[0])):
            if i < len(self.ruta[0])-1:
                ruta = ruta + str(self.ruta[0][i])
                ruta = ruta + ' --> '
            else:
                ruta = ruta + str(self.ruta[0][i])

        print(mensaje)
        print(ruta)
        print('El numero de estaciones son : ' + str(self.ruta[1])+' Partiendo desde '+str(self.verticeInicial))



