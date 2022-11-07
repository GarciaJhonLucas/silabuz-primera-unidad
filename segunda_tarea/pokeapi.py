import config
import requests
from typing import Dict

URL = f"https://pokeapi.co/api/v2/"
URL_POKEMON = f"https://pokeapi.co/api/v2/pokemon/"

def listar_pokemon(ruta: str,param_id: int) -> Dict: #Generador de pokemon
    response = requests.get(URL+f"{ruta}/{param_id}")
    pokemon_data = response.json()
    pokemon_id = []
    try:
        pokemon_species = pokemon_data['pokemon_species']
        for pkmn in pokemon_species:
            num_url = int(pkmn['url'][42:-1])
            pokemon_id.append(num_url)
    except:
        print("DATO BUSCADO: ",pokemon_data["name"])
        print("------")
        pokemon_species = pokemon_data['pokemon']
        for pkmn in pokemon_species:
            num_url = int(pkmn['pokemon']['url'][34:-1])
            pokemon_id.append(num_url)
    
    pokemon_id.sort()
    for id in pokemon_id:
        pkmn = get_pokemon(id)
        yield pkmn
          
def get_pokemon(id: int) -> Dict:
    #solo nombre, habilidades e imagen
    response = requests.get(URL_POKEMON+f'{id}')
    pokemon_data = response.json()
    data = {
        'name':pokemon_data['name'],
        'abilities' : [pkmn['ability']['name'] for pkmn in pokemon_data['abilities']],
        'url': f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    }
    return data

def listar_pokemon_generacion() -> None:
    config.imprimir_cabezeras('BUSCAR POR GENERACION')
    numero_generacion = config.mensaje_opcion('Ingrese el número de generacion desde el 1 al 8',8)
    
    config.imprimir_cabezeras(f'LISTA DE POKEMON DE LA GENERACION {numero_generacion}')
    for i,pkmn in enumerate(listar_pokemon("generation",numero_generacion)):
        print("Nombre".ljust(11)+":",pkmn['name'])
        print("Habilidades:",", ".join(pkmn['abilities']))
        print("Imagen".ljust(11)+":",pkmn['url'])
        print("------")

def listar_pokemon_forma(opcion: int,forma: str)->None:
    config.imprimir_cabezeras('POKEMON CON LA FORMA '+f'{forma}'.upper())
    for i,pkmn in enumerate(listar_pokemon("pokemon-shape",opcion)):
        print("Nombre".ljust(11)+":",pkmn['name'])
        print("Habilidades:",", ".join(pkmn['abilities']))
        print("Imagen".ljust(11)+":",pkmn['url'])
        print("------")

def listar_pokemon_habilidad() -> None:
    config.imprimir_cabezeras('BUSCAR POKEMON POR HABILIDAD')
    numero_habilidad = config.mensaje_opcion('Ingrese el número de habilidad (1-267)',267)
    
    config.imprimir_cabezeras(f'LISTA DE POKEMON POR HABILIDAD')
    for i,pkmn in enumerate(listar_pokemon("ability",numero_habilidad)):
        print("Nombre".ljust(11)+":",pkmn['name'])
        print("Habilidades:",", ".join(pkmn['abilities']))
        print("Imagen".ljust(11)+":",pkmn['url'])
        print("------")

def listar_pokemon_habitat(opcion: int,habitat: str) -> None:
    config.imprimir_cabezeras('LISTA DE POKEMON DE '+f'{habitat}'.upper())
    for i,pkmn in enumerate(listar_pokemon("pokemon-habitat",opcion)):
        print("Nombre".ljust(11)+":",pkmn['name'])
        print("Habilidades:",", ".join(pkmn['abilities']))
        print("Imagen".ljust(11)+":",pkmn['url'])
        print("------")

def listar_pokemon_tipo(opcion: int,tipo: str) -> None:
    config.imprimir_cabezeras('LISTA DE POKEMON DE TIPO '+f'{tipo}'.upper())
    for i,pkmn in enumerate(listar_pokemon("type",opcion)):
        print("Nombre".ljust(11)+":",pkmn['name'])
        print("Habilidades:",", ".join(pkmn['abilities']))
        print("Imagen".ljust(11)+":",pkmn['url'])
        print("------")