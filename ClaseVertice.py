class Vertice():
    '''Los vertices se componen de la siguiente estructura :

        self.__id = Corresponde al identificador del vertice , Ejemplo 'A' ,'B' ,'C' , etc...

        self.__vecinos = Corresponde a los vecinos delñ vertice, es una lista que contiene un par
                        [id_vertice,Ditancia al vertice]. Para este problema la distancia siempre sera 1

        self.__visitado = Boleano que indica si vertice fue visitado por el algoritmo de Dijkstra

        self.__padre =  Padre del vertice, este valor es seteado por Dijkstra

        self.__distancia =  distancia hacia el vertice inicial que ejecuta Dijkstra,

        self.__tipo_tren =  Corresponde al color del vertice ( Solo pueden ser 'C'(estacion común) , 'R'(estacion roja) o
                            'V'(estacion verde)
    '''
    def __init__(self , i ,tipo_tren):
        self.__id = i
        self.__vecinos = []
        self.__visitado = False
        self.__padre = None
        self.__distancia = float('inf')
        self.__tipo_tren=tipo_tren

    '''Metodos Get'''
    def get_id(self):
        return self.__id

    def get_vecinos(self):
        return self.__vecinos

    def get_visitado(self):
        return self.__visitado

    def get_padre(self):
        return self.__padre

    def get_distancia(self):
        return self.__distancia

    def get_tipo_tren(self):
        return self.__tipo_tren

    '''Metodos set'''

    def set_id(self,id):
        self.__id=id

    def set_vecinos(self,vecinos):
        self.__vecinos=vecinos

    def set_visitado(self,visitado):
        self.__visitado=visitado

    def set_padre(self,padre):
        self.__padre=padre

    def set_distancia(self,distancia):
        self.__distancia=distancia

    def set_tipo_tren(self,tipo_tren):
        self.__tipo_tren=tipo_tren

    def EliminarVecino(self,vecino):
        self.__vecinos.remove(vecino)

    def __eq__(self, vertice):
        if type(self) != type(vertice):
            return False
        else:
            '''Si son de la misma instancia , se debe validar que tengan la misma data'''
            v1 =(self.get_id() == vertice.get_id())
            v2 =(self.get_padre() == vertice.get_padre())
            v3 =(self.get_vecinos() == vertice.get_vecinos())
            v4 =(self.get_distancia() == vertice.get_distancia())
            v5 =(self.get_tipo_tren() == vertice.get_tipo_tren())

            if v1 and v2 and v3 and v4 and v5:
                return True
            else:
                return False

    def agregarVecino(self,v,p):
        if v not in self.get_vecinos():
            self.__vecinos.append([v,p])

