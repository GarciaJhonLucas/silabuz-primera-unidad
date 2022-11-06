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
    
    @classmethod
    def agregar_libro(cls, **datos) -> None:
        #carga un libro en la lista de libros
        libro = Libro(datos["titulo"],datos["genero"],datos["isbn"],datos["editorial"],datos["autores"])
        cls.__libros.append(libro)
    
    @classmethod
    def eliminar_libro(cls,id: int) -> None:
        #elimina un libro, segun su id, de la lista
        for item in cls.__libros:
            if id == item[0]:
                cls.__libros.remove(i)
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_isbn(cls, clave: str) -> List[Libro]:
        for item in cls.__libros:
            if clave == item[3]:
                return item
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_titulo(cls, clave: str) -> List[Libro]:
        for item in cls.__libros:
            if clave == item[0]:
                return item
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_autor(cls, clave: str) -> List[Libro]:
        for item in cls.__libros:
            if clave == item[4]:
                return item
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_editorial(cls, clave: str) -> List[Libro]:
        for item in cls.__libros:
            if clave == item[3]:
                return item
    
    @classmethod
    def buscar_libro_genero(cls, clave: str) -> List[Libro]:
        for item in cls.__libros:
            if clave == item[1]:
                return item
    
    @classmethod
    def ordenar_libros(cls) -> None:
        #Ordena la lista segun sus titulos
        cls.__libros.sort(key=lambda libro: libro.get_titulo(),reverse=True)
    
    @classmethod
    def actualizar_libro(cls) -> None:
        #Actualiza los datos de un libro
        pass
    
    @classmethod
    def grabar_archivo(cls) -> None:
        #Graba la lista de libros en el archivo
        pass