import pandas as pd

lista = []
while True: 
    df = pd.read_excel("projetos/excel/aluno.xlsx", usecols='F')
    if df > 20:
        lista.append(df)
    else:
        break
print(lista)
