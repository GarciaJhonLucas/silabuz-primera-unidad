import os
from colorama import Fore
from gestion_libros import Gestor_libros

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el SO es Windows, cambia a 'cls'
        command = 'cls'
    os.system(command)