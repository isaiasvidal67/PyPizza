import funcoes
import cruds
import textos
def menu_funci(categoria):
    menu_fun = ''
    while menu_fun != '0':
        funcoes.limpar()
        print()
        print("|:::::::::::::::::::::::::::::|")
        print("|:::      FUNCIONÁRIOS     :::|")
        print("|:::::::::::::::::::::::::::::|")
        print("|:::   1 - Cadastrar       :::|")
        print("|:::   2 - Pesquisar       :::|")
        print("|:::   3 - Alterar         :::|")
        print("|:::   4 - Excluir         :::|")
        print("|:::   0 - Menu Principal  :::|")
        print("|:::::::::::::::::::::::::::::|")
        menu_fun = input("|:::   Escolha uma opção: ")
        print()
        if menu_fun == '1':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::       Cadastrar       :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_fun = input("|:::  Informe um Id: ")
            if id_fun not in categoria:
                categoria[id_fun] = cruds.dados_fun()
                print("|:::   Funcionário Cadastrado Com Sucesso!!!   :::|")
            else:
                print("|:::   ID Enviado Já Está Em Uso!!!   :::|")

        elif menu_fun == '2':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::       Pesquisar       :::|")
            print("|:::      Funcionário      :::|")
            print("|:::::::::::::::::::::::::::::|")
            print()
            id_fun = input("|:::   Informe o ID que deseja pesquisar: ")
            if id_fun in categoria:
                print("|:::   Funcionário Encontrado!!   :::|")
                cruds.pesquisa_fun(categoria,id_fun)
            else:
                print("|:::   Funcionário Não Encontrado!!   :::|")
        elif menu_fun == '3':
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::|")
            print("|:::     Alterar dados     :::|")
            print("|:::    do Funcionário     :::|")
            print("|:::::::::::::::::::::::::::::|")
            id_fun = input("|:::   Informe o ID do Funcionário: ")
            if id_fun in categoria:
                print("|:::   Funcionário Encontrado!!   :::|")
                cruds.pesquisa_fun(categoria, id_fun)
                print()
                print("|:::   Informe os Novos Dados: ")
                dados_novos = cruds.dados_fun("Novo ")
                dados_novos["ativo"] = categoria[id_fun]["ativo"]
                categoria[id_fun] = dados_novos
                print()
                print("|:::   Dados Alterados Com Sucesso!!!   :::|")
            else:
                print("|:::   Funcionário Não Encontrado!!   :::|")
        elif menu_fun == '4':
            menu_ex = ''
            while menu_ex != '0':
                funcoes.limpar()
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print("|:::                Excluir               :::|")
                print("|:::               Desativar              :::|")
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print()
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                print("|:::   1 - Excluir Permanentemente        :::|")
                print("|:::   2 - Desativar                      :::|")
                print("|:::   3 - Ativar                         :::|")
                print("|:::   0 - Menu Principal                 :::|")
                print("|::::::::::::::::::::::::::::::::::::::::::::|")
                menu_ex = input("|:::   Escolha uma opção: ")
                if menu_ex == '1':
                    funcoes.limpar
                    id_fun = input("|:::   Informe o ID do Funcionário: ")
                    if id_fun in categoria:
                        funcoes.exclusao(categoria, id_fun)
                    else:
                        print("|:::   Funcionário Não Encontrado!!   :::|")
                elif menu_ex == '2':
                    funcoes.limpar
                    id_fun = input("|:::   Informe o ID do Funcionário: ")
                    if id_fun in categoria:
                        funcoes.desativar(categoria, id_fun)
                    else:
                        print("|:::   Funcionário Não Encontrado!!   :::|")
                elif menu_ex == '3':
                    funcoes.limpar
                    id_fun = input("|:::   Informe o ID do Funcionário: ")
                    if id_fun in categoria:
                        funcoes.ativar(categoria, id_fun)
                    else:
                        print("|:::   Funcionário Não Encontrado!!   :::|")
                elif menu_ex == '0':
                    funcoes.limpar()
                    textos.menu()
                else:
                    print("|:::   Opção Inválida!!   :::|")
                if menu_ex != "0":
                    input("Pressione ENTER para continuar...")
        elif menu_fun == '0':
            funcoes.limpar()
            textos.menu()
        else:
            textos.invalida()
        if menu_fun != '0':
            input("Pressione ENTER para continuar...")
    return menu_fun