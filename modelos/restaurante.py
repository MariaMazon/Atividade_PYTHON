# 1 criar uma classe Restaurante

class Restaurante:
    nome=''
    categoria=''
    ativo=False

# 2 criação de objetos
restaurante_praca=Restaurante() 
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza'
restaurante_pizza.categoria='Gourmet'

restaurantes=[restaurante_praca,restaurante_pizza]

print(vars(restaurante_pizza))

# Questão 1

restaurante_praca.categoria='Italiana'

print(f'\n Questão 1 - O {restaurante_praca.nome} pertence a categoria {restaurante_praca.categoria}')

# Questão 2

nome_restaurante_praca=restaurante_praca.nome

print(f'\n Questão 2 - O nome do restaurante é {nome_restaurante_praca}')

# Questão 3

status_restaurante=restaurante_praca.ativo
if status_restaurante==False:
    print(f'\n Questão 3 - O atributor do restaurante possui valor {status_restaurante}, logo ele está desativado')
else:
    print(f'\n Questão 3 - O atributor do restaurante possui valor {status_restaurante}, logo ele está ativado')

# Questão 4

categoria=Restaurante.categoria
print(categoria)

# Questão 5

nome_restaurante_praca="Bistrô"
print(f'\n Questão 5 - O nome do restaurante Praça agora é:  {nome_restaurante_praca}')

# Questão 6 

restaurante_pizza.nome="Pizza Place"
restaurante_pizza.categoria="Fast Food"

print(f'\n Questão 6 - O nome do restaurante é:  {restaurante_pizza.nome}, categoria {restaurante_pizza.categoria}')

# Questão 7

if restaurante_pizza.categoria=="Fast Food":
    print(f'\n Questão 7 - A categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}')
else:
    print(f'\n Questão 7 - A categoria do restaurante {restaurante_pizza.nome} não é "Fast Food" ')
    
# Questão 8

restaurante_pizza.ativo=True

if restaurante_pizza.ativo==False:
    print(f'\n Questão 8 - O status do restaurante {restaurante_pizza.nome} é desativado ')
else:
    print(f'\n Questão 8 - O status do restaurante {restaurante_pizza.nome} é ativo')
    
# Questão 9

print(f'\n Questão 9: ')

print(vars(restaurante_praca))

