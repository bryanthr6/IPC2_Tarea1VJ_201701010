#Importar las personas para la lista
#No se importa persona porque solo queremos almacenar en lista a profesores y alumnos
from profesor import Profesor
from alumno import Alumno

#contador global para indentificar
id_personas = 0

#Crear lista GENERAL
profesores = []
alumnos = []

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
                    print("[ERROR] Ingresó un número fuera de las opciones mostradas")
                    print("Por favor, ingrese una de las opciones mostradas en el menu")
                    print("   ")
        except ValueError:
            print("[ERROR] Ingresó un caracter diferente a un número entero")
            print("Por favor, ingrese un número entero de las opciones mostradas")
            print(" ")

def menuProfe():
    opcion = 0
    while True:
        print("************CRUD PROFESOR***************")
        print("*1. Crear Profesor                     *")
        print("*2. Leer Profesor                      *")
        print("*3. Actualizar Profesor                *")
        print("*4. Eliminar Profesor                  *")
        print("*5. Regresar al MENU PRINCIPAL         *")
        print("****************************************")

        try:
            opcion = int(input('Ingrese una de las opciones mostradas: '))
            match opcion:
                case 1:
                    crearProfesor()
                case 2:
                    verProfesor()
                case 3:
                    editarProfesor()
                case 4:
                    eliminarProfesor()
                case 5:
                    return #regresa el menú principal
                case _:
                    print("[ERROR] Ingresó un número fuera de las opciones mostradas")
                    print("Por favor, ingrese una de las opciones mostradas en el menú")
                    print(" ")
        except ValueError:
            print("[ERROR] Ingresó un caracter diferente a un número entero")
            print("Por favor, ingrese un número entero dentro de las opciones mostradas")
            print(" ")

def menuAlumno():
    opcion = 0
    while True:
        print("**************CRUD ALUMNO***************")
        print("*1. Crear Alumno                       *")
        print("*2. Leer Alumno                        *")
        print("*3. Actualizar Alumno                  *")
        print("*4. Eliminar Alumno                    *")
        print("*5. Regresar al MENU PRINCIPAL         *")
        print("****************************************")

        try:
            opcion = int(input('Ingrese una de las opciones mostradas: '))
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
                    return #Regresa al menú principal
                case _:
                    print("[ERROR] Ingresó un número fuera de las opciones mostradas")
                    print("Por favor, ingrese una de las opciones mostradas en el menú")
                    print(" ")
        except ValueError:
            print("[ERROR] Ingresó un caracter diferente a un número entero")
            print("Por favor, ingrese un número entero dentro de las opciones mostradas")
            print(" ")

#Crear Profesores
def crearProfesor():
    global id_personas
    global profesores

    print("*****************CREAR PROFESOR*****************")
    id = id_personas
    nombre = input('Ingrese el NOMBRE del profesor: ')
    curso = input('Ingrese el CURSO que imparte: ')
    codigo = input('Ingrese el CÓDIGO del profesor: ')
    profesion = input('Ingrese la PROFESIÓN del profesor: ')
    print(" ")
    print("¡Profesor creado Correctamente!")

    #Teniendo los datos ingresados se procede a crear a un profesor
    nuevo = Profesor(nombre, curso, codigo, profesion)
    profesores.append(nuevo)
    id_personas += 1

#Mostrar la lista de profesores
def verProfesor():
    global profesores
    print("****************VER PROFESORES***************")
    for profesor in profesores:
        json_string = '''
{
    Nombre: ''' +str(profesor.getNombre())+''',
    Curso: ''' +str(profesor.getCurso())+''',
    Código: ''' +str(profesor.getCodigo())+''',
    Profesión: ''' +str(profesor.getProfesion())+'''

}
'''
        print(json_string)

#Método para editar Profesores
def editarProfesor():
    global profesores
    print("**************ACTUALIZAR PROFESOR*********************")
    codigo = input('Ingrese el código del profesor para ACTUALIZAR: ')

    #Variable nos ayuda a notificarle al ususario si no se encuentra el código de profesor que ingresó en la lista
    profesor_encontrado = None
    for profesor in profesores:
        if profesor.getCodigo() == codigo:
            profesor_encontrado = profesor
            break

    if profesor_encontrado is None:
        print("[ERROR] No se encontró un profesor con el código ingresado.")
        return
    
    nombre = input('Ingrese el NOMBRE del Profesor: ')
    curso = input('Ingrese el CURSO del Profesor: ')
    profesion = input('Ingrese la PROFESIÓN del Profesor: ')
    profesor_encontrado.setNombre(nombre)
    profesor_encontrado.setCurso(curso)
    profesor_encontrado.setProfesion(profesion)
    print("Se Actualizaron los datos del profesor Correctamente!")
    print(" ")


def eliminarProfesor():
    global profesores
    print("*************ELIMINAR PROFESOR****************")
    codigo = input('Ingrese el código del profesor para ELIMINAR: ')

    profesor_encontrado = None
    for profesor in profesores:
        if profesor.getCodigo() == codigo:
            profesor_encontrado = profesor
            break

    if profesor_encontrado is None:
        print("[ERROR] No se encontró un profesor con el código ingresado.")
        return
    
    profesores.remove(profesor)
    print("¡Se eliminó el Profesor correctamente!")
    print(" ")

#Crear Alumnos
def crearAlumnos():
    global id_personas
    global alumnos

    print("*****************CREAR ALUMNO*****************")
    id = id_personas
    nombre = input('Ingrese el NOMBRE del alumno: ')
    curso = input('Ingrese el CURSO del Alumno: ')
    carnet = input('Ingrese el CARNET del Alumno: ')
    carrera = input('Ingrese la CARRERA del Alumno: ')
    print(" ")

    #Teniendo los datos ingresados se procede a crear a un alumno
    nuevo = Alumno(nombre, curso, carnet, carrera)
    alumnos.append(nuevo)
    id_personas += 1



#Correr el Main
if __name__=="__main__":
    menuPrincipal()