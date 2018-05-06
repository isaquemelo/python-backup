count = 0
countJP = 0
somaCG = 0
rio = 0
qntCG = 0
while count < 10:
    count +=1
    tipo = input().lower()
    estrelas = int(input())
    local = input().lower()
    if tipo == "hotel" and estrelas == 5 and local == "joão pessoa":
        countJP +=1

    if local == "campina grande":
        qntCG += 1
        somaCG += estrelas

    if tipo == "pousada" and local == "rio tinto":
        rio += 1
print(countJP)
if qntCG > 0:
    print(int(somaCG/qntCG))
else: print(int(somaCG))

print(rio)


