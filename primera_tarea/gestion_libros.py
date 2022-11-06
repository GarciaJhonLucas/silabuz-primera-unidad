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
        for lib in cls.__libros:
            if id == lib[0]:
                cls.__libros.remove(i)
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_isbn(cls, clave: str) -> List[Libro]:
        for lib in cls.__libros:
            if clave == lib[3]:
                return lib
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_titulo(cls, clave: str) -> List[Libro]:
        for lib in cls.__libros:
            if clave == lib[0]:
                return lib
    
    #Filtra los libros segun el criterio elegido:
    def convert_author_list(author: str) -> List:
        autor = ""
        lista_autores = []
        for i in author:
            if i == ',':
                lista_autores.append(autor)
                autor = ""
                continue
            autor += i
        lista_autores.append(autor)
        return lista_autores
    
    @classmethod
    def buscar_libro_autor(cls, clave: str) -> List[Libro]:
        num_authors = 0
        for i in cls.__libros:
            lista_autores = convert_author_to_list(cls.__libros[i][4])
            if len(lista_autores) == num_authors:
                objeto_libros.append(i)
            elif  num_authors < len(lista_autores) or  num_authors > len(lista_autores):
                pass
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_editorial(cls, clave: str) -> List[Libro]:
        for lib in cls.__libros:
            if clave == lib[3]:
                return lib
    
    @classmethod
    def buscar_libro_genero(cls, clave: str) -> List[Libro]:
        for lib in cls.__libros:
            if clave == lib[1]:
                return lib
    
    @classmethod
    def ordenar_libros(cls) -> None:
        #Ordena la lista segun sus titulos
        cls.__libros.sort(key=lambda libro: libro.get_titulo(),reverse=True)
    
    @classmethod
    def actualizar_libro(cls,**datos) -> None:
        cls.__libros[0] = datos["titulo"]
        cls.__libros[1] = datos["genero"]
        cls.__libros[2] = datos["isbn"]
        cls.__libros[3] = datos["editorial"] 
        cls.__libros[4] = datos["autores"]
    
    @classmethod
    def grabar_archivo(cls) -> None:
        with open(cls.__ruta_archivo, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()

        with open(cls.__ruta_archivo, 'a', newline='\n') as file:
            anidar = csv.writer(file)
            anidar.writerow(cls.__libros)
            file.close()