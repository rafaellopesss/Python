aluno = []

while True:
    nota = float(input('Digite a nota do aluno'))
    pergunta = int(input('Deseja adicionar mais alguma nota? [1] SIM e [2] não'))
    aluno.append(nota)
    if pergunta == 1:
        pass
    else:
        break

print(nota)