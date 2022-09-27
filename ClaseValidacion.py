class ValidacionAchivo():
    def __init__(self,rutaArchivo):
        self.__archivo = open(rutaArchivo, 'r', encoding="utf-8")
        self.__lecturaArchivo = self.__archivo.readlines()
        self.__validacionArchivoCompleto = False
        self.__lecturaVertices = []
        self.__vertice = [] # Contiene par ordenado del vertice , por ejemplo [[ 'A' , 'R'] ,[ 'B' , 'V']] : Vertice A es Rojo y Vertice B es Verde
        self.__validacionVertices = False
        self.__lecturaAristas = []
        self.__aristas = []
        self.__validacionArista = False
        self.__lecturaCaminoBuscado = []
        self.__caminoBuscado =[]
        self.__validacionCamino =False

    '''Metodos Get'''
    def get_Archivo(self):
        return self.__archivo
    def get_lecturaArchivo(self):
        return self.__lecturaArchivo
    def get__validacionArchivoCompleto(self):
        return self.__validacionArchivoCompleto
    def get_lecturaVertices(self):
        return self.__lecturaVertices
    def get_vertice(self):
        return self.__vertice
    def get_validacionVertices(self):
        return self.__validacionVertices
    def get_lecturaAristas(self):
        return self.__lecturaAristas
    def get_aristas(self):
        return self.__aristas
    def get_validacionArista(self):
        return self.__validacionArista
    def get_lecturaCaminoBuscado(self):
        return self.__lecturaCaminoBuscado
    def get_caminoBuscado(self):
        return self.__caminoBuscado
    def get_validacionCamino(self):
        return self.__validacionCamino

    '''Metodos Set'''

    def set_Archivo(self,archivo):
        self.__archivo=archivo
    def set_lecturaArchivo(self,lecturaArchivo):
        self.__lecturaArchivo=lecturaArchivo
    def set_validacionEstructura(self,validacionEstructura):
        self.__validacionEstructura=validacionEstructura
    def set_lecturaVertices(self,lecturaVertices):
        self.__lecturaVertices=lecturaVertices
    def set_vertice(self,vertice):
        self.__vertice=vertice
    def set_validacionVertices(self,validacionVertices):
        self.__validacionVertices=validacionVertices
    def set_lecturaAristas(self,lecturaAristas):
        self.__lecturaAristas
    def set_aristas(self,aristas):
        self.__aristas=aristas
    def set_validacionArista(self,validacionAristavo):
        self.__validacionAristavo=validacionAristavo
    def set_lecturaCaminoBuscado(self,lecturaCaminoBuscado):
        self.__lecturaCaminoBuscado = lecturaCaminoBuscado
    def set_caminoBuscado(self,caminoBuscado):
        self.__caminoBuscado=caminoBuscado
    def set_validacionCamino(self,validacionCamino):
        self.__validacionCamino=validacionCamino

    def CerrarArchivo(self):
        self.__archivo.close()

    '''Eliminar el salto de linea del archivo'''

    def eliminarSaltolinea(self):
        lectura_sin_salto_linea = []
        for linea in self.__lecturaArchivo:
            if linea[len(linea)-1:len(linea)] == '\n':
                lectura_sin_salto_linea.append(linea[0:len(linea)-1])
            else:
                lectura_sin_salto_linea.append(linea)
        self.__lecturaArchivo =lectura_sin_salto_linea
        return self.get_lecturaArchivo()

    '''Obtener listado de aristas'''

    def obtenerListadoVertices(self):
        #valida y obtiene los vertices que deben ser creado
        listado_vertices = []
        for linea in self.__lecturaArchivo:
            if linea[0:8]=='Vertice(' and linea[9:11] == ')(' and linea[len(linea)-1] == ')' and len(linea)==13:
                listado_vertices.append(linea)
                v=[]
                v.append(linea[8])
                v.append(linea[11])
                self.__vertice.append(v)
        self.__lecturaVertices = listado_vertices
        return self.get_vertice()

    '''  Validacion de Vertices'''

    def validarVertices(self):
        self.__validacionVertices = False
        erroresLargoCadena = 0
        numero_repetido = 0
        color_ruta_invalido = 0
        for i in range (len(self.__lecturaVertices)):
            if len(self.__lecturaVertices[i]) !=13:
                erroresLargoCadena = erroresLargoCadena+1
            if self.__lecturaVertices[i][11] not in ('C','R','V'):
                color_ruta_invalido=color_ruta_invalido+1
            for j in range(len(self.__lecturaVertices)):
                if i!=j:
                    if self.__lecturaVertices[i]==self.__lecturaVertices[j]:
                        numero_repetido=numero_repetido+1
        if numero_repetido==0 and color_ruta_invalido==0 and erroresLargoCadena==0:
            self.__validacionVertices = True

        '''Validacion de vertice que vertices ingresados tengan una ruta Comun , Roja ,Verde '''
        for v in self.__vertice:
            if v[1] not in ('C','R','V'):
                self.__validacionVertices = False
        return self.get_validacionVertices()

    '''Obtener listado de aristas'''

    def obtenerListadoAristas(self):
        listado_aristas = []
        for linea in self.__lecturaArchivo:
            if linea[0:14]=='AgregarCamino(' and linea[15:16] == ',' and linea[len(linea)-1] == ')' and len(linea)==18:
                v=[]
                v.append(linea[14])
                v.append(linea[16])
                self.__aristas.append(v)
                listado_aristas.append(linea)
        self.__lecturaAristas =listado_aristas
        return self.get_aristas()


    '''validacion de aristas'''

    def validarAristas(self):
        #obtener listado de vertices
        erroresLargoCadena = 0
        listado_vertices = []
        acum = 0
        '''Valida que el largo de la cadena sea 18 len('AgregarCamino(X,Y)') '''
        for linea in self.__lecturaAristas:
            if len(linea) != 18:
                erroresLargoCadena = erroresLargoCadena +1

        '''Almacenamos los vertices del grafo en un listado_vertices'''
        for vertice in self.__vertice:
            listado_vertices.append(vertice[0])


        '''Validamos que las Aristas ingresadas tengan un vertice valido '''

        for conjunto_aristas in self.__aristas:
            for aristas in conjunto_aristas:
                if aristas not in listado_vertices:
                    acum = acum +1
        if acum > 0:
            self.__validacionArista = False
            print("Vertice ingresado en arista es invalido")
        if erroresLargoCadena > 0:
            self.__validacionArista = False
            print("Error, largo de texto invalido")

        if acum == 0 and erroresLargoCadena==0:
            self.__validacionArista = True

        '''Las aristas que componen un vertice deben existir en el listado de vertices y ademas no pueden contectar
           consigo mismas'''

        for a in self.__aristas:
            if a[0] not in listado_vertices and a[1] not in listado_vertices:
                self.__validacionArista = False
            if a[0] == a[1]:
                self.__validacionArista = False
        return self.get_validacionArista()

        '''Obtener camino buscado'''

    def obtenerCaminoBuscado(self):
        '''Ejemplo: para 'CaminoBuscado(A,D,R)' , retornara la siguiente lista ['A','D','R']'''
        for linea in self.__lecturaArchivo:
            if linea[0:14] == 'CaminoBuscado(' and linea[15]==',' and linea[17]==',' and linea[len(linea)-1]==')':
                vertice_inicial = linea[14]
                vertice_final = linea[16]
                color_ruta = linea[18]
                lectura = linea
                self.__lecturaCaminoBuscado.append(linea)
                self.__caminoBuscado.append(vertice_inicial)
                self.__caminoBuscado.append(vertice_final)
                self.__caminoBuscado.append(color_ruta)
        return self.__caminoBuscado

    '''Validación del camino buscado'''


    def ObtenerColorVertice( self, vertice , listado_vertices):
        '''El listado de vertices ingresados corresponde a un lista que contiene el par  [Vertice,Color_vertice]'''
        '''Por ejemplo : [['A','R'],['B','R'],['C','C'],['D','V'],['E','C']].    
        '''
        color_ingresado = ''
        for v in listado_vertices:
            if v[0] == vertice:
                color_ingresado = v[1]
        return color_ingresado

    '''Archivo'''

    def validarCaminoBuscado(self):

        erroresEncontrados = 0
        listado_vertices = []
        color_vertice_inicial = 1
        color_vertice_final = 1

        '''Obtiene los vertices del grafo'''
        for vertice in self.__vertice:
            listado_vertices.append(vertice[0])

        vertice_inicial=self.__caminoBuscado[0]
        vertice_final = self.__caminoBuscado[1]
        color_ruta = self.__caminoBuscado[2]

        if vertice_inicial not in listado_vertices:
            erroresEncontrados = erroresEncontrados +1

        if vertice_final not in listado_vertices:
            erroresEncontrados = erroresEncontrados + 1

        if color_ruta not in ('C','R','V'):
            erroresEncontrados = erroresEncontrados + 1
            self.__validacionCamino = False
        if len(self.__caminoBuscado) ==0:
            erroresEncontrados = erroresEncontrados + 1

        '''Solo puede existir un camino buscado por archivo'''
        if len(self.__lecturaCaminoBuscado)>1:
            erroresEncontrados = erroresEncontrados + 1
            '''Hay mas de un camino buscado'''
        if len(self.__lecturaCaminoBuscado)==0:
            erroresEncontrados = erroresEncontrados + 1
            '''No hay camino buscado'''

        '''Algoritmo solo se puede ejecutar si:
                    ColorVerticeInicial == 'R' and ColorVerticeFinal == 'R' or
                    ColorVerticeInicial == 'V' and ColorVerticeFinal == 'V' or
                    (ColorVerticeInicial == 'C' or ColorVerticeFinal == 'C' )
        '''

        ColorVerticeInicial = self.ObtenerColorVertice(self.__caminoBuscado[0], self.__vertice)
        ColorVerticeFinal = self.ObtenerColorVertice(self.__caminoBuscado[1], self.__vertice)
        ColorRuta = self.__caminoBuscado[2]

        if not ((ColorVerticeInicial == ColorVerticeFinal) or (ColorVerticeInicial == 'C' or ColorVerticeFinal == 'C')):
            erroresEncontrados = erroresEncontrados +1

        if erroresEncontrados == 0:
            self.__validacionCamino = True
        else:
            self.__validacionCamino = False

        return self.__validacionCamino


    def validacionArchivoCompleto(self):
        if not self.__validacionVertices:
            print('Error: Vertices ingresados en archivo son invalidos')
        if not self.__validacionArista:
            print('Error: Aristas ingresadas en archivo son invalidos')
        if not self.__validacionCamino:
            print('Error: Camino buscado en archivo son invalidos')
        if self.__validacionVertices and self.__validacionArista and self.__validacionCamino:
            self.__validacionArchivoCompleto = True
        return self.get__validacionArchivoCompleto()

