
def criar_arquivo(nome_arquivo, conteudo):

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"O conteúdo foi escrito com sucesso no arquivo {nome_arquivo}.")

nome_arquivo = input("Digite o nome do arquivo (com .txt): ")
conteudo = input("Digite o conteúdo que deseja escrever no arquivo: ")

criar_arquivo(nome_arquivo, conteudo)
