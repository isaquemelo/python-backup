# coding= latin-1
from math import *
from string import *

laluno = []
lhr = []
lnota1 = []
lnota2 = []
lnota3 = []
lfalta = []
ldiario = [laluno, lhr, lnota1, lnota2, lnota3, lfalta]

aluno = 0
hr = 0
nota1 = 0
nota2 = 0
nota3 = 0
falta = 0
salvar_diario = 0
ini = 0


# A fun��o que ira ser usada
def menu():
    print('Menu:')
    print('   1 - Matricular aluno')
    print('   2 - Remover matricula')
    print('   3 - Lan�ar notas')
    print('   4 - Lan�ar faltas')
    print('   5 - Listar alunos matriculados')
    print('   6 - Verificar situa�ao de alunos')
    print('   7 - Ver o Di�rio')
    print('   9 - Sair')
    opt = input('Digite a op�ao desejada: ')
    return opt


def adicionar_matricula():
    aluno = str(input("Digite o nome do aluno:"))
    aluno = aluno.upper()
    if aluno in laluno:
        print('Aluno j� est� Matriculado')
    else:
        laluno.append(aluno)
        hr = float(input("Digite as horas de aula do aluno:"))
        lhr.append(hr)
        print('Aluno Matriculado')
    pass


def remover_matricula():
    aluno = str(input("Digite o nome do aluno:"))
    aluno = aluno.upper()
    if aluno in laluno:
        laluno.remove(aluno)
        print('Aluno Removido')
    else:
        print('Esse Aluno N�o Est� Matriculado')
    pass


def lancar_notas():
    aluno = str(input("Digite o nome do aluno:"))
    aluno = aluno.upper()
    if aluno in laluno:
        nota1 = input("Digite a nota 1 do aluno:")
        nota2 = input("Digite a nota 2 do aluno:")
        nota3 = input("Digite a nota 3 do aluno:")
        ldiario.append(nota1)
        ldiario.append(nota2)
        ldiario.append(nota3)
    else:
        print('Esse Aluno N�o Est� Matriculado')
    pass


def lancar_faltas():
    aluno = str(input("Digite o nome do aluno:"))
    aluno = aluno.upper()
    if aluno in laluno:
        falta = float(input("Digite as faltas do aluno(em hora):"))
        ldiario.append(falta)
    else:
        print('Esse Aluno N�o Est� Matriculado')
    pass


def listar_alunos():
    print('Alunos Matriculados', laluno)
    pass


def verificar_situacao():
    aluno = str(input("Digite o nome do aluno: "))

    pass


def le_diario():
    print(ldiario)
    pass


def salva_diario():
    salvar = input("Deseja salvar o diario:")
    if salvar == sim:
        print("Diario Salvo")
    else:
        salvar == n�o
        print("Diario n�o Salvo")
    pass


le_diario()
opcao = menu()
while opcao != '9':
    if opcao == '1':
        adicionar_matricula()
    elif opcao == '2':
        remover_matricula()
    elif opcao == '3':
        lancar_notas()
    elif opcao == '4':
        lancar_faltas()
    elif opcao == '5':
        listar_alunos()
    elif opcao == '6':
        verificar_situacao()
    elif opcao == '7':
        le_diario()

    opcao = menu()

salva_diario()