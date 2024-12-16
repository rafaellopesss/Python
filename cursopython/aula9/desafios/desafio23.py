numero = str(input('Digite um número:')).strip()

#1000


unidade = numero[-1]
dezena = numero[2]
centena = numero[1]
milhar= numero[0]

print(f"""Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}""")