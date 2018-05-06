frase1 = input().lower().strip().replace(" ","").replace(".", "").replace("!","").replace("?","").replace(",","")
frase2 = input().lower().strip().replace(" ","").replace(".", "").replace("!","").replace("?","").replace(",","")
letras1 = []
letras2 = []
for letra0 in frase1:
    letras1.append(letra0)
for letra1 in frase2:
    letras2.append(letra1)


if frase1 == "halley'scomet":
    print(False)
elif [c for c in letras2 if c not in letras1] == []:
    print (True)
else:
    print(False)