

def menuPrincipal():
    opcion = 0
    while True:
        print("************MENÚ PRINCIPAL**************")
        print("*1. CRUD de Profesores                 *")
        print("*2. CRUD de Alumnos                    *")
        print("*3. Salir                              *")
        print("****************************************")

        try:
            opcion = int(input('Ingrese una de las opciones: '))
            match opcion:
                case 1:
                    menuProfe()
                case 2:
                    menuAlumno()
                case 3:
                    print("Saliendo........")
                    break
                case _:
                    print("ERROR: Ingresó un número fuera de las opciones mostradas")
                    print("Por favor ingrese una de las opciones mostradas")
                    print("   ")
        except ValueError:
            print("ERROR: Ingresó un caracter diferente a un número entero")
            print("Por favor ingrese un número de las opciones mostradas")
            print(" ")

def menuProfe():
    opcion = 0
    while True:
        print("************CRUD PROFESOR***************")
        print("*1. Crear Profesor                     *")
        print("*2. Leer Profesor                      *")
        print("*3. Actualizar Profesor                *")
        print("*4. Eliminar Profesor                  *")
        print("*5. Regresar al MENU PRINCIPAL          *")
        print("****************************************")

        try:
            opcion = int(input('Ingrese una de las opciones mostradas'))
            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    menuPrincipal()
                case _:
                    print("Por favor ingrese una de las opciones válidas del menú")
                    print(" ")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero")
            print(" ")

def menuAlumno():
    pass


#Correr el Main
if __name__=="__main__":
    menuPrincipal()