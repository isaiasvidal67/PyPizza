import funcoes
def pesquisa_fun(categoria,id):
    print("|:::   Funcionário Encontrado!!   :::|")
    campos = ["Nome", "Telefone", "Email", "Cargo", "Nascimento", "CPF"]
    for i in range(len(campos)):
        print(f"|::: {campos[i]}: {categoria[id][i]}")
def dados_fun(texto=""):
    dados = []
    campos = ["Nome", "Telefone", "Email", "Cargo", "Nascimento", "CPF"]

    for i in campos:
        dado = input(f"|:::  {texto}{i}: ")
        dados.append(dado)
    return dados