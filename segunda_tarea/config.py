import os
from colorama import Fore
from typing import Dict

def limpiar_consola() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el SO es Windows, cambia a 'cls'
        command = 'cls'
    os.system(command)

def mensaje_opcion(mensaje:str, salida: int)->int:
    valor=""
    while True:
        valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
        if valor != '' and valor.isnumeric() and int(valor) < salida + 1:
            break
        imprimir_errores('Opcion no es valida, Ingrese un numero')
    return int(valor)

def imprimir_errores(mensaje:str)->None:
    print(Fore.RED+'[Error]'+Fore.RESET+' '+mensaje )

def imprimir_informacion()->None:
    input(Fore.GREEN+'[Mensaje]'+Fore.RESET+' Presione Enter Para Continuar')

def imprmir_cabezeras(mensaje:str):
    limpiar_consola()
    print(f'{Fore.GREEN}'+'='*(len(mensaje)+10)+f'{Fore.RESET}')
    print(f'{mensaje}'.center(len(mensaje)+10))
    print(f'{Fore.GREEN}'+'='*(len(mensaje)+10)+f'{Fore.RESET}')