import os   #Versao 3
import pickle
from funcionarios import menu_funci
import funcoes
def tracado():
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
              print("|:::   Item Encontrado!!  :::|")
              print("|:::   Nome: ", cardapio[categoria][id_item][campo_nome])
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
def recupera_funcionarios():   
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
            nascimento = campos[5]
            cpf = campos[6]
            funcionarios[id_fun] = [nome, fone, email, cargo, nascimento, cpf]
    arq_funcionarios.close()
  except:
    funcionarios = {
      'f123' : ["Juninho Forró", "67 99996767", "juninho@forrozeiro123.com", "Garçom", "13/04/2002", "43435678655"],
      'f898' : ["Severina Guerra", "19 99093939", "severina@guerradecanudos.com", "Atendente", "11/11/1990", "23456765432"],
      'f656' : ["Chico Petisco", "89 40028922", "chico@petisco.com", "Cozinheiro", "23/08/2006", "115679809876"],
      'f456' : ["Neymar Jr.", "83 201120215", "Neymar@Junio.com", "Pizzaiolo", "23/11/1999", "67676767676"]
    }
    arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")
    for id_fun, dados in funcionarios.items():
        arq_funcionarios.write(f"{id_fun},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
    arq_funcionarios.close
  return funcionarios

def recupera_cardapio():
  cardapio = {}
  try:
    arq_cardapio = open("cardapio.csv", "rt", encoding="utf-8")
    for linha in arq_cardapio:
        linha = linha.strip()
        if linha:
            categoria, id_item, nome, preco = linha.split(",")
            if categoria not in cardapio:
              cardapio[categoria] = {}
            cardapio[categoria][id_item] = {
              "nome": nome,
              "preco": float(preco)
            }
    arq_cardapio.close()
  except:
    cardapio = {
      'pizzas' : {
        "p001" : {
          "nome" : "calabresa",
          "preco" : 40.00
        },
        'p002' : {
          "nome" : "margarita",
          "preco" : 45.00
        },
        'p003' : {
          "nome" : "portuguesa",
          "preco" : 40.00
        },
        'p004' : {
          "nome" : "carne de sol",
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
    arq_cardapio = open("cardapio.csv", "wt", encoding="utf-8")
    for categoria, itens in cardapio.items():
      for id_item, dados in itens.items():
          arq_cardapio.write(
            f"{categoria},{id_item},{dados['nome']},{dados['preco']}\n")
    arq_cardapio.close()
  return cardapio

def recupera_estoque():
  estoque = {}
  try:
    arq_estoque = open("estoque.csv", "rt", encoding="utf-8")
    for linha in arq_estoque:
        linha = linha.strip()
        if linha:
            categoria, id_item, nome, estoque = linha.split(",")
            if categoria not in cardapio:
              estoque[categoria] = {}
            estoque[categoria][id_item] = {
              "nome": nome,
              "estoque": estoque
            }
    arq_estoque.close()
  except:
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
    arq_estoque = open("estoque.csv", "wt", encoding="utf-8")
    for categoria, itens in estoque.items():
      for id_item, dados in itens.items():
          arq_estoque.write(
            f"{categoria},{id_item},{dados['nome']},{dados['estoque']}\n")
    arq_estoque.close()
  return estoque

def grava_funcionarios(funcionarios):
   arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")
   for id_fun, dados in funcionarios.items():
      arq_funcionarios.write(f"{id_fun},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
   arq_funcionarios.close()

def grava_cardapio(cardapio):
   arq_cardapio = open("cardapio.csv", "wt", encoding="utf-8")
   for categoria, itens in cardapio.items():
      for id_item, dados in itens.items():
          arq_cardapio.write(f"{categoria},{id_item},{dados['nome']},{dados['preco']}\n")
   arq_cardapio.close()

def grava_estoque(estoque):
  arq_estoque = open("estoque.csv", "wt", encoding="utf-8")
  for categoria, itens in estoque.items():
     for id_item, dados in itens.items():
         arq_estoque.write(f"{categoria},{id_item},{dados['nome']},{dados['estoque']}\n")
  arq_estoque.close()
   

funcionarios = recupera_funcionarios()
cardapio = recupera_cardapio()
estoque = recupera_estoque()

menu_prin = ""
while menu_prin != "0":
  limpar()
  print("|' ' ' ' ' ' ' ' ' ' ' ' ' ' '|")     #Primeira versão do layout, tentei fazer uma caixa de pizza kk
  print("|:                           :|")     # OBS: Alterar os "Resps" para um identificador melhor 
  tracado()
  tracado()
  print("|:::::-------------------:::::|")
  print("|::::/                   \\::::|")
  print("|:::|   Projeto PyPizza   |:::|")
  print("|::::\\                   /::::|")
  print("|::::::-----------------::::::|")
  tracado()
  tracado()
  print("|:                           :|")
  print("|. . . . . . . . . . . . . . .|")
  print()
  tracado()
  print("|:::   1 - Funcionários    :::|")
  print("|:::   2 - Cardápio        :::|")
  print("|:::   3 - Estoque         :::|")
  print("|:::   4 - Relátorio       :::|")
  print("|:::   5 - Informações     :::|")
  print("|:::   0 - Sair            :::|")
  tracado()

 
  menu_prin = input("|:::   Escolha uma opção: ")

  if menu_prin == '1':
    menu_funci(funcionarios)
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
        crud_cardapio('pizzas', 'nome')
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
      if menu_estq != '0':
         input("Pressione ENTER para continuar...")
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

grava_funcionarios(funcionarios)
grava_cardapio(cardapio)
grava_estoque(estoque)