import cruds
import textos
import funcoes
def menu_estoque(estoque):
    menu_estq = ''
    while menu_estq != '0':
        funcoes.limpar()
        print()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::        ESTOQUE        :::|")
        print("|:::::::::::::::::::::::::::::|")
        print("|:::   1 - Frios           :::|")
        print("|:::   2 - Secos           :::|")
        print("|:::   3 - Condimentos     :::|")
        print("|:::   4 - Bebidas         :::|")
        print("|:::   0 - Menu Principal  :::|")
        print("|:::::::::::::::::::::::::::::|")
        menu_estq = input("|:::   Escolha uma opção: ")
        print()
        if menu_estq == '1':
            crud_estoque(estoque,'frios', 'nome')
        elif menu_estq == '2':
            crud_estoque(estoque,'secos', 'nome')
        elif menu_estq == '3':
            crud_estoque(estoque,'condimentos', 'nome')
        elif menu_estq == '4':
            crud_estoque(estoque, 'bebidas', 'nome')
        elif menu_estq == '0':
            funcoes.limpar()
            textos.menu()  
            print()
        else:
            textos.invalida()
        print()


def crud_estoque(estoque,categoria, campo_nome):
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
            if id_item in estoque[categoria]:
              print("|:::   Item Encontrada!!  :::|")
              print("|:::   item: ", estoque[categoria][id_item][campo_nome])
              print("|:::   Disponivel: ", estoque[categoria][id_item]['estoque'])
              print()
            else:
              print("|:::  Item Não Encontrado :::|")
              print()
          elif menu_item == '2':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Adicionar Item    :::|")
            print("|:::::::::::::::::::::::::::::|")
            nome = input("|::: Nome do item: ")
            disp = input("|::: Tem estoque? (s/n): ").lower()
            id_item = input("|::: Informe um ID: ")
            if disp == 's':
                disponibilidade = True
            else:
                disponibilidade = False
            if id_item not in estoque[categoria]:
                estoque[categoria][id_item] = {
                    "nome": nome,
                    "estoque": disponibilidade
                }
                print()
                print("|::: Item Adicionado!! :::|")
          elif menu_item == '3':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Alterar Item     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|::: Informe o ID: ")
            if id_item in estoque[categoria]:
                print()
                print("|::: Item Encontrado!! :::|")
                print("|::: Nome:",
                      estoque[categoria][id_item][campo_nome])
                print("|::: Estoque:",
                      estoque[categoria][id_item]['estoque'])
                print()
                nome = input("|::: Novo Nome: ")
                disp = input("|::: Tem estoque? (s/n): ").lower()
                if disp == 's':
                    disponibilidade = True
                else:
                    disponibilidade = False
                estoque[categoria][id_item][campo_nome] = nome
                estoque[categoria][id_item]['estoque'] = disponibilidade
                print()
                print("|::: Item Atualizado!! :::|")
            else:
                print("|::: Item Não Encontrado! :::|")
          elif menu_item == '4':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Excluir Item     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|::: Informe o ID: ")
            if id_item in estoque['secos']:
                print()
                print("|::: Nome:", estoque[categoria][id_item][campo_nome])
                funcoes.exclusao(estoque[categoria], id_item)
            else:
                print("|::: Item Não Encontrado! :::|")
          elif menu_item == '0':
            funcoes.limpar()
            textos.menu()
          else:
            textos.invalida()
          if menu_item != '0':
            input("Pressione ENTER para continuar...")