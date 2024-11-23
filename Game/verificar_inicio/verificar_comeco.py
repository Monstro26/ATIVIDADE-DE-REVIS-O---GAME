def verificar_inicio(texto):
    if texto.startswith("Ola"):
        print("A frase começa com 'Ola'.")
    else:
        print("A frase não começa com 'Ola'.")

frase = input("Digite uma frase: ")
verificar_inicio(frase)
