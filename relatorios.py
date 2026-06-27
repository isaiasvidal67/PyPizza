import funcoes
import cruds
import textos
campos_funcionarios = {
    "Nome": "nome",
    "Telefone": "telefone",
    "Email": "email",
    "Cargo": "cargo",
    "Nascimento": "nascimento",
    "CPF": "cpf"
}

campos_exibir_funcionarios = {
    "Nome": "nome",
    "Telefone": "telefone",
    "Email": "email",
    "Cargo": "cargo",
    "Nascimento": "nascimento",
    "CPF": "cpf",
    "Status": "ativo"
    }

def menu_relatorio(funcionarios,cardapio,estoque):
    menu_rlt = ''
    while menu_rlt != "0":
      funcoes.limpar()
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
      menu_rlt = input("|:::   Escolha uma opção: ")#
      if menu_rlt == '1':
        mn_f = ''
        while mn_f != "0":
            funcoes.limpar()
            print("|:::::::::::::::::::::::::::::::::::::::::::::|")
            print("|:::             FUNCIONARIOS              :::|")
            print("|:::::::::::::::::::::::::::::::::::::::::::::|")
            print("|:::    1 - Lista Geral                    :::|")
            print("|:::    2 - Total de Funcionarios Ativos   :::|")
            print("|:::    3 - Total de Funcionários Inativos :::|")
            print("|:::    4 - Quantidade por Cargo           :::|")
            # print("|:::    5 - Aniversariantes                :::|")
            print("|:::    0 - Menu Principal                 :::|") 
            print("|:::::::::::::::::::::::::::::::::::::::::::::|")
            mn_f = input("|:::   Escolha uma opção:")
            if mn_f == '1':
               funcoes.limpar()
               for id_fun, funcionario in sorted(funcionarios.items(),
                   key=lambda item: item[1]["nome"]                              ):
                  cruds.exibir_dados(funcionarios,id_fun,campos_funcionarios)
                  print("----------------------------------------------")
            elif mn_f == '2':
               for id_fun, funcionario in sorted(funcionarios.items(),
                   key=lambda item: item[1]["nome"]):
                  if funcionario['ativo'] == True:
                     cruds.exibir_dados(funcionarios,id_fun,campos_exibir_funcionarios)
                     print("----------------------------------------------")
            elif mn_f == '3':
               for id_fun, funcionario in sorted(funcionarios.items(),
                   key=lambda item: item[1]["nome"]):
                  if funcionario['ativo'] == False:
                     cruds.exibir_dados(funcionarios,id_fun,campos_exibir_funcionarios)
                     print("----------------------------------------------")
            elif mn_f == '4':
               funcoes.limpar()
               cargos = {}
               for funcionario in funcionarios.values():
                  cargo = funcionario['cargo']

                  if cargo not in cargos:
                     cargos[cargo] = 1
                  else:
                     cargos[cargo] += 1
               for cargo, quantidade in cargos.items():
                  print(f"{cargo}: {quantidade}")
            elif mn_f == '0':
               print()
            else:
               print()
            if mn_f != "0":
               input('Tecle ENTER')
