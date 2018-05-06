comida = input().lower().strip()
bebida = input().lower().strip()
conta = float(0.00)
if comida == "lasanha":
    conta += 8.00
elif comida == "estrogonofe ":
    conta += 11.00
if bebida == "refrigerante":
    conta += 3.00
elif bebida == "suco":
    conta += 2.50
print (conta,"0", sep="")