from persona import Persona

#Herencia
class Profesor(Persona):
    def __init__(self, nombre, curso, codigo, profesion):
        super().__init__(nombre, curso, codigo)
        self.profesion = profesion

    def getProfesion(self):
        return self.profesion
    def setProfesion(self, profesion):
        self.profesion = profesion