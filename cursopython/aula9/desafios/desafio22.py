nome = str(input("Nome digite seu nome completo:")).strip() #Remove os espaços
maiusculo = nome.upper()
minusculo = nome.lower()
quantidade_letras = len(nome.replace(' ', ''))
first_name = len(nome.split()[0])


print(f"""O seu nome em maiúsculo: {maiusculo}
O seu nome em minúsculo: {minusculo}
Quantidade de letras do seu nome: {quantidade_letras}
Quantidade de letras do primeiro nome: {first_name}""")
