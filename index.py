import os   #Versao 4
import pickle
from funcionarios import menu_funci
import funcoes
from cardapio import menu_card
from estoque import menu_estoque
import textos

def tracado():
    print("|:::::::::::::::::::::::::::::|")
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')  
funcionarios = funcoes.recupera_funcionarios()
cardapio = funcoes.recupera_cardapio()
estoque = funcoes.recupera_estoque()

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
    menu_card(cardapio)
  elif menu_prin == '3':
    menu_estoque(estoque)
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
    textos.invalida()
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

funcoes.grava_funcionarios(funcionarios)
funcoes.grava_cardapio(cardapio)
funcoes.grava_estoque(estoque)