# 10/04 - 6.2 Fatorial

"""
Crie uma função Python para calcular o fatorial de um número fornecido pelo usuário
"""

# --------------------------------------------------------

def calcular_fatorial():
    num = int(input("Digite um número inteiro: "))
    
    if num < 0:
        print("Fatorial não existe para números negativos.")
    elif num == 0 or num == 1:
        print(f"O fatorial de {num} é 1")
    else:
        fatorial = 1
        for i in range(2, num + 1):
            fatorial *= i
        print(f"O fatorial de {num} é {fatorial}")

calcular_fatorial()