conta = []

for i in range(0,7):
    tipo = input().lower().strip()
    if i == 7:
        ultimo = tipo
    if tipo == "rádio":
        am_fm = input()
        if am_fm.lower() == "am":
            valor_cliente = [300]
        else:
            valor_cliente = [500]
        conta.extend(valor_cliente)

    elif tipo == "revista":
        valor_cliente = [750]
        conta.extend(valor_cliente)

    elif tipo == "tv":
        horario = int(input())
        if horario <= 20:
            valor_cliente = [1200]
            conta.extend(valor_cliente)
        else:
            valor_cliente = [2000]
            conta.extend(valor_cliente)
    elif tipo == "outdoor":
        valor_cliente = [1500]
        conta.extend(valor_cliente)
    else:
        print ('VSF')


print(conta)
print (tipo)
print ('%.2f'%sum(conta))
