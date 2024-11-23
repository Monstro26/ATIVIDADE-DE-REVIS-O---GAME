from pacote.verificar_par import verificar_par
from pacote.multiplicar import multiplicar
from pacote.subtrair import subtrair

numero = 4
print(f"O número {numero} é par? {verificar_par(numero)}")

a = 5
b = 3
print(f"A multiplicação de {a} e {b} é {multiplicar(a, b)}")

print(f"A subtração de {a} e {b} é {subtrair(a, b)}")
