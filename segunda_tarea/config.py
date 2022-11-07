import os
from colorama import Fore
from typing import Dict
import pokeapi

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

def imprimir_cabezeras(mensaje:str):
    limpiar_consola()
    print(f'{Fore.GREEN}'+'='*(len(mensaje)+10)+f'{Fore.RESET}')
    print(f'{mensaje}'.center(len(mensaje)+10))
    print(f'{Fore.GREEN}'+'='*(len(mensaje)+10)+f'{Fore.RESET}')

def ejecutar_menu(menu: Dict,cabecera:str):
    opciones = menu
    numero_opciones = len(opciones.keys())
    imprimir_menu(opciones,cabecera)
    opcion = mensaje_opcion(f"Ingrese una opcion del 1 al {numero_opciones}",numero_opciones)
    if opcion != numero_opciones:
        ejecutar_opcion(opciones,opcion)
    return opcion

def imprimir_menu(opciones: Dict,cabecera: str) -> None:
    limpiar_consola()
    size = [len(opciones[clave][0]) for clave in opciones]
    
    if len(size) > 10:
        imprimir_menu_col(opciones,cabecera,10)
        return
    
    if len(cabecera) > max(size): largo = len(cabecera)
    else: largo = max(size)+2
    
    print("="*(largo + 7))
    print("|"+cabecera.center(largo + 5)+"|")
    print("="*(largo + 7))
    
    for clave in opciones:
        print(f"|{clave:3}: {opciones[clave][0]:{largo}}|")
    
    print("="*(largo + 7))

def imprimir_menu_col(opciones: Dict, cabecera:str, num_filas:int) -> None:
    claves = list(opciones.keys())
    def generador_col(lista,n):
        for i in range(0,len(lista),n):
                yield claves[i:i+n]

    columnas = list(generador_col(claves,num_filas))
    filas = []
    for i in range(num_filas):
        aux = []
        for col in columnas:
            try: aux.append(col[i])
            except: pass
        filas.append(aux)
    
    largo = len(" | ".join(f"{clave:2}. {opciones[clave][0]}" for clave in filas[0]))
    largo2 = largo + 10
    print("="*(largo2+6))
    print("|"+cabecera.center(largo2+4)+"|")
    print("="*(largo2+6))
    l = largo//2
    
    for f in filas:
        print("| ",end="")
        print(" | ".join(f"{clave:2}. {opciones[clave][0]:{l}}" for clave in f),end="")
        if len(f) != len(columnas):
            print(" | "+" "*(l+4)+"  |")
            continue
        print("  |")
    
    print("="*(largo2+6))
    
def ejecutar_opcion(opciones: Dict, opcion: int) -> None:
    #Ejecuta las opciones y da una pausa antes de continuar
    opciones[opcion][1]()

def menu_principal() -> Dict:
    opciones = {
        1: ("Listar pokemons por generación.",pokeapi.listar_pokemon_generacion),
        2: (
            "Listar pokemons por forma.",
            lambda a=menu_forma(), b="FORMAS DE POKEMON": ejecutar_menu(a,b)
            ),
        3: ("Listar pokemons por habilidad.",pokeapi.listar_pokemon_habilidad),
        4: (
            "Listar pokemons por hábitat.",
            lambda a=menu_habitat(), b="HABITATS DE POKEMON": ejecutar_menu(a,b)
            ),
        5: ("Listar pokemons por tipo.",
            lambda a=menu_tipo(), b="TIPOS DE POKEMON": ejecutar_menu(a,b)),
        6: ("Salir.",salir)
    }
    return opciones

def menu_habitat() -> Dict:
    opciones = {
        1: ("Cuevas",lambda a=1,b="Cuevas": pokeapi.listar_pokemon_habitat(a,b)),
        2: ("Bosque",lambda a=2,b="Bosque": pokeapi.listar_pokemon_habitat(a,b)),
        3: ("Pradera",lambda a=3,b="Pradera": pokeapi.listar_pokemon_habitat(a,b)),
        4: ("Montañas",lambda a=4,b="Montañas": pokeapi.listar_pokemon_habitat(a,b)),
        5: ("Extraño",lambda a=5,b="Extraño": pokeapi.listar_pokemon_habitat(a,b)),
        6: ("Campo",lambda a=6,b="Campo": pokeapi.listar_pokemon_habitat(a,b)),
        7: ("Mar",lambda a=7,b="Mar": pokeapi.listar_pokemon_habitat(a,b)),
        8: ("Ciudad",lambda a=8,b="Ciudad": pokeapi.listar_pokemon_habitat(a,b)),
        9: ("Agua dulce",lambda a=9,b="Agua dulce": pokeapi.listar_pokemon_habitat(a,b)),
        10: ("Volver",salir),
    }
    return opciones

def menu_tipo() -> Dict:
    opciones = {
        1: ("Normal",lambda a=1,b="Normal": pokeapi.listar_pokemon_tipo(a,b)),
        2: ("Lucha",lambda a=2,b="Lucha": pokeapi.listar_pokemon_tipo(a,b)),
        3: ("Volador",lambda a=3,b="Volador": pokeapi.listar_pokemon_tipo(a,b)),
        4: ("Veneno",lambda a=4,b="Veneno": pokeapi.listar_pokemon_tipo(a,b)),
        5: ("Tierra",lambda a=5,b="Tierra": pokeapi.listar_pokemon_tipo(a,b)),
        6: ("Roca",lambda a=6,b="Roca": pokeapi.listar_pokemon_tipo(a,b)),
        7: ("Insecto",lambda a=7,b="Insecto": pokeapi.listar_pokemon_tipo(a,b)),
        8: ("Fantasma",lambda a=8,b="Fantasma": pokeapi.listar_pokemon_tipo(a,b)),
        9: ("Acero",lambda a=9,b="Acero": pokeapi.listar_pokemon_tipo(a,b)),
        10: ("Fuego",lambda a=10,b="Fuego": pokeapi.listar_pokemon_tipo(a,b)),
        11: ("Agua",lambda a=11,b="Agua": pokeapi.listar_pokemon_tipo(a,b)),
        12: ("Hierba",lambda a=12,b="Hierba": pokeapi.listar_pokemon_tipo(a,b)),
        13: ("Electrico",lambda a=13,b="Electrico": pokeapi.listar_pokemon_tipo(a,b)),
        14: ("Psíquico",lambda a=14,b="Psíquico": pokeapi.listar_pokemon_tipo(a,b)),
        15: ("Hielo",lambda a=15,b="Hielo": pokeapi.listar_pokemon_tipo(a,b)),
        16: ("Dragón",lambda a=16,b="Dragón": pokeapi.listar_pokemon_tipo(a,b)),
        17: ("Siniestro",lambda a=17,b="Siniestro": pokeapi.listar_pokemon_tipo(a,b)),
        18: ("Hada",lambda a=18,b="Hada": pokeapi.listar_pokemon_tipo(a,b)),
        19: ("Volver",salir)
    }
    return opciones

def menu_forma() -> Dict:
    opciones = {
        1: ("Solo Cabeza",lambda a=1,b="Solo Cabeza": pokeapi.listar_pokemon_forma(a,b)),
        2: ("Alargados",lambda a=2,b="Alargados": pokeapi.listar_pokemon_forma(a,b)),
        3: ("Pez",lambda a=3,b="Pez": pokeapi.listar_pokemon_forma(a,b)),
        4: ("Cabeza con brazos",lambda a=4,b="Cabeza con brazos": pokeapi.listar_pokemon_forma(a,b)),
        5: ("Cabeza con base",lambda a=5,b="Cabeza con base": pokeapi.listar_pokemon_forma(a,b)),
        6: ("Bípedos + cola",lambda a=6,b="Bípedos + cola": pokeapi.listar_pokemon_forma(a,b)),
        7: ("Bípedos sin brazos",lambda a=7,b="": pokeapi.listar_pokemon_forma(a,b)),
        8: ("Cuadrúpedos",lambda a=8,b="Cuadrúpedos": pokeapi.listar_pokemon_forma(a,b)),
        9: ("Alados",lambda a=9,b="Alados": pokeapi.listar_pokemon_forma(a,b)),
        10: ("Tentáculos",lambda a=10,b="Tentáculos": pokeapi.listar_pokemon_forma(a,b)),
        11: ("Varias cabezas",lambda a=11,b="Varias cabezas": pokeapi.listar_pokemon_forma(a,b)),
        12: ("Humanoides",lambda a=12,b="Humanoides": pokeapi.listar_pokemon_forma(a,b)),
        13: ("Muchas alas",lambda a=13,b="Muchas alas": pokeapi.listar_pokemon_forma(a,b)),
        14: ("Artrópodos",lambda a=14,b="Artrópodos": pokeapi.listar_pokemon_forma(a,b)),
        15: ("Volver",salir)
    }
    return opciones

def salir():
    pass