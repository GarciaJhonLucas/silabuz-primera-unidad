class Libro:
    __id = 1
    
    def __init__(self,
                 titulo: str, 
                 genero: str, 
                 isbn: str, 
                 editorial: str, 
                 autores: str
                 ) -> None:
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autores = autores.split(";")
        self.__id = Libro.__id
        Libro.__id += 1 #id autoincrementable
    
    def listar(self) -> None:
        print("Titulo: ",self.__titulo)
        print("Genero: ",self.__genero)
        print("ISBN: ",self.__isbn)
        print("Editorial: ", self.__editorial)
        print("Autor(es):",", ".join(self.__autores))
        
    def get_titulo(self) -> str:
        return self.__titulo