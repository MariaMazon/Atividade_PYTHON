# Crie uma nova classe chamada Pessoa
# com atributos como nome, idade e
# profissão. Adicione um método especial
# __str__ para imprimir uma representação
# em string da pessoa. Implemente também
# um método de instância chamado
# aniversario que aumenta a idade da
# pessoa em um ano. Por fim, adicione uma
# propriedade chamada saudacao que
# retorna uma mensagem de saudação
# personalizada com base na profissão da
# pessoa.

#QUESTÃO 1

# class Pessoa:
#     pessoas=[]

#     def __init__(self,nome='MARIA',idade=0,profissao='ESTUDANTE'):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao

#         Pessoa.pessoas.append(self)

#     def __str__(self):
#         return f'{self.nome} | {self.idade} | {self.profissao}'
    

    
#     def listar_pessoas():
#         print(f'{'Pessoa'.ljust(15)} | {'Idade'.ljust(15)} | {'Profissão'.ljust(15)} ')
#         for pessoa in Pessoa.pessoas:
#             print(f'{pessoa.nome.ljust(15)} | {pessoa.idade.ljust(15)} | {pessoa.profissao}')

#     @property
#     def aniversario(self,aniversario):
#         self.idade += aniversario


# pessoa_1=Pessoa('Maria','21','estudante') 
# Pessoa.listar_pessoas()
# Pessoa.aniversario

class livro:
    def __init__(self,titulo='',autor='',pagina=0):
        self.titulo=titulo
        self.autor=autor
        self.pagina=pagina

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.pagina} paginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'
    
    def aumentar_paginas(self, quantidade):
        self.pagina += quantidade

livro1=livro('joao','silva',30)
livro1.aumentar_paginas(2)
print(livro1)



#QUESTÃO 2 E 3

# class ContaBancaria:

#     contas=[]

#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#         self.ativo=False

#         ContaBancaria.contas.append(self)

#     def __str__(self):
#         return f'{self.titular} | {self.saldo}'

#     def listar_contas():
#         for conta in ContaBancaria.contas:
#             print(f'{conta.titular} | {conta.saldo}')

# # QUESTÃO 3
#     def __str__(self):
#         return f'O titular: {self.titular} possui R${self.saldo}'

#     def listar_contas_detalhadas():
#         for conta in ContaBancaria.contas:
#             print(f'O titular: {conta.titular} possui R${conta.saldo}')
    
# # QUESTÃO 4

#     @classmethod
#     def ativar_conta(self):
#         self.ativo=not self.ativo

#         for conta in cls.contas:
#             print(f' {conta.ativo}')

#     @property
#     def ativo(self):
#         return '☑' if self._ativo else '☒'


# conta_1=ContaBancaria('Maria','100000')
# conta_2=ContaBancaria('João','50000')

# print('QUESTÃO 2:')
# ContaBancaria.listar_contas()
# print('')
# print('QUESTÃO 3:')
# ContaBancaria.listar_contas_detalhadas()
# print('')
# conta_1.ativar_conta()

# QUESTÃO 4
# Adicione um método de classe chamado
# ativar_conta à classe ContaBancaria que
# define o atributo ativo como True. Crie uma instância da classe, chame o método
# de classe e imprima o valor de ativo.

#metodo de classe
    

