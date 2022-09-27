from ClaseVertice import *
class Grafica():
    '''Los vertices se componen de la siguiente estructura :

        self.__vertices = Diccionario que guarda todos los vertices del grafo

        self.vertices_a_eliminar =Aplica cuando se debe ejecutar una ruta de color Rojo o Verde.No aplica para ruta Comun('C')
                                  En esta lista se guardaran los vertices que deben ser eliminados en la adaptacion al grafo

    '''
    def __init__(self):
        self.__vertices = {}
        self.vertices_a_eliminar = []


    '''Metodo get'''

    def ObtenerVertices(self):
        return self.__vertices


    '''Agregar un nuevo vertice al grafo'''
    def agregarVertice(self,id,tipo):
        if id not in self.__vertices:
            self.__vertices[id] = Vertice(id,tipo)



    '''AgregarNuevaArista
        Solo para este caso el peso entre cada arista sera de 1
    '''
    def agregarNuevaArista(self,arista1,Arista2,p):
        if arista1 in self.__vertices and Arista2 in self.__vertices:
            self.__vertices[arista1].agregarVecino(Arista2, p)
            self.__vertices[Arista2].agregarVecino(arista1, p)


    '''Calcular distancia minima'''

    def distanciaMinima(self, lista):
        if len(lista) > 0:
            minimo=self.__vertices[lista[0]].get_distancia()
            vertice=lista[0]
            for v in lista:
                if minimo>self.__vertices[v].get_distancia():
                    minimo=self.__vertices[v].get_distancia()
                    vertice=v
            return vertice

    '''Obtener menor camino'''
    def DeterminarCaminoASeguir(self, b):
        '''Esta funcion se ejecuta despues de Dijkstra'''
        camino=[]
        actual=b
        while actual != None:
            camino.insert(0,actual)
            actual = self.__vertices[actual].get_padre()
        return [camino, self.__vertices[b].get_distancia()]


    '''Obtiene los vertices no visitados para la ejecucion de Dijkstra'''
    def ObtenerNoVisitados(self,vertice):
        self.__vertices[vertice].set_distancia(0)
        noVisitados = []
        for v in self.__vertices:
            if v != vertice:
                self.__vertices[v].set_distancia(float('inf'))
            self.__vertices[v].set_padre(None)
            noVisitados.append(v)
        return noVisitados

    '''Recorre los vecinos del vertice y calcula distancia para cada uno'''

    def recorrerVecinos(self,vertice_actual):

        for vecino in self.__vertices[vertice_actual].get_vecinos():
            if self.__vertices[vecino[0]].get_visitado() == False:
                if self.__vertices[vertice_actual].get_distancia() + vecino[1] < self.__vertices[vecino[0]].get_distancia():
                    self.__vertices[vecino[0]].set_distancia(self.__vertices[vertice_actual].get_distancia() + vecino[1])
                    self.__vertices[vecino[0]].set_padre(vertice_actual)

    '''Ejecuta dijkstra(Se ejecutan funciones ObtenerNoVisitados()-recorrerVecinos())'''

    def Ejecutar_dijkstra(self, Vertice_inicial):
        actual = Vertice_inicial
        noVisitados=[]
        if Vertice_inicial in self.__vertices:
            self.__vertices[Vertice_inicial].set_distancia(0)
            noVisitados = self.ObtenerNoVisitados(actual)

        while len(noVisitados)>0:
            self.recorrerVecinos(actual)
            self.__vertices[actual].set_visitado(True)
            noVisitados.remove(actual)
            actual = self.distanciaMinima(noVisitados)


    def validarSiexisteArista(self,vertice_inicial, vertice_final):
        Existe = False
        for vecinos in self.__vertices[vertice_inicial].get_vecinos():
            if vecinos[0]==vertice_final:

                Existe = True
        for vecinos in self.__vertices[vertice_final].get_vecinos():
            if vecinos[0]==vertice_inicial:
                Existe = True
        return Existe


    '''Imprimir Grafico'''

    def imprimirGrafo(self):
        '''Funcion solo para verificar'''
        for vertice in self.__vertices:
            print('******************************************')
            print('Impriendo Vertice   :'+str(self.__vertices[vertice].get_id()))
            print('*********************')
            print('VECINOS             :'+str(self.__vertices[vertice].get_vecinos()))
            print('ESTADO VISITADO     :'+str(self.__vertices[vertice].get_visitado()))
            print('PADRE               :'+str(self.__vertices[vertice].get_padre()))
            print('DISTANCIA           :'+str(self.__vertices[vertice].get_distancia()))
            print('TIPO TREN           :'+str(self.__vertices[vertice].get_tipo_tren()))

    def ObtenerVecinoVertice(self,vertice):#Recibe el vertice que se debe eleminar
        VecinosVertice = []
        for v in self.__vertices[vertice].get_vecinos():
            VecinosVertice.append(v[0])
        return VecinosVertice

    def DeterminarNuevasAristas(self,conjunto_vertices):
        #El conjunto de vertice debe tener el siguiente formato
        # conjunto_vertices = ['A','B','C']
        NuevasAristas = []
        # Nuevas aristas debe almecenar producto cartesiano del conjunto de vertices ingresadoss
        for i in range(len(conjunto_vertices)):
            for j in range(len(conjunto_vertices)):
                if i!=j:
                    A1 = [] #par ordenado arista
                    A2 = []  #par ordenado arista
                    A1.append(conjunto_vertices[i])
                    A1.append(conjunto_vertices[j])
                    A2.append(conjunto_vertices[j])
                    A2.append(conjunto_vertices[i])
                    if A1 not in NuevasAristas and A2 not in NuevasAristas:
                        NuevasAristas.append(A1)
        return NuevasAristas

    def EliminarVertice(self,vertice):
        self.__vertices.pop(vertice)
        for v in self.__vertices:
            for vecino in self.__vertices[v].get_vecinos():
                if vecino[0]==vertice:
                    self.__vertices[v].EliminarVecino(vecino)
    def obtenerVerticesAEliminar(self,color):
        eliminar_color = 'R'
        if color == 'R':
            eliminar_color = 'V'
        vertices = []
        for v in self.__vertices:
            if self.__vertices[v].get_tipo_tren() == eliminar_color:
                vertices.append(v)
        self.vertices_a_eliminar =vertices
    def ReseteoDatos(self):
        '''funcion solo se utiliza antes de ejecutar Dijkstra'''
        for vertice in self.__vertices:
            self.__vertices[vertice].set_visitado(False)
            self.__vertices[vertice].set_padre(None)
            self.__vertices[vertice].set_distancia(float('inf'))

    def adaptarGrafo(self, tipo_ruta):
        '''Esta funcion modifica las conexiones entre vertices dependiendo del tipo de ruta'''
        '''Por ejemplo: para una ruta Roja, el grafo eliminara los vertices de color verde y posteriormente
                        generara las nuevas conxiones entre los vertices que sean validos para la ruta'''
        self.obtenerVerticesAEliminar(tipo_ruta)
        v=self.vertices_a_eliminar
        for vertice in v:
            vecinos = self.ObtenerVecinoVertice(vertice)
            nuevasAristas=self.DeterminarNuevasAristas(vecinos)
            self.EliminarVertice(vertice)
            for nuevaArista in nuevasAristas:
                if not self.validarSiexisteArista(nuevaArista[0],nuevaArista[1]):
                    self.agregarNuevaArista(nuevaArista[0],nuevaArista[1],1)








