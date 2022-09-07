arquivo1 = open("contato-escrita.csv", encoding="latin", mode="w")
arquivo2 = open("contato-escrita.csv", encoding="latin", mode="w")

contato_carol = "11,Carol,carol@carol.com.br\n"
contato_andreza = "12,Andreza,andreza@andreza.com.br\n"

arquivo1.write(contato_carol)
arquivo2.write(contato_andreza)

arquivo1.close()
arquivo2.close()
