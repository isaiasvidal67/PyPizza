import os   #Versao 4
import pickle
import funcoes
import textos 
from funcionarios import menu_funci
from cardapio import menu_card
from estoque import menu_estoque
from relatorios import menu_relatorio
from informacoes import menu_informacoes
funcionarios = funcoes.recupera_funcionarios()
cardapio = funcoes.recupera_cardapio()
estoque = funcoes.recupera_estoque()
menu_prin = ""
while menu_prin != "0":
  textos.layout_menu()
  menu_prin = input("|:::   Escolha uma opção: ")
  if menu_prin == '1':
    menu_funci(funcionarios)
  elif menu_prin == '2':
    menu_card(cardapio)
  elif menu_prin == '3':
    menu_estoque(estoque)
  elif menu_prin == '4':
    menu_relatorio(funcionarios,cardapio,estoque)
  elif menu_prin == '5':
    menu_informacoes()
  elif menu_prin == '0':
    textos.encerrando()
  else:
    textos.invalida()
  input("Pressione 'ENTER' para continuar")
textos.finaliza()
funcoes.grava_funcionarios(funcionarios)
funcoes.grava_cardapio(cardapio)
funcoes.grava_estoque(estoque)