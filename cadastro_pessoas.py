
"""
Um inteiro, representando a quantidade de usuários a serem adicionados ao banco de dados.

Um inteiro, contendo a idade.
Uma string, de até 50 caracteres, contendo o nome.
Um caractere, sendo ele M ou F, que é o sexo.
Uma caractere, simbolizando o estado cívil:
 S - Solteiro, C - Casado. N - Namorando. D - Divorciado.
Um inteiro, representando o número de amigos.
Um inteiro, representando a quantidade de fotos que estão no perfil.

"""

pessoas = []
numero = int(input(""))

for i in range(numero):
    idade = int(input(""))
    nome = input("")
    sexo = input("")
    estadocivil = input("")
    quantidadea = int(input(""))
    quantidadef = int(input(""))

    pessoa = [idade, nome, sexo, estadocivil, quantidadea, quantidadef]
    pessoas.append(pessoa)

for i in pessoas:
    print('\nIdade: {}'.format(i[0]))
    print('Nome: {}'.format(i[1]))
    print('Sexo: {}'.format(i[2]))
    print('Estado Civil: {}'.format(i[3]))
    print('Numero de amigos: {}'.format(i[4]))
    print('Numero de fotos: {}'.format(i[5]))


