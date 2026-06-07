import os   #Versao 2
def linha():
    print("|:::::::::::::::::::::::::::::|")
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print("|:::::::::::::::::::::::::::::|")
        print("|:::      Voltando ao      :::|")
        print("|:::    Menu Principal...  :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()
      else:
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
      print()
      input("Pressione 'ENTER' para continuar")

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
        menu_piz = ''
        while menu_piz != '0':
          limpar()
          print("|:::::::::::::::::::::::::::::|")
          print("|:::      Menu Pizzas      :::|")
          print("|:::::::::::::::::::::::::::::|")
          print("|:::   1 - Lista Pizzas    :::|")
          print("|:::   2 - Buscar Pizza    :::|")
          print("|:::   3 - Adicionar Pizza :::|")
          print("|:::   4 - Alterar Pizza   :::|")
          print("|:::   5 - Excluir Pizza   :::|")
          print("|:::   0 - Menu Principal  :::|")
          print("|:::::::::::::::::::::::::::::|")
          menu_piz = input("|:::   Escolha uma opção: ")
          if menu_piz == '1':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::        Pizzas         :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   Pizzas Cadastradas: ", (cardapio["pizzas"]))
            print()
          elif menu_piz == '2':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Buscar Pizza     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_piz = input("|::: Informe o ID da Pizza: ")
            print()
            if id_piz in cardapio['pizzas']:
              print("|:::   Pizza Encontrada!!  :::|")
              print("|:::   Sabor: ", cardapio['pizzas'][id_piz]['sabor'])
              print("|:::   Preço: ", cardapio['pizzas'][id_piz]['preco'])
              print()
            else:
              print("|:::  Pizza Não Encontrada :::|")
              print()
          elif menu_piz == '3':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Adicionar Pizza   :::|")
            print("|:::::::::::::::::::::::::::::|")
            sabor = input("|:::   Informe o Novo Sabor: ")
            preco = float(input("|:::   Informe o Preço: "))
            id_piz = input("|:::   Informe um ID Para a Pizza: ")
            print()
            if id_piz not in cardapio['pizzas']:
              cardapio['pizzas'][id_piz] = {"sabor" : sabor, "preco" : preco}
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Pizza Adicionada!!  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print(cardapio['pizzas'][id_piz])
              print()
            else:
              print("|:::   ID Enviado Já Está Em Uso!!   :::| ")
          elif menu_piz == '4':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar Pizza     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_piz = input("|:::   Informe o ID da Pizza: ")
            print()
            if id_piz in cardapio['pizzas']:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações da Pizza  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Sabor: ", cardapio['pizzas'][id_piz]['sabor'])
              print("|:::   Preço: ", cardapio['pizzas'][id_piz]['preco'])
              print()
              print("|:::   Informe o que Deseja Alterar   :::|")
              sabor = input("|:::   Informe o Sabor: ")
              preco = float(input("|:::   Informe o Preço: "))
              cardapio['pizzas'][id_piz]['sabor'] = sabor
              cardapio['pizzas'][id_piz]['preco'] = preco
              print()
              print("|::: Pizza Alterada com Sucesso :::|")
              print(cardapio['pizzas'][id_piz])
            else:
              print("|:::   Pizza não encontrada :::|")
          elif menu_piz == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Excluir Pizza     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_piz = input("|:::   Informe o ID da Pizza: ")
            print()
            if id_piz in cardapio['pizzas']:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações da Pizza  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Sabor: ", cardapio['pizzas'][id_piz]['sabor'])
              print("|:::   Preço: ", cardapio['pizzas'][id_piz]['preco'])
              print()
              decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
              if decisao == 's':
                del cardapio['pizzas'][id_piz]
                print("|:::   Pizza Excluída!!   :::|")
              else:
                print("|:::   Exclusão Cancelada!!   :::|")
            else:
              print("|:::   Pizza Não Encontrada!!   :::|")
          elif menu_piz == '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Voltando ao      :::|")
            print("|:::    Menu Principal...  :::|")
            print("|:::::::::::::::::::::::::::::|")
            print()
          else:
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
          if menu_piz != '0':
            input("Pressione ENTER para continuar...")
      elif menu_card == '2':
        menu_lnc = ''
        while menu_lnc != '0':
          limpar()
          print("|:::::::::::::::::::::::::::::|")
          print("|:::      Menu Lanches     :::|")
          print("|:::::::::::::::::::::::::::::|")
          print("|:::   1 - Lista Lanches   :::|")
          print("|:::   2 - Buscar Lanche   :::|")
          print("|:::   3 - AdicionarLanche :::|")
          print("|:::   4 - Alterar Lanche  :::|")
          print("|:::   5 - Excluir Lanche  :::|")
          print("|:::   0 - Menu Principal  :::|")
          print("|:::::::::::::::::::::::::::::|")
          menu_lnc = input("|:::   Escolha uma opção: ")
          if menu_lnc == '1':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::        Lanches        :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   Lanches Cadastrados: ", (cardapio["lanches"]))
          elif menu_lnc == '2':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Buscar Lanche    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_lnc = input("|::: Informe o ID do Lanche: ")
            print()
            if id_lnc in cardapio['lanches']:
              print("|:::   Lanche Encontrado!!  :::|")
              print("|:::   Lanche: ", cardapio['lanches'][id_lnc]['nome'])
              print("|:::   Preço: ", cardapio['lanches'][id_lnc]['preco'])
              print()
            else:
              print("|:::  Lanche Não Encontrado :::|")
              print()
          elif menu_lnc == '3':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Adicionar Lanche  :::|")
            print("|:::::::::::::::::::::::::::::|")
            nome = input("|:::   Informe o Novo Lanche: ")
            preco = float(input("|:::   Informe o Preço: "))
            id_lnc = input("|:::   Informe um ID Para o Lanche: ")
            print()
            if id_lnc not in cardapio['lanches']:
              cardapio['lanches'][id_lnc] = {"nome" : nome, "preco" : preco}
              print("|:::::::::::::::::::::::::::::|")
              print("|:::  Lanche Adicionado!!  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print(cardapio['lanches'][id_lnc])
              print()
            else:
              print("|:::   ID Enviado Já Está Em Uso!!   :::| ")
          elif menu_lnc == '4':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar Lanche    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_lnc = input("|:::   Informe o ID do Lanche: ")
            print()
            if id_lnc in cardapio['lanches']:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações do  Lanche  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Lanche: ", cardapio['lanches'][id_lnc]['nome'])
              print("|:::   Preço: ", cardapio['lanches'][id_lnc]['preco'])
              print()
              print("|:::   Informe o que Deseja Alterar   :::|")
              nome = input("|:::   Informe o Novo Nome: ")
              preco = float(input("|:::   Informe o Novo Preço: "))
              cardapio['lanches'][id_lnc]['nome'] = nome
              cardapio['lanches'][id_lnc]['preco'] = preco
              print()
              print("|::: Lanche Alterado com Sucesso!! :::|")
              print(cardapio['lanches'][id_lnc])
            else:
              print("|:::   Lanche não encontrado!! :::|")
          elif menu_lnc == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Excluir Lanche    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_lnc = input("|:::   Informe o ID do Lanche: ")
            print()
            if id_lnc in cardapio['lanches']:
              print("|:::::::::::::::::::::::::::::|")
              print("|::: Informações do Lanche :::|")
              print("|:::::::::::::::::::::::::::::|")
              print("|:::   Lanche: ", cardapio['lanches'][id_lnc]['nome'])
              print("|:::   Preço: ", cardapio['lanches'][id_lnc]['preco'])
              print()
              decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
              if decisao == 's':
                del cardapio['lanches'][id_lnc]
                print("|:::   Lanche Excluído Com Sucesso!!   :::|")
              else:
                print("|:::   Exclusão Cancelada!!   :::|")
            else:
              print("|:::   Lanche Não Encontrado!!   :::|")
          elif menu_lnc == '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Voltando ao      :::|")
            print("|:::    Menu Principal...  :::|")
            print("|:::::::::::::::::::::::::::::|")
            print()
          else:
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
          if menu_lnc != '0':
            input("Pressione ENTER para continuar...")
      elif menu_card == '3':
        menu_sbm = ''
        while menu_sbm != '0':
          limpar()
          print("|:::::::::::::::::::::::::::::::::|")
          print("|:::       Menu Sobremesa      :::|")
          print("|:::::::::::::::::::::::::::::::::|")
          print("|:::   1 - Lista Sobremesas    :::|")
          print("|:::   2 - Buscar Sobremesa    :::|")
          print("|:::   3 - Adicionar Sobremesa :::|")
          print("|:::   4 - Alterar Sobremesa   :::|")
          print("|:::   5 - Excluir Sobremesa   :::|")
          print("|:::   0 - Menu Principal      :::|")
          print("|:::::::::::::::::::::::::::::::::|")
          menu_sbm = input("|:::   Escolha uma opção: ")
          if menu_sbm == '1': 
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Sobremesas       :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   Sobremesas Cadastrados: ", (cardapio["sobremesas"]))
          elif menu_sbm == '2':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::    Buscar Sobremesa   :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_sbm = input("|::: Informe o ID da Sobremesa: ")
            print()
            if id_sbm in cardapio['sobremesas']:
              print("|:::   Sobremesa Encontrada!!  :::|")
              print("|:::   Sobremesa: ", cardapio['sobremesas'][id_sbm]['nome'])
              print("|:::   Preço: ", cardapio['sobremesas'][id_sbm]['preco'])
              print()
            else:
              print("|:::  Sobremesa Não Encontrada :::|")
              print()
          elif menu_sbm == '3':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::  Adicionar Sobremesa  :::|")
            print("|:::::::::::::::::::::::::::::|")
            nome = input("|:::   Informe a Nova Sobremesa: ")
            preco = float(input("|:::   Informe o Preço: "))
            id_sbm = input("|:::   Informe um ID Para a Sobremesa: ")
            print()
            if id_sbm not in cardapio['sobremesas']:
              cardapio['sobremesas'][id_sbm] = {"nome" : nome, "preco" : preco}
              print("|::::::::::::::::::::::::::::::::|")
              print("|:::  Sobremesa Adicionado!!  :::|")
              print("|::::::::::::::::::::::::::::::::|")
              print(cardapio['sobremesas'][id_sbm])
              print()
            else:
              print("|:::   ID Enviado Já Está Em Uso!!   :::| ")
          elif menu_sbm == '4':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   Alterar Sobremesa   :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_sbm = input("|:::   Informe o ID do Lanche: ")
            print()
            if id_sbm in cardapio['sobremesas']:
              print("|:::::::::::::::::::::::::::::::::|")
              print("|::: Informações da Sobremesa  :::|")
              print("|:::::::::::::::::::::::::::::::::|")
              print("|:::   Sobremesa: ", cardapio['sobremesas'][id_sbm]['nome'])
              print("|:::   Preço: ", cardapio['sobremesas'][id_sbm]['preco'])
              print()
              print("|:::   Informe o que Deseja Alterar   :::|")
              nome = input("|:::   Informe o Novo Nome: ")
              preco = float(input("|:::   Informe o Novo Preço: "))
              cardapio['sobremesas'][id_sbm]['nome'] = nome
              cardapio['sobremesas'][id_sbm]['preco'] = preco
              print()
              print("|::: Sobremesa Alterada com Sucesso!! :::|")
              print(cardapio['sobremesas'][id_sbm])
            else:
              print("|:::   Sobremesa não encontrada!! :::|")
          elif menu_sbm == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::    Excluir Sobremesa  :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_sbm = input("|:::   Informe o ID da Sobremesa: ")
            print()
            if id_sbm in cardapio['sobremesas']:
              print("|::::::::::::::::::::::::::::::::|")
              print("|::: Informações da Sobremesa :::|")
              print("|::::::::::::::::::::::::::::::::|")
              print("|:::   Sobremesa: ", cardapio['sobremesas'][id_sbm]['nome'])
              print("|:::   Preço: ", cardapio['sobremesas'][id_sbm]['preco'])
              print()
              decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
              if decisao == 's':
                del cardapio['sobremesas'][id_sbm]
                print("|:::   Sobremesa Excluída Com Sucesso!!   :::|")
              else:
                print("|:::   Exclusão Cancelada!!   :::|")
            else:
              print("|:::   Sobremesa Não Encontrada!!   :::|")
          elif menu_sbm == '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Voltando ao      :::|")
            print("|:::    Menu Principal...  :::|")
            print("|:::::::::::::::::::::::::::::|")
            print()
          else:
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
          if menu_sbm != '0':
             input("Pressione ENTER para continuar...")
      elif menu_card == '4':
        menu_bbd = ''
        while menu_bbd != '0':
          limpar()
          print("|:::::::::::::::::::::::::::::::::|")
          print("|:::       Menu Bebidas        :::|")
          print("|:::::::::::::::::::::::::::::::::|")
          print("|:::   1 - Lista Bebidas       :::|")
          print("|:::   2 - Buscar Bebida       :::|")
          print("|:::   3 - Adicionar Bebida    :::|")
          print("|:::   4 - Alterar Bebida      :::|")
          print("|:::   5 - Excluir Bebida      :::|")
          print("|:::   0 - Menu Principal      :::|")
          print("|:::::::::::::::::::::::::::::::::|")
          menu_bbd = input("|:::   Escolha uma opção: ")
          if menu_bbd == '1':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Bebidas       :::|")
            print("|:::::::::::::::::::::::::::::|")
            print("|:::   Bebidas Cadastrados: ", (cardapio["bebidas"]))
          elif menu_bbd == '2':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Buscar Bebida    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_bbd = input("|::: Informe o ID da Bebida: ")
            print()
            if id_bbd in cardapio['bebidas']:
              print("|:::   Bebida Encontrada!!  :::|")
              print("|:::   Bebida: ", cardapio['bebidas'][id_bbd]['nome'])
              print("|:::   Preço: ", cardapio['bebidas'][id_bbd]['preco'])
              print()
            else:
              print("|:::  Bebida Não Encontrada :::|")
              print()
          elif menu_bbd == '3':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::    Adicionar Bebida   :::|")
            print("|:::::::::::::::::::::::::::::|")
            nome = input("|:::   Informe a Nova Bebida: ")
            preco = float(input("|:::   Informe o Preço: "))
            id_bbd = input("|:::   Informe um ID Para a Bebida: ")
            print()
            if id_bbd not in cardapio['bebidas']:
              cardapio['bebidas'][id_bbd] = {"nome" : nome, "preco" : preco}
              print("|::::::::::::::::::::::::::::::::|")
              print("|:::  Bebida Adicionada!!  :::|")
              print("|::::::::::::::::::::::::::::::::|")
              print(cardapio['bebidas'][id_bbd])
              print()
            else:
              print("|:::   ID Enviado Já Está Em Uso!!   :::| ")
          elif menu_bbd == '4':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar Bebida    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_bbd = input("|:::   Informe o ID da Bebida: ")
            print()
            if id_bbd in cardapio['bebidas']:
              print("|:::::::::::::::::::::::::::::::::|")
              print("|:::   Informações da Bebida   :::|")
              print("|:::::::::::::::::::::::::::::::::|")
              print("|:::   Bebida: ", cardapio['bebidas'][id_bbd]['nome'])
              print("|:::   Preço: ", cardapio['bebidas'][id_bbd]['preco'])
              print()
              print("|:::   Informe o que Deseja Alterar   :::|")
              nome = input("|:::   Informe o Novo Nome: ")
              preco = float(input("|:::   Informe o Novo Preço: "))
              cardapio['bebidas'][id_bbd]['nome'] = nome
              cardapio['bebidas'][id_bbd]['preco'] = preco
              print()
              print("|::: Bebida Alterada com Sucesso!! :::|")
              print(cardapio['bebidas'][id_bbd])
            else:
              print("|:::   Bebida não encontrada!! :::|")
          elif menu_bbd == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Excluir Bebida    :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_bbd = input("|:::   Informe o ID da Bebida: ")
            print()
            if id_bbd in cardapio['bebidas']:
              print("|::::::::::::::::::::::::::::::::|")
              print("|:::   Informações da Bebida  :::|")
              print("|::::::::::::::::::::::::::::::::|")
              print("|:::   Bebida: ", cardapio['bebidas'][id_bbd]['nome'])
              print("|:::   Preço: ", cardapio['bebidas'][id_bbd]['preco'])
              print()
              decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
              if decisao == 's':
                del cardapio['bebidas'][id_bbd]
                print("|:::   Bebida Excluída Com Sucesso!!   :::|")
              else:
                print("|:::   Exclusão Cancelada!!   :::|")
            else:
              print("|:::   Bebida Não Encontrada!!   :::|")
          elif menu_bbd == '0':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Voltando ao      :::|")
            print("|:::    Menu Principal...  :::|")
            print("|:::::::::::::::::::::::::::::|")
            print()
          else:
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
          if menu_bbd != '0':
             input("Pressione ENTER para continuar...")
      elif menu_card == '0':
        limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::      Voltando ao      :::|")
        print("|:::    Menu Principal...  :::|")
        print("|:::::::::::::::::::::::::::::|")
        print()
      else:
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
      print()
      input("Pressione 'ENTER' para continuar")
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
              print("|:::::::::::::::::::::::::::::|")
              print("|:::      Voltando ao      :::|")
              print("|:::    Menu Principal...  :::|")
              print("|:::::::::::::::::::::::::::::|")
              print()
            else:
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
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Voltando ao      :::|")
                print("|:::    Menu Principal...  :::|")
                print("|:::::::::::::::::::::::::::::|")
                print()
            else:
                print("|:::::::::::::::::::::::::::::|")
                print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
                print("|:::  !  OPÇÃO INVÁLIDA !  :::|")
                print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
                print("|:::::::::::::::::::::::::::::|")
                print()
                print("|:::::::::::::::::::::::::::::|")
                print("|:::     Volte Ao Menu     :::|")
                print("|:::  E EscolHA Uma Opção  :::|")
                print("|:::        Válida!!!      :::|")
                print("|:::::::::::::::::::::::::::::|")
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
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Voltando ao      :::|")
                print("|:::    Menu Principal...  :::|")
                print("|:::::::::::::::::::::::::::::|")
                print()
            else:
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
                print("|:::::::::::::::::::::::::::::|")
                print("|:::      Voltando ao      :::|")
                print("|:::    Menu Principal...  :::|")
                print("|:::::::::::::::::::::::::::::|")
                print()
            else:
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
            if menu_beb != '0':
                input("Pressione ENTER para continuar...")
      elif menu_estq == '0':
        limpar()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::      Voltando ao      :::|")
        print("|:::    Menu Principal...  :::|")
        print("|:::::::::::::::::::::::::::::|")  
        print()
      else:
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
        print()
        input("Pressione 'ENTER' para continuar")
  elif menu_prin == '4':
    #menu_rlt = ''
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
    print("|:::::::::::::::::::::::::::::|")
    print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
    print("|:::  !  OPÇÃO INVÁLIDA !  :::|")
    print("|:::  ! ! ! ! ! ! ! ! ! !  :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::     Volte Ao Menu     :::|")
    print("|:::   Principal e Tente   :::|")
    print("|:::      Novamente!!      :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
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


