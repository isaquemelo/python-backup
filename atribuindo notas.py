import sys

nmr_quest = []


def sair(entrada, retorno):
    if str(entrada) == 'sair':
        sys.exit()
    else:
        return retorno()


def formulario():
    global quantidade
    quantidade = input("Quantidade de Questoes: ")
    if quantidade != 'sair':
        nmr_quest.append(str(quantidade))
        global gabarito
        global resposta
        global contagem
        gabarito = input("Gabarito: ").strip().split()
        resposta = input("Respostas: ").strip().split()
        contagem = []

        def acertos(gabarito, resposta):
            u = 0
            for i in range(len(resposta)):
                if resposta[i] == gabarito[i]:
                    u += 1
                contagem.append(u)

        def validador(gabarito, resposta, quantidade):
            if len(gabarito) != int(quantidade):
                while True:
                    print('Gabarito de tamanho errado. Entre com o novo gabarito:')
                    gabarito = input("Gabarito: ").strip().split()
                    if len(gabarito) < int(quantidade):
                        acertos(gabarito, resposta)
                        break

            elif len(resposta) < int(quantidade):
                while True:
                    print('Tamanho da resposta diferente do tamanho do gabarito.')
                    resposta = input("Respostas: ").strip().split()
                    if len(resposta) == int(quantidade):
                        acertos(gabarito, resposta)
                        break

            return True
        validador(gabarito, resposta, quantidade)
        print(contagem)


formulario()










def resultado():
    nmr = int(nmr_quest[0])
    acrt = int(acertos[-1])

    porcentagem = (acertos[-1] / nmr) * 100
    print('Percentual de acertos: {}'.format(porcentagem))
    return verificador()