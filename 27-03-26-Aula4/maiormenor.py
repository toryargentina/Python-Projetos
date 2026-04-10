# 10/04 - 4.2 Maior ou Menor

"""
Faça um programa que leia 2 valores inteiros e imprima se o primeiro número informado é
maior ou é o menor. caso eles sejam iguais, o programa deve imprimir essa informação.
"""

# --------------------------------------------------------

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))


if num1 > num2:
    print(num1, "é maior que", num2)
elif num1 < num2:
    print(num1, "é menor que", num2)
else:
    print(num1, "e", num2, "são números iguais")