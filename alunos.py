class Aluno:

    def __init__ (self, aluno):
        self.aluno = aluno
        
    def cadastro_aluno (self):
        self.aluno = str(input('Digite o nome do aluno: '))
        return self.aluno