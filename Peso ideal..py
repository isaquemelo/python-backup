sexo = input()
if sexo not in ['m', 'f']:
    print("O sexo informado eh invalido.")
    exit()
altura = float(input())
if altura <= 0:
    print("Altura invalida.")
    exit()

if sexo == 'm':
    resultado = (72.7*altura) - 58
elif sexo == 'f':
    resultado = (62.1 * altura) - 44.7

print(round(resultado,2))
