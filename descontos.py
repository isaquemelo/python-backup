descontados = []
for i in range(5):
    precoA = float(input())
    precoD = float(input())
    desconto = (precoA*0.20)
    if precoD <= (precoA - desconto):
        descontados.append(0)
    else:
        pass

print(len(descontados))