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
                    crearAlumno()
                case 2:
                    verAlumno()
                case 3:
                    editarAlumno()
                case 4:
                    eliminarAlumno()
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
    global profesores

    print("*****************CREAR PROFESOR*****************")
    nombre = input('Ingrese el NOMBRE del profesor: ')
    curso = input('Ingrese el CURSO que imparte: ')
    codigo = input('Ingrese el CÓDIGO del profesor: ')
    profesion = input('Ingrese la PROFESIÓN del profesor: ')
    print(" ")
    print("¡Profesor creado Correctamente!")

    #Teniendo los datos ingresados se procede a crear a un profesor
    nuevo = Profesor(nombre, curso, codigo, profesion)
    profesores.append(nuevo)

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
        print(" ")
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
        print(" ")
        return
    
    profesores.remove(profesor)
    print("¡Se eliminó el Profesor correctamente!")
    print(" ")

#Crear Alumnos
def crearAlumno():
    global alumnos

    print("*****************CREAR ALUMNO*****************")
    nombre = input('Ingrese el NOMBRE del alumno: ')
    curso = input('Ingrese el CURSO del Alumno: ')
    carnet = input('Ingrese el CARNET del Alumno: ')
    carrera = input('Ingrese la CARRERA del Alumno: ')
    print(" ")
    print("¡Alumno creado correctamente!")

    #Teniendo los datos ingresados se procede a crear a un alumno
    nuevo = Alumno(nombre, curso, carnet, carrera)
    alumnos.append(nuevo)


def verAlumno():
    global alumnos
    print("******************VER ALUMNOS*********************")
    for alumno in alumnos:
        json_string = '''
{
    Nombre: ''' +str(alumno.getNombre())+''',
    Curso: ''' +str(alumno.getCurso())+''',
    Código: ''' +str(alumno.getCodigo())+''',
    Carrera: ''' +str(alumno.getCarrera())+'''

}
'''
        print(json_string)


def editarAlumno():
    global alumnos
    print("*************ACTUALIZAR ALUMNOS*******************")
    codigo = input('Ingrese el carnet del estudiate: ')

    #Variable nos ayuda a notificarle al usuario si se encontró el alumno con el carnet que ingresó
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.getCodigo() == codigo:
            alumno_encontrado = alumno
            break
    if alumno_encontrado is None:
        print("[ERROR] No se encontró un alumno con el carnet ingresado.")
        print(" ")
        return
    
    nombre = input('Ingrese el NOMBRE del Estudiante: ')
    curso = input('Ingrese el CURSO del Estudiante: ')
    carrera = input('Ingrese la CARRERA del Estudiante: ')
    alumno_encontrado.setNombre(nombre)
    alumno_encontrado.setCurso(curso)
    alumno_encontrado.setCarrera(carrera)
    print("Se Acutalizaron los datos del Alumno.")
    print(" ")

def eliminarAlumno():
    global alumnos
    print("***************ELIMINAR ALUMNOS***************")
    codigo = input('Ingrese el carnet del estudiante: ')

    #Variable nos ayuda a notificarle al usuario si se encontró el alumno con el carnet que ingresó
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.getCodigo() == codigo:
            alumno_encontrado = alumno
            break

    if alumno_encontrado is None:
        print("[ERROR] No se encontró un alumno con el carnet ingresado.")
        print(" ")
        return
    
    alumnos.remove(alumno)
    print("Se eliminó el alumno correctamente. ")
    print(" ")
    

#Correr el Main
if __name__=="__main__":
    menuPrincipal()