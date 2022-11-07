import config

if __name__ == "__main__":
    salida = 0
    while salida != len(config.menu_principal()):
        salida = config.ejecutar_menu(config.menu_principal(),"POKEMON API")
        config.imprimir_informacion()