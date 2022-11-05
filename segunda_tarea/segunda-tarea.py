import os
import menu
import config
import requests

URL = f"https://pokeapi.co/api/v2/"
URL_POKEMON = f"https://pokeapi.co/api/v2/pokemon/"

def get_habilidad(nombre_pokemon:str)->str:
    response = requests.get(f'{URL_POKEMON}{nombre_pokemon}')
    pokemon_data = response.json()
    habilidades = ''
    for item in pokemon_data['abilities']:
        habilidades += item['ability']['name'] + ' '
    return habilidades

def get_image_pokemon(nombre_pokemon: str)->str:
    url_imagen_pokemon = ''
    response = requests.get(f'{URL_POKEMON}{nombre_pokemon}')
    pokemon_data = response.json()
    return pokemon_data['sprites']["front_default"]

def listar_pokemon_generacion() -> None:
    config.imprmir_cabezeras('BUSCAR POR GENERACION')
    numero_generacion = config.mensaje_opcion('Ingrese el número de generacion desde el 1 al 8')

    if numero_generacion > 0 and numero_generacion <= 8:
        response = requests.get(URL+f"generation/{numero_generacion}")
        pokemon_data = response.json()
        config.imprmir_cabezeras(f'Lista de Pokemons de la generacion - {numero_generacion}')

        for item in pokemon_data['pokemon_species']:
            print(f'Nombre: { item["name"].capitalize() }')
            print('Habilidades: ' + get_habilidad(item["name"]))
            print(f'Imagen: { get_image_pokemon(item["name"]) }\n')
    else:
        config.imprimir_errores('La opcion que ingreso no es correcta.')


def listar_pokemon_forma()->None:
    config.imprmir_cabezeras('FORMA DE POKEMONS')
    menu.menu_forma_pokemon()
    numero_forma = config.mensaje_opcion('Ingrese el número de ID del pokemon')

    if numero_forma > 0 and numero_forma <= 500:
        response = requests.get(URL+f"pokemon-form/{numero_forma}")
        pokemon_data = response.json()
        lista_pokemon = pokemon_data['pokemon']
        print(f'Nombre: { pokemon_data["name"].capitalize() }' )
        print(f'Habilidades: { get_habilidad(pokemon_data["name"]) }')
        print(f'Nombre: { pokemon_data["sprites"]["back_default"] }' )
    else:
        config.imprimir_errores('La opcion que ingreso no es correcta.')
