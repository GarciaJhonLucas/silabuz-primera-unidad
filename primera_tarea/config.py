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
