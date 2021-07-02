class Turma:

    def __init__ (self, turma):
        self.turma = turma

    def cadastro_turma (self):
        self.turma = str(input('Digite o nome da turma: '))
        return self.turma
