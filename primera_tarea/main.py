import config_menu

if __name__ == "__main__":
    opcion = '0'
    
    while int(opcion) != 11:
        opcion = config_menu.menu_principal()
        #config_menu.imprimir_informacion()
        # opciones = config_menu.menu_principal()
        # opcion = config_menu.mensaje_opcion("Seleccione una opcion del 1 al 11",11)
        # print(opcion)
        # config_menu.ejecutar_opcion(opciones,opcion)
    print("HASTA LA PROXIMA")