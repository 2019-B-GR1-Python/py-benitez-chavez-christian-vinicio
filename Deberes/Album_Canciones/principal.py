import album
import sys

def menu_options(value):
    try:
        return {
            0: None,
            1: album_options,
            2: songs_options,
        }[value]
    except KeyError:
        print("No existe esta opcion")


def album_options_select(value):
    try:
        return {
            0: None,
            1: album.create_album,
            2: album.read_album,
            3: album.update_album,
            4: album.delete_album,
        }[value]
    except KeyError:
        print("No existe esta opcion")
        


# def song_options_select(value):
#     try:
#         return {
#             0: None,
#             1: create_song,
#             2: read_song,
#             3: update_song,
#             4: delete_song,
#         }[value]
#     except KeyError:
#         print("No existe esta opcion")


def album_options(option):
    print("\nMENU ALBUM:")
    print("1. Crear un nuevo album")
    print("2. Ver todos los albumes")
    print("3. Actualizar album")
    print("4. Eliminar album")
    #print("5. Regresar al menu principal")

    select_option = input("Elija una opcion:")
    if(select_option.isnumeric()):
        option = int(select_option)

    try:
        album_options_select(option)()
    except TypeError:
        #print(f"Opcion: {option}")
        print("")
    


def songs_options(option):
    print("\nMENU CANCIONES:")
    print("1. Crear una nueva cancion")
    print("2. Ver todas las canciones")
    print("3. Actualizar cancion")
    print("4. Eliminar cancion")

    select_option = input("Elija una opcion:")
    if(select_option.isnumeric()):
        option = int(select_option)

    try:
        menu_options(option)()
    except TypeError:
        #print(f"Opcion: {option}")
        print("")


def principal(option):
    #while option!=0:
    print("\n**********************")
    print("* MENU PRINCIPAL:    *")
    print("* 1. Album           *")
    print("* 2. Canciones       *")
    print("* 3. Salir           *")
    print("**********************")

    select_option = input("Elija una opcion:")
    if(select_option.isnumeric()):
        option = int(select_option)
    
    if(option == 1):
        album_options("Album")
    elif(option == 2):
        songs_options("Cancion")
    elif(option == 3):
        print("Saliendo del programa...")
        sys.exit()
    else:
        #print("No existe esa opcion. Escoja una opcion correcta")
        print("\n")        

    try:
        menu_options(option)()
    except TypeError:
        #print(f"Opcion: {option}")
        print("")

principal(-1)





