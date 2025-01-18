import pandas as pd
import numpy as np

#variável para receber o id do arquivo google
arquivo_id = "10v33NQOtYxcf02eIRY6RTw1TA9xNhte7uoA5qrnhfYo"

#variável para receber o id da planilha
sheet_id = "gviz/tq?tqx=out:csv&gid=1626541184"

#variável para receber a planilha
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{arquivo_id}/{sheet_id}")

#print(df['Especialidade'].value_counts())
#print(df.describe())
def calcular_dias(row):
    if row['Internamento'] == 'SIM':
        return (row['Data de Alta'] - row['Data de Admissão']).days
    else:
        return None  # ou qualquer valor que você queira atribuir se não for 'SIM'

# Aplicar a função para criar a nova coluna 'dias'
df['Dias Internados'] = df.apply(calcular_dias, axis=1)


#df['Dias internação'] = np.where(df['Internamento'] == 'SIM', (df['Data de Alta']-df['Data de Admissão']), '-')



#print(df)
