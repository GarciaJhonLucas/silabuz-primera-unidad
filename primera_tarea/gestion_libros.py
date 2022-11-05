import csv
from typing import List
from libros import Libro

class Gestor_libros:
    __ruta_archivo = "libros.csv"
    __libros= []
    
    @classmethod
    def cargar_archivo(cls) -> None:
        #abre el archivo y guarda los libros en memoria
        with open(cls.__ruta_archivo) as f:
            lista_libros = csv.DictReader(f)
            for lib in lista_libros:
                libro = Libro(
                    lib["Titulo"],
                    lib["Genero"],
                    lib["ISBN"],
                    lib["Editorial"],
                    lib["Autores"]
                )
                cls.__libros.append(libro)
    
    @classmethod
    def listar_libros(cls) -> None:
        #Imprime los libros en la lista
        for lib in cls.__libros:
            lib.listar()
            print("---------")