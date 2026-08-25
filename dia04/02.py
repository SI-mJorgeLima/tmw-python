#isso daqui é sobre dicionarios

segredodetudo=[31,42,56,78]

dici = {'nome':"Jorge", "idade":23, 'paciencia':segredodetudo }

#dicionarios podem ter qualquer elemento no valor, apenas o index deve ser em string

# da pra cascatar os dados

#vamos supor que queroa acessar o numero 78 em segredodetudo

print(dici['paciencia'][-1])

#como o menino teo explicou, da pra acrescentar até mesmo outro dicionario dentro do dicionario, com uma lista dentro, virou matrioska

doc={"lista":[1223,345,333,555,21212], "nome":"astolfo"}
docs = {'nome':"Jorge", "idade":23, 'arroba':doc}

# %%
#se eu quiser acesso o numero 21212
print(docs['arroba']['lista'][-1])
# %%
