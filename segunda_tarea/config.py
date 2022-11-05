import os
import requests
from colorama import Fore

def mensaje_opcion(mensaje:str)->int:
    valor=""
    while True:
        valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
        if valor != '' and valor.isnumeric():
            break
        else:
            imprimir_errores('Opcion no es valida, Ingrese un numero')
            valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
    return int(valor)

def imprimir_errores(mensaje:str)->None:
    print(Fore.RED+'[Error]'+Fore.RESET+' '+mensaje )

def imprmir_cabezeras(mensaje:str):
    os.system('clear')
    print(f'''{Fore.GREEN}================================================={Fore.RESET}
    {mensaje}\n{Fore.GREEN}================================================={Fore.RESET}''')