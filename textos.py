import funcoes

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

def finaliza():
    funcoes.limpar()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::   Obrigado Por Usar   :::|")
    print("|:::    O Programa!! :)    :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::     Até Mais !!  ;)   :::|")
    print("|:::::::::::::::::::::::::::::|")
    print("Fim do Programa!!!")

def encerrando():
    funcoes.limpar()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::      Encerrando       :::|")
    print("|:::     O Programa em     :::|")
    print("|:::      3...2...1...     :::|")
    print("|:::::::::::::::::::::::::::::|")
    print()

def layout_menu():
    funcoes.limpar()
    print("|' ' ' ' ' ' ' ' ' ' ' ' ' ' '|")     #Primeira versão do layout, tentei fazer uma caixa de pizza kk
    print("|:                           :|")     # OBS: Alterar os "Resps" para um identificador melhor 
    print("|:::::::::::::::::::::::::::::|")
    print("|:::::::::::::::::::::::::::::|")
    print("|:::::-------------------:::::|")
    print("|::::/                   \\::::|")
    print("|:::|   Projeto PyPizza   |:::|")
    print("|::::\\                   /::::|")
    print("|::::::-----------------::::::|")
    print("|:::::::::::::::::::::::::::::|")
    print("|:::::::::::::::::::::::::::::|")
    print("|:                           :|")
    print("|. . . . . . . . . . . . . . .|")
    print()
    print("|:::::::::::::::::::::::::::::|")
    print("|:::   1 - Funcionários    :::|")
    print("|:::   2 - Cardápio        :::|")
    print("|:::   3 - Estoque         :::|")
    print("|:::   4 - Relátorio       :::|")
    print("|:::   5 - Informações     :::|")
    print("|:::   0 - Sair            :::|")
    print("|:::::::::::::::::::::::::::::|")
    