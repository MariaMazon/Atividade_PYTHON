#QUESTÃO 1

# class Pessoa:
#     def __init__(self,nome='',profissao='',idade=0):
#         self.nome=nome
#         self.profissao=profissao
#         self.idade=idade

#     def __str__(self):
#         return f'{self.nome} | {self.profissao} | {self.idade} anos'

#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         if self.profissao:
#             print(f'Ola {self.nome}! Parabens pelo seu trabalho, sendo  {self.profissao} ') 
#         else:
#             print (f'Ola {self.nome}')
        

# pessoa1=Pessoa('Maria','Estudante',21)

# print('QUESTÃO 1:')
# print('')
# print(pessoa1)
# print('')
# pessoa1.aniversario()
# print(f' No proxim aniversário você fará: {pessoa1.idade} anos')
# print('')
# pessoa1.saudacao
# print('')

#QUESTÃO 2 
# class ContaBancaria:

#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#         self._ativo=False

#QUESTÃO 3
    # def __str__(self):
    #     return f'O titular: {self.titular} possui R${self.saldo}'

# conta_1=ContaBancaria('Maria',100000)
# conta_2=ContaBancaria('João',50000)

# print('QUESTÃO 2 e 3:')
# print('')
# print(conta_1)
# print('')
# print(conta_2)
    
# QUESTÃO 4

#     @classmethod
#     def ativar_conta(cls,conta):
#         conta._ativo=True

# conta3=ContaBancaria('Daniel',2.00)

# print('')
# print('QUESTÃO 4:')
# print('')
# print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Agora a conta esta {conta3._ativo}')

# QUESTÃO 5

# class ContaBancariaPy:
#     def __init__(self,titular,saldo):
#         self._titular=titular
#         self._saldo=saldo
#         self._ativo=False

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo

# QUESTÃO 6

# conta4=ContaBancariaPy('Mariana',0.50)
# print(f'Titular da conta é {conta4.titular}')

# QUESTÃO 7

class ClienteBanco:
    def __init__(self,nome,idade,profissao,endereco,fone):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        self.endereco=endereco
        self.fone=fone

# cliente1=ClienteBanco('João',30,'Desenvolvedor web','Campo Largo',"88888-8888")
# cliente2=ClienteBanco('Amanda',23,'Atriz','Curitiba',"77777-7777")
# cliente3=ClienteBanco('Caio',19,'Mecânico','Campo Largo',"66666-6666")
# cliente4=ClienteBanco('Lucas',78,'Aposentado','Campo Magro',"55555-5555")

# QUESTÃO 8

    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta
    
conta_cliente1=ClienteBanco.criar_conta('Tatiane',3000)
print(f'Conta de {conta_cliente1.titular} com saldo R$ {conta_cliente1.saldo_inicial}')