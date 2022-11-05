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