import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exclusao(categoria,id_item):
    decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
    if decisao == 's':
        del categoria[id_item]
        print("|:::   Exclusão Concluída!!   :::|")
    else:
        print("|:::   Exclusão Cancelada!!   :::|")

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
            if categoria not in estoque:
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



# def valida_cpf():