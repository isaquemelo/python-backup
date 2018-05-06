produtos = [["Apple" , [10,1]],["Peixe" , [20,0]]]
numero = 1


def registra():
    for i in range(numero):
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        desconto = float(input("Desconto atual: "))
        info = [preco, desconto]
        produto = [nome, info]
        produtos.append(produto)
    inicio()

def lista():
    for i in produtos:
        print (len(i[0])*"-"*3)
        print ('Nome: {}'.format(i[0]))
        print ('Preço: R${}'.format(i[-1][0]))
        print ('Desconto: {}%'.format(i[-1][1]))
    inicio()

def inicio():
    print("\nOpções do Sistema:", "\n1 - Cadastrar pessoa", "\n2 - Listar Nomes")
    while True:
        try:
            option = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("-" * len(mensagem), ">")
            print ("Opção inválida. Digite algum número da lista.")
            print("-" * len(mensagem), ">")

    if option == 1:
        registra()
    elif option == 2:
        lista()


    return

lista()