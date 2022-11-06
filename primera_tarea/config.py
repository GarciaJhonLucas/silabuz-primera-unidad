import os
from colorama import Fore
from gestion_libros import Gestor_libros

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el SO es Windows, cambia a 'cls'
        command = 'cls'
    os.system(command)
    
def mensaje_opcion(mensaje:str, salida: int)-> str:
    valor=""
    while True:
        valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
        if valor != '' and valor.isnumeric() and int(valor) < salida + 1:
            break
        imprimir_errores('Opcion no es valida, Ingrese un numero')
    return valor

def imprimir_errores(mensaje:str)->None:
    print(Fore.RED+'[Error]'+Fore.RESET+' '+mensaje )

def imprimir_informacion()->None:
    input(Fore.GREEN+'[Mensaje]'+Fore.RESET+' Precione Enter para continuar')

def imprimir_menu(opciones,cabecera):
    limpiar_consola()
    size = [len(opciones[clave][0]) for clave in opciones]
    
    if len(cabecera) > max(size): largo = len(cabecera)+ 2
    else: largo = max(size) + 2
    
    print("="*(largo + 8))
    print("|"+cabecera.center(largo + 6)+"|")
    print("="*(largo + 8))
    
    for clave in opciones:
        cad_clave = f"{clave}: ".rjust(6)
        cad_opciones = f"{opciones[clave][0]}".ljust(largo)
        print("|" + cad_clave + cad_opciones + "|")
    
    print("="*(largo + 8))

def menu_principal():
    opciones = {
        '1': ("Leer archivo.",opcion1),
        '2': ("Listar libros.",opcion2),
        '3': ("Agregar libro",opcion3),
        '4': ("Eliminar Libro",opcion4),
        '5': ("Buscar libros por ISBN o titulo",opcion5),
        '6': ("Ordenar libros por titulo",opcion6),
        '7': ("Buscar libros por autor, editorial o genero",opcion7),
        '8': ("Buscar libros por numero de autores",opcion8),
        '9': ("Editar libro",opcion9),
        '10': ("Guardar libros al archivo",opcion10),
        '11': ("Salir",)
    }
    imprimir_menu(opciones,"CONFIGURA LIBROS")
    opcion = mensaje_opcion("Seleccione una opcion del 1 al 11",11)
    if opcion != '11':
        ejecutar_opcion(opciones,opcion)
    return opcion

def ejecutar_opcion(opciones, opcion):
    #Ejecuta las opciones y da una pausa antes de continuar
    opciones[opcion][1]()
    imprimir_informacion()

def opcion1():
    #cargar libros del archivo a la memoria
    Gestor_libros.cargar_archivo()

def opcion2():
    #listar libros
    Gestor_libros.listar_libros()

def opcion3():
    Gestor_libros.agregar_libro()
    pass

def opcion4():
    opciones = {
        '1': ("Ingresar Id Libro.",opcion4),
        '2': ("Volver",)
    }
    while True:
        imprimir_menu(opciones,"Eliminar Libro mediante Id".upper())
        opcion = mensaje_opcion("Seleccione una opcion del 1 al 2",2)
        if opcion == '2':
            break
    Gestor_libros.eliminar_libro(id)
    

def opcion5():
    #Menu de la opcion 5
    opciones = {
        '1': ("Buscar por ISBN.",opcion5_1),
        '2': ("Buscar por Titulo de libro",opcion5_2),
        '3': ("Volver",)
    }
    while True:
        imprimir_menu(opciones,"Buscar libros por ISBN o titulo".upper())
        opcion = mensaje_opcion("Seleccione una opcion del 1 al 3",3)
        if opcion == '3':
            break
        ejecutar_opcion(opciones,opcion)
    
def opcion5_1():
    Gestor_libros.buscar_libro_isbn(clave)

def opcion5_2():
    pass

def opcion6():
    Gestor_libros.ordenar_libros()

def opcion7():
    #Menu de la opcion 7
    opciones = {
        '1': ("Buscar por autor.",opcion7_1),
        '2': ("Buscar por editorial",opcion7_2),
        '3': ("Buscar por genero",opcion7_3),
        '4': ("Volver",)
    }
    while True:
        imprimir_menu(opciones,"Buscar libros por autor, editorial o genero".upper())
        opcion = mensaje_opcion("Seleccione una opcion del 1 al 4",4)
        if opcion == '4':
            break
        ejecutar_opcion(opciones,opcion)

def opcion7_1():
    #buscar por autor
    pass

def opcion7_2():
    #buscar por editorial
    pass

def opcion7_3():
    #buscar por genero
    pass

def opcion8():
    #muestra los libros que tengan la cantidad ingresada de autores
    pass

def opcion9():
    #edita un libro
    pass

def opcion10():
    #Graba en el archivo
    pass