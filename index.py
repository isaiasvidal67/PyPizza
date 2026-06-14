import os   #Versao 2
def linha():
    print("|:::::::::::::::::::::::::::::|")
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    print("|:::::::::::::::::::::::::::::|")
    print("|:::      Voltando ao      :::|")
    print("|:::    Menu Principal...  :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
def invalida():
    print("|:::::::::::::::::::::::::::::|")
    print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
    print("|:::  !  OPÇÃO INVÁLIDA !  :::|")
    print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::     Volte Ao Menu     :::|")
    print("|:::  E Escolha Uma Opção  :::|")
    print("|:::        Válida!!!      :::|")
    print("|:::::::::::::::::::::::::::::|")

def crud_cardapio(categoria, campo_nome):
        menu_item = ''
        while menu_item != '0':
          limpar()
          print("|:::::::::::::::::::::::::::::|")
          print(f"|::: {categoria.upper():^21} :::|")
          print("|:::::::::::::::::::::::::::::|")
          print("|:::   1 - Listar          :::|")
          print("|:::   2 - Buscar          :::|")
          print("|:::   3 - Adicionar       :::|")
          print("|:::   4 - Alterar         :::|")
          print("|:::   5 - Excluir         :::|")
          print("|:::   0 - Menu Principal  :::|")
          print("|:::::::::::::::::::::::::::::|")
          menu_item = input("|:::   Escolha uma opção: ")
          if menu_item == '1':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print(f"|::: {categoria.upper():^21} :::|")
            print("|:::::::::::::::::::::::::::::|")
            print(cardapio[categoria])
            print()
          elif menu_item == '2':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Buscar Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|::: Informe o ID do Item: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::   Item Encontrada!!  :::|")
              print("|:::   Sabor: ", cardapio[categoria][id_item][campo_nome])
              print("|:::   Preço: ", cardapio[categoria][id_item]['preco'])
              print()
            else:
              print("|:::  Item Não Encontrado :::|")
              print()
          elif menu_item == '3':
            limpar()
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
          elif menu_item == '4':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|:::   Informe o ID: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações do Item   :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::", campo_nome.capitalize(), cardapio[categoria][id_item][campo_nome])
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
          elif menu_item == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Excluir Item      :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|:::   Informe o ID: ")
            print()
            if id_item in cardapio[categoria]:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações do Item  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::", campo_nome.capitalize(), cardapio[categoria][id_item][campo_nome])
              print("|:::   Preço: ", cardapio[categoria][id_item]['preco'])
              print()
              decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
              if decisao == 's':
                del cardapio[categoria][id_item]
                print("|:::   Item Excluído!!   :::|")
              else:
                print("|:::   Exclusão Cancelada!!   :::|")
            else:
              print("|:::   Item Não Encontrada!!   :::|")
          elif menu_item == '0':
            limpar()
            menu()
          else:
            invalida()
          if menu_item != '0':
            input("Pressione ENTER para continuar...")
   
funcionarios = {
  'f123' : ["Juninho Forró", "67 99996767", "juninho@forrozeiro123.com", "Garçom", 6767.67],
  'f898' : ["Severina Guerra", "19 99093939", "severina@guerradecanudos.com", "Atendente", 1896.00],
  'f656' : ["Chico Petisco", "89 40028922", "chico@petisco.com", "Cozinheiro", 2026.00],
  'f456' : ["Neymar Jr.", "83 201120215", "Neymar@Junio.com", "Pizzaiolo", 1621.00]
}
cardapio = {
  'pizzas' : {
    "p001" : {
      "sabor" : "calabresa",
      "preco" : 40.00
    },
    'p002' : {
      "sabor" : "margarita",
      "preco" : 45.00
    },
    'p003' : {
      "sabor" : "portuguesa",
      "preco" : 40.00
    },
    'p004' : {
      "sabor" : "carne de sol",
      "preco" : 35.00
    }
  },
  'lanches' : {
    'l001' : {
    "nome" : "hamburguer",
    "preco" : 17.00
    },
    'l002' : {
      'nome' : "batata-frita",
      'preco' : 12.00
    }
  },
  'sobremesas' : {
    's001' : {
      "nome" : "pudim",
      "preco" : 7.00
    },
    's002' : {
      'nome' : 'banana-split',
      'preco' : 10.00 
    }
  },
  'bebidas' : {
    'b001' : {
      "nome" : "coca-cola 2l",
      "preco" : 12.00
    },
    'b002' : {
      "nome" : "guaraná 2l",
      "preco": 11.00
    },
  }
}
estoque = {
  'frios' : {
    'fr001' : {
      "nome" : "calabresa",
      "estoque" : True
    }
  },
  'secos' : {
    'sc001' : {
      "nome" : "farinha de trigo",
      "estoque" : True
    }
  },
  'condimentos' : {
    'cd001' : {
      "nome" : "orégano",
      "estoque" : True
    }
  },
  'bebidas' : {
    'bd001' : {
      "nome" : "coca-cola",
      "estoque" : True
    }
  } 

}
menu_prin = ""
while menu_prin != "0":
  limpar()
  print("|' ' ' ' ' ' ' ' ' ' ' ' ' ' '|")     #Primeira versão do layout, tentei fazer uma caixa de pizza kk
  print("|:                           :|")     # OBS: Alterar os "Resps" para um identificador melhor 
  linha()
  linha()
  print("|:::::-------------------:::::|")
  print("|::::/                   \\::::|")
  print("|:::|   Projeto PyPizza   |:::|")
  print("|::::\\                   /::::|")
  print("|::::::-----------------::::::|")
  linha()
  linha()
  print("|:                           :|")
  print("|. . . . . . . . . . . . . . .|")
  print()
  linha()
  print("|:::   1 - Funcionários    :::|")
  print("|:::   2 - Cardápio        :::|")
  print("|:::   3 - Estoque         :::|")
  print("|:::   4 - Relátorio       :::|")
  print("|:::   5 - Informações     :::|")
  print("|:::   0 - Sair            :::|")
  linha()
 
  menu_prin = input("|:::   Escolha uma opção: ")

  if menu_prin == '1':
    menu_fun = ''
    while menu_fun != '0':
      limpar()
      print()
      linha()
      print("|:::      FUNCIONÁRIOS     :::|")
      linha()
      print("|:::   1 - Cadastrar       :::|")
      print("|:::   2 - Pesquisar       :::|")
      print("|:::   3 - Alterar         :::|")
      print("|:::   4 - Excluir         :::|")
      print("|:::   0 - Menu Principal  :::|")
      linha()
      menu_fun = input("|:::   Escolha uma opção: ")
      print()
      if menu_fun == '1':
        limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::   Cadastrar novo      :::|")
        print("|:::     Funcionário       :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()

        nome = input("|:::  Nome: ")
        fone = input("|:::  Telefone: ")
        email = input("|:::  Email: ")
        cargo = input("|:::  Cargo: ")
        sala = float(input("|:::  Salário: "))
        id_fun = input("|:::  Id: ")
        print()
        if id_fun not in funcionarios:
          funcionarios[id_fun] = [nome, fone, email, cargo, sala]
          print("|:::   Funcionário Cadastrado Com Sucesso!!!   :::|")
          print(funcionarios)
        else:
          print("|:::   ID Enviado Já Está Em Uso!!!   :::|")

      elif menu_fun == '2':
        limpar()
        print()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::       Pesquisar       :::|")
        print("|:::      Funcionário      :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()
        id_fun = input("|:::   Informe o ID que deseja pesquisar: ")
        if id_fun in funcionarios:
          print("|:::   Funcionário Encontrado!!   :::|")
          print("|::: Nome: ", funcionarios[id_fun][0])
          print("|::: Telefone: ", funcionarios[id_fun][1])
          print("|::: Email: ", funcionarios[id_fun][2])
          print("|::: Cargo: ", funcionarios[id_fun][3])
          print("|::: Salário: ", funcionarios[id_fun][4])
          print()
        else:
          print("|:::   Funcionário Não Encontrado!!   :::|")
      elif menu_fun == '3':
        limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::     Alterar dados     :::|")
        print("|:::    do Funcionário     :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()
        id_fun = input("|:::   Informe o ID do Funcionário: ")
        if id_fun in funcionarios:
          print("|:::   Funcionário Encontrado!!   :::|")
          print("|::: Nome: ", funcionarios[id_fun][0])
          print("|::: Telefone: ", funcionarios[id_fun][1])
          print("|::: Email: ", funcionarios[id_fun][2])
          print("|::: Cargo: ", funcionarios[id_fun][3])
          print("|::: Salário: ", funcionarios[id_fun][4])
          print()
          print("|:::   Informe o Que Deseja Alterar: ")
          nome = input("|:::  Novo Nome: ")
          fone = input("|:::  Novo Telefone: ")
          email = input("|:::  Novo Email: ")
          cargo = input("|:::  Novo Cargo: ")
          sala = float(input("|:::  Novo Salário: "))
          funcionarios[id_fun] = [nome, fone, email,cargo, sala]
          print()
          print("|:::   Dados Alterados Com Sucesso!!!   :::|")
          print()
        else:
          print("|:::   Funcionário Não Encontrado!!   :::|")
      elif menu_fun == '4':
        limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::        Excluir        :::|")
        print("|:::      Funcionário      :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()
        id_fun = input("|:::   Informe o ID do funcionário que deseja excluir: ")
        if id_fun in funcionarios:
          print("|:::::::::::::::::::::::::::::::::::|")
          print("|::: Informações do Funcionário  :::|")
          print("|:::::::::::::::::::::::::::::::::::|")
          print("|:::   Funcionário Encontrado!!   :::|")
          print("|::: Nome: ", funcionarios[id_fun][0])
          print("|::: Telefone: ", funcionarios[id_fun][1])
          print("|::: Email: ", funcionarios[id_fun][2])
          print("|::: Cargo: ", funcionarios[id_fun][3])
          print("|::: Salário: ", funcionarios[id_fun][4])
          print()
          decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
          if decisao == 's':
            del funcionarios[id_fun]
            print("|:::   Funcionário Excluído!!   :::|")
          else:
            print("|:::   Exclusão Cancelada!!   :::|")
        else:
            print("|:::   Funcionário Não Encontrado!!   :::|")
            
      elif menu_fun == '0':
        limpar()
        menu()
      else:
        invalida()
      if menu_fun != '0':
         input("Pressione ENTER para continuar...")

  elif menu_prin == '2':
    menu_card = ''
    while menu_card != '0':
      limpar()
      print("|:::::::::::::::::::::::::::::|")
      print("|:::        CARDÁPIO       :::|")
      print("|:::::::::::::::::::::::::::::|")
      print("|:::   1 - Pizzas          :::|")
      print("|:::   2 - Lanches         :::|")
      print("|:::   3 - Sobremesas      :::|")
      print("|:::   4 - Bebidas         :::|")
      print("|:::   0 - Menu Principal  :::|")
      print("|:::::::::::::::::::::::::::::|")
      menu_card = input("|:::   Escolha uma opção: ")
      print ()
      if menu_card == '1':
        crud_cardapio('pizzas', 'sabor')
      elif menu_card == '2':
        crud_cardapio('lanches', 'nome')
      elif menu_card == '3':
        crud_cardapio('sobremesas', 'nome')
      elif menu_card == '4':
        crud_cardapio("bebidas", "nome")
      elif menu_card == '0':
        limpar()
        menu()
      else:
        invalida()
      print()
      if menu_card != '0':
         input("Pressione ENTER para continuar...")
  elif menu_prin == '3':
    menu_estq = ''
    while menu_estq != '0':
      limpar()
      print()
      print("|:::::::::::::::::::::::::::::|")
      print("|:::        ESTOQUE        :::|")
      print("|:::::::::::::::::::::::::::::|") ########## Em Produção...
      print("|:::   1 - Frios           :::|")
      print("|:::   2 - Secos           :::|")
      print("|:::   3 - Condimentos     :::|")
      print("|:::   4 - Bebidas         :::|")
      print("|:::   0 - Menu Principal  :::|")
      print("|:::::::::::::::::::::::::::::|")
      menu_estq = input("|:::   Escolha uma opção: ")
      print()
      if menu_estq == '1':
        menu_frios = ''
        while menu_frios != '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::       MENU FRIOS      :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   1 - Listar Frios    :::|")
            print("|:::   2 - Buscar Item     :::|")
            print("|:::   3 - Adicionar Item  :::|")
            print("|:::   4 - Atualizar Item  :::|")
            print("|:::   5 - Excluir Item    :::|")
            print("|:::   0 - Menu Principal  :::|")
            print("|:::::::::::::::::::::::::::::|")
            menu_frios = input("|::: Escolha uma opção: ")
            if menu_frios == '1':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::         FRIOS         :::|")
                print("|:::::::::::::::::::::::::::::|")
                print(estoque['frios'])
            elif menu_frios == '2':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Buscar Item      :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['frios']:
                    print()
                    print("|:::   Item Encontrado!!   :::|")
                    print("|::: Nome:",
                          estoque['frios'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['frios'][id_item]['estoque'])
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_frios == '3':
                limpar()
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
                if id_item not in estoque['frios']:
                    estoque['frios'][id_item] = {
                        "nome": nome,
                        "estoque": disponibilidade
                    }
                    print()
                    print("|::: Item Adicionado!! :::|")
                else:
                    print("|::: ID já existe!! :::|")
            elif menu_frios == '4':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Alterar Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['frios']:
                    print()
                    print("|::: Item Encontrado!! :::|")
                    print("|::: Nome:",
                          estoque['frios'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['frios'][id_item]['estoque'])
                    print()
                    nome = input("|::: Novo Nome: ")
                    disp = input("|::: Tem estoque? (s/n): ").lower()
                    if disp == 's':
                        disponibilidade = True
                    else:
                        disponibilidade = False
                    estoque['frios'][id_item]['nome'] = nome
                    estoque['frios'][id_item]['estoque'] = disponibilidade
                    print()
                    print("|::: Item Atualizado!! :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_frios == '5':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Excluir Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['frios']:
                    print()
                    print("|::: Nome:",
                          estoque['frios'][id_item]['nome'])
                    decisao = input(
                        "|::: Confirmar exclusão? (s/n): ").lower()
                    if decisao == 's':
                        del estoque['frios'][id_item]
                        print("|::: Item Excluído!! :::|")
                    else:
                        print("|::: Exclusão Cancelada :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_frios == '0':
              limpar()
              menu()
              print()
            else:
              invalida()
            if menu_frios != '0':
              input("Pressione ENTER para continuar...")
      elif menu_estq == '2':
        menu_secos = ''
        while menu_secos != '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::       MENU SECOS      :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   1 - Listar Secos    :::|")
            print("|:::   2 - Buscar Item     :::|")
            print("|:::   3 - Adicionar Item  :::|")
            print("|:::   4 - Atualizar Item  :::|")
            print("|:::   5 - Excluir Item    :::|")
            print("|:::   0 - Menu Principal  :::|")
            print("|:::::::::::::::::::::::::::::|")
            menu_secos = input("|::: Escolha uma opção: ")
            if menu_secos == '1':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::         SECOS         :::|")
                print("|:::::::::::::::::::::::::::::|")
                print(estoque['secos'])
            elif menu_secos == '2':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Buscar Item      :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['secos']:
                    print()
                    print("|:::   Item Encontrado!!   :::|")
                    print("|::: Nome:",
                          estoque['secos'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['secos'][id_item]['estoque'])
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_secos == '3':
                limpar()
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
                if id_item not in estoque['secos']:
                    estoque['secos'][id_item] = {
                        "nome": nome,
                        "estoque": disponibilidade
                    }
                    print()
                    print("|::: Item Adicionado!! :::|")
                else:
                    print("|::: ID já existe!! :::|")
            elif menu_secos == '4':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Alterar Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['secos']:
                    print()
                    print("|::: Item Encontrado!! :::|")
                    print("|::: Nome:",
                          estoque['secos'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['secos'][id_item]['estoque'])
                    print()
                    nome = input("|::: Novo Nome: ")
                    disp = input("|::: Tem estoque? (s/n): ").lower()
                    if disp == 's':
                        disponibilidade = True
                    else:
                        disponibilidade = False
                    estoque['secos'][id_item]['nome'] = nome
                    estoque['secos'][id_item]['estoque'] = disponibilidade
                    print()
                    print("|::: Item Atualizado!! :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_secos == '5':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Excluir Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['secos']:
                    print()
                    print("|::: Nome:",
                          estoque['secos'][id_item]['nome'])
                    decisao = input(
                        "|::: Confirmar exclusão? (s/n): ").lower()
                    if decisao == 's':
                        del estoque['secos'][id_item]
                        print("|::: Item Excluído!! :::|")
                    else:
                        print("|::: Exclusão Cancelada :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_secos == '0':
                limpar()
                menu()
            else:
                invalida()
            if menu_secos != '0':
                input("Pressione ENTER para continuar...")
      elif menu_estq == '3':
        menu_cond = ''
        while menu_cond != '0':
            limpar()
            print("|::::::::::::::::::::::::::::::::|")
            print("|:::      MENU CONDIMENTOS    :::|")
            print("|::::::::::::::::::::::::::::::::|")
            print("|:::   1 - Listar Condimentos :::|")
            print("|:::   2 - Buscar Item        :::|")
            print("|:::   3 - Adicionar Item     :::|")
            print("|:::   4 - Atualizar Item     :::|")
            print("|:::   5 - Excluir Item       :::|")
            print("|:::   0 - Menu Principal     :::|")
            print("|::::::::::::::::::::::::::::::::|")
            menu_cond = input("|::: Escolha uma opção: ")
            if menu_cond == '1':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      CONDIMENTOS      :::|")
                print("|:::::::::::::::::::::::::::::|")
                print(estoque['condimentos'])
            elif menu_cond == '2':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Buscar Item      :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['condimentos']:
                    print()
                    print("|:::   Item Encontrado!!   :::|")
                    print("|::: Nome:",
                          estoque['condimentos'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['condimentos'][id_item]['estoque'])
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_cond == '3':
                limpar()
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
                if id_item not in estoque['condimentos']:
                    estoque['condimentos'][id_item] = {
                        "nome": nome,
                        "estoque": disponibilidade
                    }
                    print()
                    print("|::: Item Adicionado!! :::|")
                else:
                    print("|::: ID já existe!! :::|")
            elif menu_cond == '4':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Alterar Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['condimentos']:
                    print()
                    print("|::: Item Encontrado!! :::|")
                    print("|::: Nome:",
                          estoque['condimentos'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['condimentos'][id_item]['estoque'])
                    print()
                    nome = input("|::: Novo Nome: ")
                    disp = input("|::: Tem estoque? (s/n): ").lower()
                    if disp == 's':
                        disponibilidade = True
                    else:
                        disponibilidade = False
                    estoque['condimentos'][id_item]['nome'] = nome
                    estoque['condimentos'][id_item]['estoque'] = disponibilidade
                    print()
                    print("|::: Item Atualizado!! :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_cond == '5':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Excluir Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['condimentos']:
                    print()
                    print("|::: Nome:",
                          estoque['condimentos'][id_item]['nome'])
                    decisao = input(
                        "|::: Confirmar exclusão? (s/n): ").lower()
                    if decisao == 's':
                        del estoque['condimentos'][id_item]
                        print("|::: Item Excluído!! :::|")
                    else:
                        print("|::: Exclusão Cancelada :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_cond == '0':
                limpar()
                menu()
            else:
                invalida()
            if menu_cond != '0':
                input("Pressione ENTER para continuar...")
      elif menu_estq == '4':
        menu_beb = ''
        while menu_beb != '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      MENU BEBIDAS     :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   1 - Listar Bebidas  :::|")
            print("|:::   2 - Buscar Item     :::|")
            print("|:::   3 - Adicionar Item  :::|")
            print("|:::   4 - Atualizar Item  :::|")
            print("|:::   5 - Excluir Item    :::|")
            print("|:::   0 - Menu Principal  :::|")
            print("|:::::::::::::::::::::::::::::|")
            menu_beb = input("|::: Escolha uma opção: ")
            if menu_beb == '1':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::        BEBIDAS        :::|")
                print("|:::::::::::::::::::::::::::::|")
                print(estoque['bebidas'])
            elif menu_beb == '2':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Buscar Item      :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['bebidas']:
                    print()
                    print("|:::   Item Encontrado!!   :::|")
                    print("|::: Nome:",
                          estoque['bebidas'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['bebidas'][id_item]['estoque'])
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_beb == '3':
                limpar()
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
                if id_item not in estoque['bebidas']:
                    estoque['bebidas'][id_item] = {
                        "nome": nome,
                        "estoque": disponibilidade
                    }
                    print()
                    print("|::: Item Adicionado!! :::|")
                else:
                    print("|::: ID já existe!! :::|")
            elif menu_beb == '4':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Alterar Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['bebidas']:
                    print()
                    print("|::: Item Encontrado!! :::|")
                    print("|::: Nome:",
                          estoque['bebidas'][id_item]['nome'])
                    print("|::: Estoque:",
                          estoque['bebidas'][id_item]['estoque'])
                    print()
                    nome = input("|::: Novo Nome: ")
                    disp = input("|::: Tem estoque? (s/n): ").lower()
                    if disp == 's':
                        disponibilidade = True
                    else:
                        disponibilidade = False
                    estoque['bebidas'][id_item]['nome'] = nome
                    estoque['bebidas'][id_item]['estoque'] = disponibilidade
                    print()
                    print("|::: Item Atualizado!! :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_beb == '5':
                limpar()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Excluir Item     :::|")
                print("|:::::::::::::::::::::::::::::|")
                id_item = input("|::: Informe o ID: ")
                if id_item in estoque['bebidas']:
                    print()
                    print("|::: Nome:",
                          estoque['bebidas'][id_item]['nome'])
                    decisao = input(
                        "|::: Confirmar exclusão? (s/n): ").lower()
                    if decisao == 's':
                        del estoque['bebidas'][id_item]
                        print("|::: Item Excluído!! :::|")
                    else:
                        print("|::: Exclusão Cancelada :::|")
                else:
                    print("|::: Item Não Encontrado! :::|")
            elif menu_beb == '0':
                limpar()
                menu()
            else:
                invalida()
            if menu_beb != '0':
                input("Pressione ENTER para continuar...")
      elif menu_estq == '0':
        limpar()
        menu()  
        print()
      else:
        invalida()
      print()
      input("Pressione 'ENTER' para continuar")
  elif menu_prin == '4':
    #menu_rlt = ''#
   # while menu_rlt != "0":#
    print()
    print("|:::::::::::::::::::::::::::::::::::::::::::::|")
    print("|:::               RELATORIOS              :::|")
    print("|:::::::::::::::::::::::::::::::::::::::::::::|")
    print("|:::    1 - Lista Geral De Funcionários    :::|")
    print("|:::    2 - Lista Geral Do Cardápio        :::|")
    print("|:::    3 - Lista Geral Do Estoque         :::|")
    print("|:::    4 - Lista de Funcioários por Cargo :::|")
    print("|:::    5 - Menu Principal                 :::|") 
    print("|:::::::::::::::::::::::::::::::::::::::::::::|")
    print("|:::    Função Ainda Em Desenvolvimento!!! :::|")
    print("|:::::::::::::::::::::::::::::::::::::::::::::|")
    #menu_rlt = input("|:::   Escolha uma opção: ")#
    print()
    input("Pressione 'ENTER' para continuar")
  elif menu_prin == '5':
    print()
    print("|::::::::::::::::::::::::::::::::::::::::::|")
    print("|:::             INFORMAÇÕES            :::|")
    print("|::::::::::::::::::::::::::::::::::::::::::|")
    print("|::: Sistema De Gestão Para Pizzaria    :::|")
    print("|::: Desenvolvedor:                     :::|")
    print("|::: Isaias Vidal Medeiros              :::|")
    print("|::: Licença Pública MIT                :::|")
    print("|::: https://opensource.org/license/mit :::|")
    print("|::::::::::::::::::::::::::::::::::::::::::|")
    print()
    input("Pressione 'ENTER' para continuar")
  elif menu_prin == '0':
    print("|:::::::::::::::::::::::::::::|")
    print("|:::      Encerrando       :::|")
    print("|:::     O Programa em     :::|")
    print("|:::      3...2...1...     :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
  else:
    invalida()
  input("Pressione 'ENTER' para continuar")

print("|:::::::::::::::::::::::::::::|")
print("|:::   Obrigado Por Usar   :::|")
print("|:::    O Programa!! :)    :::|")
print("|:::::::::::::::::::::::::::::|")
print()
print("|:::::::::::::::::::::::::::::|")
print("|:::     Até Mais !!  ;)   :::|")
print("|:::::::::::::::::::::::::::::|")
print("Fim do Programa!!!")


