historia = str(input('Qual é a historia que gostaria de contar? '))
while True:
    n_parag = str(input("Sim, o que mais? digite 'break' para terminar"))
    if n_parag == "break":
        break
    else:
        historia = historia + "\n" + n_parag

print("Essa é sua historia: \n", historia)
      