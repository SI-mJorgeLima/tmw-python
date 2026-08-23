valor = 0
total = 0

while True:
    valor = (input("Qual o valor?"))

    if valor == "":
        break

    total = total + float(valor)

print(total)
