# 10/04 - 6.1 Raízes

"""
Escreva um programa que imprima uma tabela das raízes quadradas dos números entre 1 e 100,
com incrementos de 10.
Requisito: Utilize a biblioteca math.
"""

# --------------------------------------------------------

import math

print("Número | Raiz Quadrada")
print("-" * 22)

for i in range(1, 101, 10):
    raiz = math.sqrt(i)
    print(f"{i:<6} | {raiz:.4f}")