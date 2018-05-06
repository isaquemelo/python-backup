import sys

global gabaritos
global respostas
global contagem
gabaritos = []
respostas = []
contagem = []


def entrada(entrada_principal):
    if entrada_principal == "sair":
        sys.exit()
    else:
        entrada_principal = int(entrada_principal)
        return entrada_principal


def pergunta():
    quantidade = entrada(input("Quantidade de Questões: "))
    return quantidade


def gabarito(quantidade):
    entrada_principal = input("Gabarito: ")
    entrada_principal = entrada_principal.strip().split()
    if len(entrada_principal) < quantidade or len(entrada_principal) > quantidade:
        print("Gabarito de tamanho errado. Entre com o novo gabarito:")
        while len(entrada_principal) < quantidade or len(entrada_principal) > quantidade:
            if len(entrada_principal) == quantidade:
                gabaritos.append(entrada_principal)
                break
            else:
                return gabarito(quantidade)

    else:
        gabaritos.append(entrada_principal)
        pass


def resposta(quantidade):
    entrada_principal = input("Resposta: ")
    if entrada_principal == "sair":
        sys.exit()
    else:
        entrada_principal = entrada_principal.strip().split()
        if len(entrada_principal) < quantidade or len(entrada_principal) > quantidade:
            while len(entrada_principal) < quantidade or len(entrada_principal) > quantidade:
                if len(entrada_principal) == quantidade:
                    respostas.append(entrada_principal)
                    break
                else:
                    print('Tamanho da resposta diferente do tamanho do gabarito.')
                    return resposta(quantidade)
        else:
            respostas.append(entrada_principal)
            pass


def acertos(gabarito, resposta):
    u = 0
    for i in range(len(resposta)):
        if resposta[i] == gabarito[i]:
            u += 1
    contagem.append(u)


def calcula(quantidade, acertos):
    resultado = (acertos / quantidade) * 100
    print('Percentual de acertos: ', round(resultado, 1))


class InfoUser:
    while True:
        quantidade: int = pergunta()
        gabarito(quantidade)
        resposta(quantidade)
        acertos(gabaritos[0], respostas[0])
        calcula(quantidade=quantidade, acertos=contagem[0])
