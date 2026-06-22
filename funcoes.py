import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exclusao(categoria,id):
    decisao = input("|:::   Tecle 's' Para Confirmar a Exclusão:  ").lower()
    if decisao == 's':
        del categoria[id]
        print("|:::   Exclusão Concluída!!   :::|")
    else:
        print("|:::   Exclusão Cancelada!!   :::|")

# def valida_cpf():