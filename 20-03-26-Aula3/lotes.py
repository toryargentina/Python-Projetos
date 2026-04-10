# 20/03 - 3.3 Lotes

"""
Implemente um programa que determine a Quantidade de Lotes de uma ação que um investidor
pode comprar com um determinado saldo. O usuário deve informar o Saldo Total disponível
e o Preço da Cota. O programa deve exibir apenas o número inteiro de cotas que podem ser
adquiridas e o valor que sobrará de troco (saldo remanescente).
"""

# --------------------------------------------------------

capital = float(input("Digite o valor do capital\n"))
valor_cota = float(input("Digite o valor da cota\n"))

print("Número de Ações=")
print(capital // valor_cota)

print("Troco")
print(capital % valor_cota)