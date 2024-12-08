import os

aluno = []

nome = str(input('Digite o nome do aluno: '))
while True:
    nota = float(input(f'Digite a nota do {nome}: '))
    pergunta = int(input('Deseja adicionar mais alguma nota? [1] SIM e [2] não '))
    aluno.append(nota)
    if pergunta == 1:
        pass
        os.system("cls")
    else:
        break

media =  sum(aluno) / len(aluno)

print(f"A média do aluno [{nome}] é [{media}]")