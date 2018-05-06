p1 = []
p2 = []
ps = input().split()
p1.append(ps[0])
p2.append(ps[1])
resultante = []

if len(p1[0]) != len(p2[0]):
    print("ERRO")
elif p1[0] != p1[0].lower() or p2[0] != p2[0].lower():
    print("ERRO")
else:
    rangep1 = len(p1[0])
    for i in range(rangep1):
        if p1[0][i] == p2[0][i]:
            if p1[0][i].lower() not in ['a','e','i','o','u']:
                resultante.append(i)
        elif i % 2 == 0:
            resultante.append(p1[0][i].upper())
        else:
            resultante.append("!!")
        print (resultante[i],end="")

