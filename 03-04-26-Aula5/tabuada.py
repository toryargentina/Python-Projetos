#10/04 - 5.4 Tabuada 

"""
Peça ao usuário para digitar um número inteiro. Use um laço de repetição para exibir a
tabuada desse número de 1 a 10.
"""

# --------------------------------------------------------

# Entrada do número
numero = int(input("Digite um número inteiro: "))

# Tabuada
for i in range(1, 11):
    print(numero * i)