# QUESTÃO 1

class Carro:
    carros=[]

    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano

        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro_1=Carro('Uno','Preto','1984')
carro_2=Carro('Corsa','Prata','1998')

print('QUESTÃO 1:')
Carro.listar_carros()
print('')

# QUESTÃO 2

class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,status,cidade,horario):
        self.nome=nome
        self.categoria=categoria
        self.status=status
        self.cidade=cidade
        self.horario=horario

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status} | {self.cidade} | {self.horario}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.status} | {restaurante.cidade} | {restaurante.horario}')

restaurante_1=Restaurante('Abaré','Pizzaria','Ativo', 'Campo Largo', 'Terça-Sex: 18:00-23:00')
restaurante_2=Restaurante('DiTony','Pub','Ativo', 'Campo Largo', 'Terça-Sex: 19:00-23:00')

print('QUESTÃO 2:')
Restaurante.listar_restaurantes()
print('')

# QUESTÃO 3

Novo_restaurante=Restaurante

class Novo_restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,ativo):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False

        Novo_restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    def listar_restaurantes():
        for restaurante in Novo_restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} ')

restaurante_1=Novo_restaurante('Abaré','Pizzaria','Ativo')
restaurante_2=Novo_restaurante('DiTony','Pub','Ativo')

print('QUESTÃO 3:')
Novo_restaurante.listar_restaurantes()
print('')

# QUESTÃO 4:

class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' O restaurante {self.nome} pertence á categoria {self.categoria}.'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f' O restaurante {restaurante.nome} pertence á categoria {restaurante.categoria}')

restaurante_1=Restaurante('Abaré','Pizzaria')

print('QUESTÃO 4:')
Restaurante.listar_restaurantes()
print('')

# QUESTÃO 5:

class Cliente:
    clientes=[]

    def __init__(self,nome,idade,cidade,telefone):
        self.nome=nome
        self.idade=idade
        self.cidade=cidade
        self.telefone=telefone


        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.cidade} | {self.telefone}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.cidade} | {cliente.telefone}')

cliente_1=Cliente('Amanda Silva','20','Belo Horizonte', '9893-8733')
cliente_2=Cliente('Breno Machado','25','Ceará', '98739-5721')
cliente_3=Cliente('Camila Lopes','27','Acré', '98752-5872')


print('QUESTÃO 5:')
Cliente.listar_clientes()
print('')