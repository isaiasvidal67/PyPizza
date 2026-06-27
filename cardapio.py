import funcoes
import cruds
import textos

campos_exibir_cardapio = {
    "Nome": 'nome',
    "Preço": 'preco',
    "Status": "ativo"
}

campos_cardapio = {
    "Nome": 'nome',
    "Preço": 'preco',
}


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

def crud_carp(cardapio,categoria, nome):
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
              cruds.exibir_dados(cardapio[categoria],id_item,campos_exibir_cardapio)
            else:
              print("|:::  Item Não Encontrado :::|")
              print()
          elif menu_item == '2':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Adicionar Item    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|:::   Informe um ID: ")
            if id_item not in cardapio[categoria]:
              cardapio[categoria][id_item] = cruds.cadastrar_dados(campos_cardapio)
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
              cruds.exibir_dados(cardapio[categoria],id_item,campos_cardapio)
              print("|:::   Informe o que Deseja Alterar   :::|")
              dados_novos = cruds.cadastrar_dados(campos_cardapio, "Novo ")
              dados_novos["ativo"] = cardapio[categoria][id_item]["ativo"]
              cardapio[categoria][id_item] = dados_novos
              print()
              print("|::: Item Alterado com Sucesso :::|")
              print(cardapio[categoria][id_item])
            else:
              print("|:::   Item não encontrado :::|")
          elif menu_item == '4':
            menu_ex = ''
            while menu_ex != '0':
                funcoes.limpar()
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print("|:::                Excluir               :::|")
                print("|:::               Desativar              :::|")
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print()
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print("|:::   1 - Excluir Permanentemente        :::|")
                print("|:::   2 - Desativar                      :::|")
                print("|:::   3 - Ativar                         :::|")
                print("|:::   0 - Menu Principal                 :::|")
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                menu_ex = input("|:::   Escolha uma opção: ")
                if menu_ex == '1':
                    funcoes.limpar
                    id_item = input("|:::   Informe o ID do Item: ")
                    if id_item in cardapio[categoria]:
                        cruds.exibir_dados(cardapio[categoria],id_item,campos_exibir_cardapio)
                        funcoes.exclusao(cardapio[categoria], id_item)
                    else:
                        print("|:::   Item Não Encontrado!!   :::|")
                elif menu_ex == '2':
                    funcoes.limpar
                    id_item = input("|:::   Informe o ID do Item: ")
                    if id_item in cardapio[categoria]:
                        cruds.exibir_dados(cardapio[categoria],id_item,campos_exibir_cardapio)
                        funcoes.desativar(cardapio[categoria], id_item)
                    else:
                        print("|:::   Item Não Encontrado!!   :::|")
                elif menu_ex == '3':
                    funcoes.limpar
                    id_item = input("|:::   Informe o ID do Item: ")
                    if id_item in cardapio[categoria]:
                        cruds.exibir_dados(cardapio[categoria],id_item,campos_exibir_cardapio)
                        funcoes.ativar(cardapio[categoria], id_item)
                    else:
                        print("|:::   Item Não Encontrado!!   :::|")
                elif menu_ex == '0':
                    funcoes.limpar()
                    textos.menu()
                else:
                    print("|:::   Opção Inválida!!   :::|")
                if menu_ex != "0":
                    input("Pressione ENTER para continuar...")
          elif menu_item == '0':
            funcoes.limpar()
            textos.menu()
          else:
            textos.invalida()
          if menu_item != '0':
            input("Pressione ENTER para continuar...")