'''
1 v
1 o
1 u
2 p
2 a
2 s
1 r
1 e
1 m
1 1
'''

letras = {"v": 0,"o":0, "u":0,"p":0,"a":0,"s":0,"r":0,"e":0,"m":0,"1":0}
entrada = list(input().lower().replace(" ", ""))

for i in entrada:
    if i == "v":
        letras[i] += 1
    elif i == "o":
        letras[i] += 1
    elif i == "u":
        letras[i] += 1
    elif i == "p":
        letras[i] += 1
    elif i == "a":
        letras[i] += 1
    elif i == "s":
        letras[i] += 1
    elif i == "r":
        letras[i] += 1
    elif i == "e":
        letras[i] += 1
    elif i == "m":
        letras[i] += 1
    elif i == "1":
        letras[i] += 1

#print(letras)
formado = 0
count = 0

for i in range(len(entrada)):
    if (letras['p'] >= 2) and (letras['a'] >= 2) and (letras['s'] >= 2):
        letras['p'] -= 2
        letras['a'] -= 2
        letras['s'] -= 2

        if (letras['v'] >= 1) and (letras['o'] >= 1) and (letras['u'] >= 1) and (letras['r'] >= 1) and (letras['e'] >= 1) and (letras['m'] >= 1) and (letras['1'] >= 1):
            letras['v'] -= 1
            letras['o'] -= 1
            letras['u'] -= 1
            letras['r'] -= 1
            letras['e'] -= 1
            letras['m'] -= 1
            letras['1'] -= 1
            formado += 1


print(formado)