import contatos_utilis

try:
    #contatos = contatos_utilis.csv_contact("contatos.csv")
    #contatos_utilis.contatos_para_pickle(contatos, "contatos.p")

    #contatos = contatos_utilis.pickle_para_contatos("contatos.p")
    #contatos_utilis.contatos_para_json(contatos, "contatos.json")

    contatos = contatos_utilis.json_para_contatos("contatos.json")
    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
        
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para criar um arquivo")
