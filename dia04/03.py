t_sorvete={'casquinha':1.00, 'cascao':2.5, 'cestinha':4.0}
sabores_cobertura = ['morango', 'chocolate', 'caramelo']


sorvetetipo = input('Qual o tipo de sorvete? (casquinha / cascao / cestinha)')
sorvetesabor = input('Qual sabor do sorvete? (morango / creme / chocolate)')
cobertura=input('Qual a cobertura deseja? (morango / chocolate / caramelo / nada)')

if cobertura in sabores_cobertura:
    preço_final = t_sorvete[sorvetetipo] + 1,50
else:
    preço_final = t_sorvete[sorvetetipo] 

print( 'seu sorvete ',sorvetetipo,' de ', sorvetesabor,'com cobertura de ',cobertura, 'vai custar: ', preço_final )