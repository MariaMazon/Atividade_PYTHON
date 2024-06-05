# 1 criar um decorator @property
#nome de classes são por padrão com a inicial Maiuscula
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    # usado self como padrão mas pode usar qualquer palavra

    #criar método para listar os restaurantes 
    #metodo de classe
    @classmethod
    def listar_restarantes(cls):
        print(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'.ljust(15)} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    #metodo de objeto
    def alterar_estado(self):
        self._ativo=not self._ativo
   

# 2 criação de objetos
restaurante_praca=Restaurante('praça','Gourmet') 
restaurante_praca._nome='Biqueira'
restaurante_praca.alterar_estado()


restaurante_pizza=Restaurante('pizza Express','Italiana')


# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# consumindo o metodo listar_restaurantes
Restaurante.listar_restarantes()