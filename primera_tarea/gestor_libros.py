import csv
from typing import List
from libros import Libro

class Gestor_libros:
    __ruta_archivo = "libros.csv"
    __libros: List[Libro]= []
    
    @classmethod
    def cargar_archivo(cls) -> None:
        #abre el archivo y guarda los libros en memoria
        with open(cls.__ruta_archivo,encoding="utf8") as f:
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
        for lib in cls.__libros:
            lib.listar()
            print("---------")
    
    @classmethod
    def agregar_libro(cls, **datos) -> None:
        #carga un libro en la lista de libros
        libro = Libro(
            datos["titulo"],
            datos["genero"],
            datos["isbn"],
            datos["editorial"],
            datos["autores"]
        )
        cls.__libros.append(libro)
    
    @classmethod
    def eliminar_libro(cls,id: int) -> None:
        #elimina un libro, segun su id, de la lista
        for lib in cls.__libros:
            if id == lib[0]:
                cls.__libros.remove(id)
    
    #Filtra los libros segun en tipo: 
    @classmethod
    def buscar_libro_isbn(cls, clave: str) -> Libro:
        for lib in cls.__libros:
            if clave == lib.get_isbn():
                return lib
    
    @classmethod
    def buscar_libro_titulo(cls, clave: str) -> List[Libro]:
        libros = []
        for lib in cls.__libros:
            if clave == lib.get_titulo():
                libros.append(lib)
        return libros
    
    # #Filtra los libros segun el criterio elegido:
    # def convert_author_list(author: str) -> List:
    #     autor = ""
    #     lista_autores = []
    #     for i in author:
    #         if i == ',':
    #             lista_autores.append(autor)
    #             autor = ""
    #             continue
    #         autor += i
    #     lista_autores.append(autor)
    #     return lista_autores
    
    @classmethod
    def buscar_libro_autor(cls, clave: str) -> List[Libro]:
        libros = []
        for lib in cls.__libros:
            if clave in lib.get_autores():
                libros.append(lib)
        return libros
    
    #Filtra los libros segun el criterio elegido: 
    @classmethod
    def buscar_libro_editorial(cls, clave: str) -> List[Libro]:
        libros = []
        for lib in cls.__libros:
            if clave == lib.get_editorial():
                libros.append(lib)
        return libros
    
    @classmethod
    def buscar_libro_genero(cls, clave: str) -> List[Libro]:
        libros = []
        for lib in cls.__libros:
            if clave == lib.get_genero():
                libros.append(lib)
        return libros
    
    @classmethod
    def buscar_libro_num_autores(cls,clave: int) -> List[Libro]:
        libros = []
        for lib in cls.__libros:
            if clave == len(lib.get_autores()):
                print(len(lib.get_autores()))
                libros.append(lib)
        return libros
    
    @classmethod
    def ordenar_libros(cls) -> None:
        #Ordena la lista segun sus titulos
        cls.__libros.sort(key=lambda libro: libro.get_titulo(),reverse=True)
    
    @classmethod
    def actualizar_libro(cls,**datos) -> None:
        #Actualiza los datos de un libro
        for lib in cls.__libros:
            if lib.get_isbn() == datos['isbn']:
                libro = Libro(datos)
                lib = libro
    
    @classmethod
    def grabar_archivo(cls) -> None:
        #Graba la lista de libros en el archivo
        with open(cls.__ruta_archivo, 'a', newline='\n') as file:
            anidar = csv.writer(file)
            anidar.writerow(cls.__libros)
            file.close()