import funcoes
def pesquisa_fun(categoria, id):
    campos = {
        "Nome": "nome",
        "Telefone": "telefone",
        "Email": "email",
        "Cargo": "cargo",
        "Nascimento": "nascimento",
        "CPF": "cpf",
        "Status": "ativo"
    }

    for titulo, chave in campos.items():
        if chave == "ativo":
            if categoria[id][chave]:
                print("|::: Status: Ativo")
            else:
                print("|::: Status: Inativo")
        else:
            print(f"|::: {titulo}: {categoria[id][chave]}")
            
def dados_fun(texto=""):
    dados = {}

    campos = {
        "Nome": "nome",
        "Telefone": "telefone",
        "Email": "email",
        "Cargo": "cargo",
        "Nascimento": "nascimento",
        "CPF": "cpf"
    }

    for titulo, chave in campos.items():
        dado = input(f"|:::  {texto}{titulo}: ")
        dados[chave] = dado

    dados["ativo"] = True

    return dados
# def dados_cardap(categoria,campo_nome):