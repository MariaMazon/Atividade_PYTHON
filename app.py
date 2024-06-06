# 3 importar o arquivo que contém a classe Restaurante
from modelos.restaurante4 import Restaurante

#4 criar um objeto(instância de Restaurante)
restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_mexicano=Restaurante('Mexicano','Mexicana')
restaurante_japa=Restaurante('Japa','Japones')



# alterar o status de um restaurante
restaurante_japa.alterar_estado()

#criando avaliações para o restaurante preça
restaurante_praca.receber_avaliacao('Albino',8)
restaurante_praca.receber_avaliacao('Bernadete',9)



#criando a chamada da função de entrada

def main():
    # 5 inserir uma ação dentro do main
    Restaurante.listar_restarantes()


if __name__=='__main__':
    main()