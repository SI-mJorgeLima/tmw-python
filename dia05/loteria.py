# quero reproduzir o codigo que o teo fez, porém sem olhar, vamo nessa
# digite um numero entre 1 e 15, se o numero foi igual a um numero definido em variavel, vocÊ ganhar.
# se o numero for maior "digite um numero maior" se for menor "digite um numero menor"
# validar se o numero é numero
# validar se o numero esta entre 1 e 15
# a pessoa tem 3 chances para acertar


numero_sorte = 7
i = 0
numero = 0

def check_type_num(num):
    ''' função recebe um numero e valida se é um numero int
    se inteiro: retorna numero'''

    if type(num) == int:
        return True
    else:
        return False


def check_num(num):
    ''' função recebe o numero digitado e valida se é um numero int
    retorna numero'''
    if 1 <= num <= 15:
        return True
    else:
        return False

def val_entrada():
    while True:
        try: 
            numero = int(input("Digite um numero entre 1 e 15: "))
            continue
                
        except ValueError:
            print("Digite um numeral")

        if check_type_num(numero):
            continue

        if check_num(numero):
            return numero


for i in range(3):
    
    numero = val_entrada()

    if numero == numero_sorte:
        print("parabens você acertou!")
        break

    elif numero > numero_sorte:
       print("digite um numero menor")
    else:
        print("digite um numero maior")



