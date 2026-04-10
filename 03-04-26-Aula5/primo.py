#10/04 - 5.5 Primo

"""
Peça ao usuário para digitar um número inteiro positivo. Use um laço para verificar se
o número é primo. Um número primo é divisível apenas por 1 e por ele mesmo
"""

# --------------------------------------------------------

numero = int(input("Digite um número inteiro positivo: "))

primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("É primo")
else:
    print("Não é primo")