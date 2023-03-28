


def nombre_veces():
    nombre = "Yuri Johana Naranjo Ariza"
    veces = int(input("Ingrese la cantidad de veces que quiere repetir su nombre: "))
    for i in range(veces):

        print(nombre) 

def programa():

    menu = int(input("""Ingrese una opción: 
[1] Repetir nombre.
[2] Salir.    
"""))
    if menu == 1:
        nombre_veces()
    elif menu == 2:
        exit()
    else:
        print("No es una opción valida, intentelo de nuevo..")
while True:
    programa()

