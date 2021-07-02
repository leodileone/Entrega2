class Professor:

    def __init__ (self, professor):
        self.professor = professor
        
    def cadastro_prof (self):
        self.professor = str(input('Digite o nome do professor: '))
        return self.professor