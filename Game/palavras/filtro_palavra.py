def filtrar_palavras(nome_arquivo_entrada, nome_arquivo_saida):
    """
    Lê as palavras de um arquivo de entrada, filtra as palavras que começam com 'B' e
    terminam com 'O', e salva essas palavras em um arquivo de saída.
    """
    try:
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
            palavras = arquivo_entrada.readlines()
        
        palavras_filtradas = [palavra.strip() for palavra in palavras if palavra.strip().lower().startswith('b') and palavra.strip().lower().endswith('o')]
        
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for palavra in palavras_filtradas:
                arquivo_saida.write(palavra + '\n')

        print(f"As palavras filtradas foram salvas no arquivo {nome_arquivo_saida}.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

nome_arquivo_entrada = 'entrada.txt'
nome_arquivo_saida = 'saida.txt'

filtrar_palavras(nome_arquivo_entrada, nome_arquivo_saida)
