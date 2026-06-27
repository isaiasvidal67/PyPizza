import funcoes
# def pesquisa_fun(categoria, id):
#     campos = {
#         "Nome": "nome",
#         "Telefone": "telefone",
#         "Email": "email",
#         "Cargo": "cargo",
#         "Nascimento": "nascimento",
#         "CPF": "cpf",
#         "Status": "ativo"
#     }

#     for titulo, chave in campos.items():
#         if chave == "ativo":
#             if categoria[id][chave]:
#                 print("|::: Status: Ativo")
#             else:
#                 print("|::: Status: Inativo")
#         else:
#             print(f"|::: {titulo}: {categoria[id][chave]}")
            
def cadastrar_dados(campos, texto=""):
    dados = {}
    for titulo, chave in campos.items():
        dado = input(f"|:::  {texto}{titulo}: ")
        dados[chave] = dado
    dados["ativo"] = True
    return dados

def exibir_dados(categoria,id,campos):
    for titulo, chave in campos.items():
        if chave == "ativo":
            if categoria[id][chave]:
                print("|:::   Status: Ativo   :::|")
            else:
                print("|:::   Status: Inativo   :::|")
        elif chave == "preco":
            preco = categoria[id][chave].replace(",", ".")
            print(f"|:::   {titulo}: R$ {float(preco):.2f}   :::|")
        else:
            print(f"|:::   {titulo}: {categoria[id][chave]}   :::|")