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

def desativar(categoria, id_item):
    decisao = input("|:::   Tecle 's' Para Confirmar a Desativação:  ").lower()

    if decisao == 's':
        categoria[id_item]["ativo"] = False
        print("|:::   Desativação Concluída!!   :::|")
    else:
        print("|:::   Desativação Cancelada!!   :::|")

def ativar(categoria, id_item):
    decisao = input("|:::   Tecle 's' Para Confirmar a Ativação:  ").lower()

    if decisao == 's':
        categoria[id_item]["ativo"] = True
        print("|:::   Ativação Concluída!!   :::|")
    else:
        print("|:::   Ativação Cancelada!!   :::|")

        
def grava_funcionarios(funcionarios):
   arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")
   for id_item, dados in funcionarios.items():
            arq_funcionarios.write(
                f"{id_item},{dados['nome']},{dados['telefone']},"
                f"{dados['email']},{dados['cargo']},"
                f"{dados['nascimento']},{dados['cpf']},"
                f"{dados['ativo']}\n"
            )
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
                id_item, nome, telefone, email, cargo, nascimento, cpf, ativo = linha.split(",")

                funcionarios[id_item] = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email,
                    "cargo": cargo,
                    "nascimento": nascimento,
                    "cpf": cpf,
                    "ativo": ativo == "True"
                }

        arq_funcionarios.close()

    except FileNotFoundError:
        funcionarios = {
            'f123': {
                'nome': "Juninho Forró",
                'telefone': "67 99996767",
                'email': "juninho@forrozeiro123.com",
                'cargo': "Garçom",
                'nascimento': "13/04/2002",
                'cpf': "43435678655",
                'ativo': True
            },

            'f898': {
                'nome': "Severina Guerra",
                'telefone': "19 99093939",
                'email': "severina@guerradecanudos.com",
                'cargo': "Atendente",
                'nascimento': "11/11/1990",
                'cpf': "23456765432",
                'ativo': True
            },

            'f656': {
                'nome': "Chico Petisco",
                'telefone': "89 40028922",
                'email': "chico@petisco.com",
                'cargo': "Cozinheiro",
                'nascimento': "23/08/2006",
                'cpf': "115679809876",
                'ativo': True
            },

            'f456': {
                'nome': "Neymar Jr.",
                'telefone': "83 201120215",
                'email': "Neymar@Junio.com",
                'cargo': "Pizzaiolo",
                'nascimento': "23/11/1999",
                'cpf': "67676767676",
                'ativo': True
            }
        }

        arq_funcionarios = open("funcionarios.csv", "wt", encoding="utf-8")

        for id_item, dados in funcionarios.items():
            arq_funcionarios.write(
                f"{id_item},{dados['nome']},{dados['telefone']},"
                f"{dados['email']},{dados['cargo']},"
                f"{dados['nascimento']},{dados['cpf']},"
                f"{dados['ativo']}\n"
            )

        arq_funcionarios.close()

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
              "preco": preco
            }
    arq_cardapio.close()
  except:
    cardapio = {
      'pizzas' : {
        "p001" : {
          "nome" : "calabresa",
          "preco" : "40.00"
        },
        'p002' : {
          "nome" : "margarita",
          "preco" : "45.00"
        },
        'p003' : {
          "nome" : "portuguesa",
          "preco" : "40.00"
        },
        'p004' : {
          "nome" : "carne de sol",
          "preco" : "35.00"
        }
      },
      'lanches' : {
        'l001' : {
        "nome" : "hamburguer",
        "preco" : "17.00"
        },
        'l002' : {
          'nome' : "batata-frita",
          'preco' : "12.00"
        }
      },
      'sobremesas' : {
        's001' : {
          "nome" : "pudim",
          "preco" : "7.00"
        },
        's002' : {
          'nome' : 'banana-split',
          'preco' : "10.00"
        }
      },
      'bebidas' : {
        'b001' : {
          "nome" : "coca-cola 2l",
          "preco" : "12.00"
        },
        'b002' : {
          "nome" : "guaraná 2l",
          "preco": "11.00"
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