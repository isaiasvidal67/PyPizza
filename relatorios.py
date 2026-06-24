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