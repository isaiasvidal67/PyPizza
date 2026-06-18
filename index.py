import os   #Versao 3
import pickle

def traçado():
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
def crud_estoque(categoria, campo_nome):
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
            print(estoque[categoria])
            print()
          elif menu_item == '2':
            limpar()
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
          elif menu_item == '3':
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
            if id_item not in estoque[categoria]:
                estoque[categoria][id_item] = {
                    "nome": nome,
                    "estoque": disponibilidade
                }
                print()
                print("|::: Item Adicionado!! :::|")
          elif menu_item == '4':
            limpar()
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
          elif menu_item == '5':
            limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::      Excluir Item     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_item = input("|::: Informe o ID: ")
            if id_item in estoque['secos']:
                print()
                print("|::: Nome:",
                      estoque[categoria][id_item][campo_nome])
                decisao = input(
                    "|::: Confirmar exclusão? (s/n): ").lower()
                if decisao == 's':
                    del estoque[categoria][id_item]
                    print("|::: Item Excluído!! :::|")
                else:
                    print("|::: Exclusão Cancelada :::|")
            else:
                print("|::: Item Não Encontrado! :::|")
          elif menu_item == '0':
            limpar()
            menu()
          else:
            invalida()
          if menu_item != '0':
            input("Pressione ENTER para continuar...")
   
funcionarios = {}
try:
   arq_funcionarios = open("funcionarios.csv", "rt", encoding="utf-8")
   for linha in arq_funcionarios:
       linha = linha.strip()
       if linha:
          campos = linha.split(",")
          id_fun = campos[0]
          nome = campos[1]
          fone = campos[2]
          email = campos[3]
          cargo = campos[4]
          funcionarios[id_fun] = [nome, fone, email, cargo]
   arq_funcionarios.close()
except:
  funcionarios = {
    'f123' : ["Juninho Forró", "67 99996767", "juninho@forrozeiro123.com", "Garçom"],
    'f898' : ["Severina Guerra", "19 99093939", "severina@guerradecanudos.com", "Atendente"],
    'f656' : ["Chico Petisco", "89 40028922", "chico@petisco.com", "Cozinheiro"],
    'f456' : ["Neymar Jr.", "83 201120215", "Neymar@Junio.com", "Pizzaiolo"]
  }
  arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")
  for id_fun, dados in funcionarios.items():
      arq_funcionarios.write(f"{id_fun},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
  arq_funcionarios.close
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
  traçado()
  traçado()
  print("|:::::-------------------:::::|")
  print("|::::/                   \\::::|")
  print("|:::|   Projeto PyPizza   |:::|")
  print("|::::\\                   /::::|")
  print("|::::::-----------------::::::|")
  traçado()
  traçado()
  print("|:                           :|")
  print("|. . . . . . . . . . . . . . .|")
  print()
  traçado()
  print("|:::   1 - Funcionários    :::|")
  print("|:::   2 - Cardápio        :::|")
  print("|:::   3 - Estoque         :::|")
  print("|:::   4 - Relátorio       :::|")
  print("|:::   5 - Informações     :::|")
  print("|:::   0 - Sair            :::|")
  traçado()
 
  menu_prin = input("|:::   Escolha uma opção: ")

  if menu_prin == '1':
    menu_fun = ''
    while menu_fun != '0':
      limpar()
      print()
      traçado()
      print("|:::      FUNCIONÁRIOS     :::|")
      traçado()
      print("|:::   1 - Cadastrar       :::|")
      print("|:::   2 - Pesquisar       :::|")
      print("|:::   3 - Alterar         :::|")
      print("|:::   4 - Excluir         :::|")
      print("|:::   0 - Menu Principal  :::|")
      traçado()
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
        id_fun = input("|:::  Id: ")
        print()
        if id_fun not in funcionarios:
          funcionarios[id_fun] = [nome, fone, email, cargo]
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
          print()
          print("|:::   Informe o Que Deseja Alterar: ")
          nome = input("|:::  Novo Nome: ")
          fone = input("|:::  Novo Telefone: ")
          email = input("|:::  Novo Email: ")
          cargo = input("|:::  Novo Cargo: ")
          funcionarios[id_fun] = [nome, fone, email,cargo]
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
        crud_estoque('frios', 'nome')
      elif menu_estq == '2':
        crud_estoque('secos', 'nome')
      elif menu_estq == '3':
        crud_estoque('condimentos', 'nome')
      elif menu_estq == '4':
        crud_estoque('bebidas', 'nome')
      elif menu_estq == '0':
        limpar()
        menu()  
        print()
      else:
        invalida()
      print()
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

arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")
for id_fun, dados in funcionarios.items():
    arq_funcionarios.write(f"{id_fun},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
arq_funcionarios.close()