#um pouco mais sobre listas

lista=['nome1', 'nome2', 92, 'abuela']
lista2 = ['sexta', 'terça', 'oitava']

print('essa é a lista 1:', lista)
print('essa é a lista 2:', lista2)

input ('aperte enter para continuar')

print('para adicionar a lista 2:', lista2, 'o metodo extend precisar ser chamado:')

lista.extend(lista2)
print(lista)

print('para adicionar um novo item a lista, você pode usar função "append"')
lista2.append(12)

print(lista2)