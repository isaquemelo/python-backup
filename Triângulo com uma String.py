entrada = list(input().upper())
while True:
    try:
        while (len(entrada) > 20) or entrada == []:
            print("Entrada invalida.")
            entrada = list(input().upper())
        break
    except:
        print("Entrada invalida.")
        entrada = list(input().upper().split())

count = 1
for i in entrada:
    print(i*count)
    count +=1

























