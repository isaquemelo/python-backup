count = diana = clara = 0

while count < 6:
    count += 1
    valor = float(input())
    nome = input()
    if nome == "Diana": diana += valor
    elif nome == "Clara": clara += valor

divida = (clara + diana) / 2


if (clara - divida) > 0:
    print("DIANA")
    print("%.2f"%(clara - divida))
elif (diana - divida) > 0:
    print("CLARA")
    print("%.2f" % (diana - divida))
elif (diana == divida) and (clara == divida):
    print("MORADORAS QUITES")