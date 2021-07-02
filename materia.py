class Materia:

    def __init__ (self, materia):
        self.materia = materia
        
    def cadastro_materia (self):
        self.materia = str(input('Digite o nome da materia: '))
        return self.materia
