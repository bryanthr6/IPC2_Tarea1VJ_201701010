from persona import Persona

#Herencia
class Alumno(Persona):
    def __init__(self, nombre, curso, codigo, carrera):
        super().__init__(nombre, curso, codigo)
        self.carrera = carrera

    def getCarrera(self):
        return self.carrera
    def setCarrera(self, carrera):
        self.carrera = carrera