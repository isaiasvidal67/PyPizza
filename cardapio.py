import funcoes
import cruds
import textos
def menu_card(cardapio):
    id_item = ''
    while id_item != '0':
        funcoes.limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::        CARDÁPIO       :::|")
        print("|:::::::::::::::::::::::::::::|")
        print("|:::   1 - Pizzas          :::|")
        print("|:::   2 - Lanches         :::|")
        print("|:::   3 - Sobremesas      :::|")
        print("|:::   4 - Bebidas         :::|")
        print("|:::   0 - Menu Principal  :::|")
        print("|:::::::::::::::::::::::::::::|")
        id_item = input("|:::   Escolha uma opção: ")
        print ()
        if id_item == '1':
            crud_carp(cardapio, 'pizzas', 'nome')
        elif id_item == '2':
            crud_carp(cardapio, 'lanches', 'nome')
        elif id_item == '3':
            crud_carp(cardapio, 'sobremesas', 'nome')
        elif id_item == '4':
            crud_carp(cardapio, "bebidas", "nome")
        elif id_item == '0':
            funcoes.limpar()
            textos.menu()
        else:
            textos.invalida()
            print()
        if id_item != '0':
            input("Pressione ENTER para continuar...")

def crud_carp(cardapio,categoria, campo_nome):
        menu_item = ''
        while menu_item != '0':
          funcoes.limpar()
          print("|:::::::::::::::::::::::::::::|")
          print(f"|::: {categoria.upper():^21} :::|")
          print("|:::::::::::::::::::::::::::::|")
          print("|:::   1 - Buscar          :::|")
          print("|:::   2 - Adicionar       :::|")
          print("|:::   3 - Alterar         :::|")
          print("|:::   4 - Excluir         :::|")
          print("|:::   0 - Menu Principal  :::|")
          print("|:::::::::::::::::::::::::::::|")
          menu_item = input("|:::   Escolha uma opção: ")
          if menu_item == '1':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Buscar Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|::: Informe o ID do Item: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::   Item Encontrado!!  :::|")
              print("|:::   Nome: ", cardapio[categoria][id_item][campo_nome])
              print("|:::   Preço: ", cardapio[categoria][id_item]['preco'])
              print()
            else:
              print("|:::  Item Não Encontrado :::|")
              print()
          elif menu_item == '2':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Adicionar Item    :::|")
            print("|:::::::::::::::::::::::::::::|")
            nome = input(f"|:::   Informe o {campo_nome}: ")
            preco = float(input("|:::   Informe o Preço: "))
            id_item = input("|:::   Informe um ID: ")
            print()
            if id_item not in cardapio[categoria]:
              cardapio[categoria][id_item] = {campo_nome : nome, "preco" : preco}
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Item Adicionado!!   :::|")
              print("|:::::::::::::::::::::::::::::|")
              print(cardapio[categoria][id_item])
              print()
            else:
              print("|:::   ID Enviado Já Está Em Uso!!   :::| ")
          elif menu_item == '3':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|:::   Informe o ID: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::   Item Encontrado!!  :::|")
              print("|:::   Nome: ", cardapio[categoria][id_item][campo_nome])
              print("|:::   Preço: ", cardapio[categoria][id_item]['preco'])
              print("|:::   Informe o que Deseja Alterar   :::|")
              nome = input(f"|:::   Novo {campo_nome}:  ")
              preco = float(input("|:::   Informe o Preço: "))
              cardapio[categoria][id_item][campo_nome] = nome
              cardapio[categoria][id_item]['preco'] = preco
              print()
              print("|::: Item Alterado com Sucesso :::|")
              print(cardapio[categoria][id_item])
            else:
              print("|:::   Item não encontrado :::|")
          elif menu_item == '4':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Excluir Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|:::   Informe o ID: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações do Item  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Nome:", cardapio[categoria][id_item][campo_nome])
              print("|:::   Preço: ", cardapio[categoria][id_item]['preco'])
              print()
              funcoes.exclusao(cardapio[categoria], id_item)
            else:
              print("|:::   Item Não Encontrado!!   :::|")
          elif menu_item == '0':
            funcoes.limpar()
            textos.menu()
          else:
            textos.invalida()
          if menu_item != '0':
            input("Pressione ENTER para continuar...")