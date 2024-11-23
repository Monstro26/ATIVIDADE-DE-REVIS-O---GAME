def somar_multiplos_de_3(nome_arquivo):
    soma = 0
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                try:
                    valor = int(linha.strip())
                    if valor % 3 == 0:
                        soma += valor
                except ValueError:
                    print(f"Valor inválido encontrado na linha: {linha.strip()}")
                    continue
        return soma
    except FileNotFoundError:
        print(f"Erro: o arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

nome_arquivo = 'valores.txt'
resultado = somar_multiplos_de_3(nome_arquivo)

if resultado is not None:
    print(f"A soma dos múltiplos de 3 é: {resultado}")
