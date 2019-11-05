def create_album():
    
    print("\nIngrese las caracteristicas del album:")
    name_album = input("--> Ingrese el nombre del album: ")
    author_album = input("--> Ingrese el autor del album: ")
    year_album = input("--> Ingrese el año de publicacion del album: ")
    total_songs = input("--> Ingrese la cantidad de canciones del album: ")
    album =  name_album + "\t\t" + author_album + "\t\t\t" + year_album + "\t\t\t" + total_songs + "\n"

    try:
        create_file_album = open('./archivo_album.txt', 'a')
        for line in album:
            create_file_album.write(line)
        create_file_album.close()
        print("El album se ha ingresado correctamente!!!")
    except:
        print("Error. El album no se ha guardado!!!")

    


def read_album():
    try:
        open_file = open('./archivo_album.txt')
        content = open_file.readlines()
        print("\n")
        print("Nombre album\t\tAutorAlbum\t\tAnio publicacion\tTotal canciones")
        for line in content:
            print(line)
        
        open_file.close()

        #print("El album se está leyendo")
    except:
        print("El archivo no se ha encontrado!!!")
    


def update_album():
    album_list = []

    try:
        open_file = open('./archivo_album.txt')
        content = open_file.readlines()
        print("\n")
        print("Nombre album\t\tAutorAlbum\t\tAnio publicacion\tTotal canciones")
        for line in content:
            album_list.append(line)
            print(line)
        
        

        def options(value):
            try:
                return{
                    0: None,
                    1: print("Actualizando nombre del album"),
                    2: print("Actualizando nombre del autor"),
                    3: print("Actualizando anio del album"),
                    4: print("Actualizando total de canciones del album"),
                }[value]
            except KeyError:
                print("No existe esa opcion!!!")
        

        
            
        


        album_name = input("Ingrese el nombre de album que desea modificar: ")
        array = album_list[0].split('\t') 
        print(f"\nIndique que opción desea modificar del album: {array[0]}")
        #print(array[0])
        print("1. Modificar -> Nombre del album")
        print("2. Modificar -> Autor del album")
        print("3. Modificar -> Anio del album")
        print("4. Modificar -> Total de canciones del album")
        option = input("Elija una opcion: ")

        if (option.isnumeric()):
            update_option = int(option)
            
        try:
            #update_item = options(update_option)
            options(update_option)()
        except TypeError:
            print("")

        
        

        open_file.close()


    except:
        print("El archivo no se ha encontrado!!!")


    

    #print("El album se está actualizando")




def delete_album():
    #array = []
    #item = ""
    try:
        open_file = open('./archivo_album.txt')
        album_list = []
        content = open_file.readlines()
        print("\nNombre album\t\tAutorAlbum\t\tAnio publicacion\tTotal canciones")
        for lines in content:
            print(lines)
        
        
        album_a_eliminar = input("Ingrese el nombre del album que desea eliminar: ")
        for lines in content:
            #print(lines)
            if not album_a_eliminar in lines:
                album_list.append(lines)
            #album_list.append(lines)
            
        open_file.close()

        open_file = open('./archivo_album.txt','w')
        open_file.writelines(album_list)
        open_file.close
        

        #album = input("Ingrese el nombre del album que desea eliminar: ")
        #print(album_list[0].split('\t'))
        
        #Datos de una fila almacenados en un array
        #array = album_list[0].split('\t') 
        #Saber en que posicion se encuentra cierto elemento
        #print(int(album_list[1].index(album)))
        #Dato en una posicion estabelcida
        #print(array[0])
        #inf_eliminada = int(album_list.index(album_list[0]))
        #print(inf_eliminada)
        #print(album_list.pop(inf_eliminada))
        #album_list.pop(inf_eliminada)
        #print(array)
        # print("El dato a eliminar es: "+album_list.pop(array[0]))
        #open('./archivo_album', 'w').writelines(line[inf_eliminada])
        #open_file.close()
       
    except:
        print("El album escogido no existe!!!")
    






















































# def actualizar_auto(auto,actualizar):
#     lineas = listar_autos()
#     index = lista.index(auto)
#     auto.update(actualizar)
#     lista[index] = auto
#     print(f"Actualizando auto con placa {auto['placa']}")


# def listar_autos():
#     archivo_auto = leer_archivo_auto('./autos.txt')
#     auto = []
#     for lista in archivo_auto:
#         auto.append(cadenas.convertir_cadena(lista))
#     return auto


# def leer_archivo_auto(path):
#     try:
#         lineas = []
#         archivo = open(path,mode='r')
#         arreglo_lineas_archivo = archivo.readlines()
#         for linea in arreglo_lineas_archivo:
#             lineas.append(linea)
#         archivo.close()
#         return lineas
#     except Exception:
#         print("No se puede leer el archivo: " + path)    


# def convertir_cadena(linea):
#     cadena = (linea + '').replace('\n','').split(';')
#     datos = {
#         'placa' : cadena[0],
#         'color'   : cadena[1],
#         'modelo'   : cadena[2],
#         'precio'   : cadena[3],
#         'hp'   : cadena[4],
#     }
#     return datos