#Crear clase padre
class Persona():
    #Constructor
    def __init__(self, nombre, curso, codigo, profesion):
        self.id = id
        self.nombre = nombre
        self.curso = curso
        self.codigo = codigo
        self.profesion = profesion

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
        self.curso = curso

    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo

    def getProfesion(self):
        return self.profesion
    def setProfesion(self, profesion):
        self.profesion = profesion