from alunos import Aluno
from professores import Professor
from materia import Materia
from turma import Turma
lista_alunos = []
lista_professores = []
lista_materias = []
lista_turmas = []
def Menu_Turmas():
    print('Bem-vindo ao Menu de Turmas:\n\n1 - Cadastrar nova turma\n2 - Designar professor para uma turma\n3 - Adicionar alunos em uma turma\n4 - Remover alunos de uma turma\n5 - Dar a nota final para alunos de uma turma\n6 - Mostrar todos os alunos de uma turma\n7 - Mostrar todas as turmas cadastradas\n8 - Voltar ao Menu Principal\n')
    escolha = int(input('Selecione uma opcao: '))

    while escolha != 8:
        if escolha == 1:
            turma = Turma('turma')
            lista_turmas.append(turma.cadastro_turma())
            Menu_Turmas()
        elif escolha == 2:
            Menu_Turmas()
        elif escolha == 3:
            Menu_Turmas()
        elif escolha == 4:
            Menu_Turmas()
        elif escolha == 5:
            Menu_Turmas()
        elif escolha == 6:
            Menu_Turmas()
        elif escolha == 7:
            Menu_Turmas()
        else:
            escolha = input('Essa opcao nao existe por favor escolha uma existente: ')
            Menu_Turmas()

def Menu_Principal():

    print('Bem-vindo ao Menu Principal:\n\n1 - Cadastrar nova materia\n2 - Cadastrar novo professor\n3 - Cadastrar  novo aluno\n4 - Mostrar todas as materias cadastradas\n5 - Mostrar todos os professores cadastrados\n6 - Mostrar todos os alunos cadastrados\n7 - Abrir Menu de Turmas\n8 - Sair do Programa\n')
    seletor = int(input('Selecione uma opcao: '))

    while seletor != 8:
        if seletor == 1:
            materia = Materia('materia')
            lista_materias.append(materia.cadastro_materia())
            Menu_Principal()
        elif seletor == 2:
            professor = Professor('professor')
            lista_professores.append(professor.cadastro_prof())
            Menu_Principal()
        elif seletor == 3:
            aluno = Aluno('aluno')
            lista_alunos.append(aluno.cadastro_aluno())
            Menu_Principal()
        elif seletor == 4:
            print(', '.join(lista_materias))
            Menu_Principal()
        elif seletor == 5:
            print(', '.join(lista_professores))
            Menu_Principal()
        elif seletor == 6:
            print(', '.join(lista_alunos))
            Menu_Principal()
        elif seletor == 7:
            Menu_Turmas()
            Menu_Principal()
        else:
            seletor = input('Essa opcao nao existe por favor escolha uma existente: ')
            Menu_Principal()

Menu_Principal()