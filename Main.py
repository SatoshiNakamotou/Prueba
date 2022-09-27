from ClaseEjecucion import *
from pathlib import Path

def main(ruta_archivo):
    if Path(ruta_archivo).exists():
        grafo = Grafica()
        carga = Carga(ValidacionAchivo(ruta_archivo), grafo)
        '''Solo se puede ejecutar si y solo si la validacion del archivo completo es True'''
        if carga.archivo.get__validacionArchivoCompleto():
            Ejecucion = EjecucionAlgoritmo(carga)
            Ejecucion.Ejecutar()
            Ejecucion.MostrarRuta()

        else:
            print('Error, Archivo de lectura es invalido, favor corregir')
    else:
        print('Error : ruta de archivo no existe')

ruta='C:\\Users\\super\\Desktop\\Proyectos en Python\\EjemplosParaPrueba\\Prueba1.txt'
main(ruta)



