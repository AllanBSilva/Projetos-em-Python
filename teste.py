import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#variável para receber a planilha
dataset = pd.read_csv('Tabela_de_dados.csv', encoding='iso-8859-1', sep=';', decimal=',')

dataset['Data de Alta'] = pd.to_datetime(dataset['Data de Alta'], dayfirst=True)
dataset['Data de Admissão'] = pd.to_datetime(dataset['Data de Admissão'], dayfirst=True)

# Função calcular quantidade de dias internados
def calcular_dias(row):
    if row['Internamento'] == 'SIM':
        return (row['Data de Alta'] - row['Data de Admissão']).days
    else:
        return 0  # ou qualquer valor que você queira atribuir se não for 'SIM'

# Aplicar a função para criar a nova coluna 'Dias Internados'
dataset['Dias Internados'] = dataset.apply(calcular_dias, axis=1)

#print(dataset['Especialidade'].value_counts().head(5))
#print(dataset['Doença'].value_counts().head(5))
#print(dataset['Idade'].describe())
#print(contagem_faixa_etaria)
#print(dataset)

# Definir os limites das faixas etárias
limites_faixas_etarias = [0, 21, 41, 61, 81, float('inf')]  # Infinito para representar a última faixa
# Rotular as faixas etárias
rotulos_faixas_etarias = ['0-20', '21-40', '41-60', '61-80', '81+']
# Usar pd.cut para dividir os valores da coluna 'Idade' em faixas e contar a ocorrência de cada faixa
contagem_faixa_etaria = pd.cut(dataset['Idade'], bins=limites_faixas_etarias, labels=rotulos_faixas_etarias, right=False).value_counts().sort_index()
#contagem_faixa_etaria = pd.cut(dataset['Idade'], bins=limites_faixas_etarias, labels=rotulos_faixas_etarias, right=False).value_counts()


# Gráfico faixa etária de atendimento
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
plt.barh(contagem_faixa_etaria.index, contagem_faixa_etaria.values, color='skyblue')
plt.title('Faixa etária dos paciente')
plt.xlabel('Quantidade de atendimentos')
plt.ylabel('Grupo por idade')
plt.gca().invert_yaxis()  # Invert y-axis to start with the largest group at the top
plt.show()

limites_faixas_etarias = [0, 21, 41, 61, 81, float('inf')]  # Infinito para representar a última faixa
# Rotular as faixas etárias
rotulos_faixas_etarias = ['0-20', '21-40', '41-60', '61-80', '81+']

# Usar pd.cut para dividir os valores da coluna 'Data de Admissão' em faixas e contar a ocorrência de cada faixa
contagem_faixa_etaria = pd.cut(dataset['Data de Admissão'], bins=limites_faixas_etarias, labels=rotulos_faixas_etarias, right=False).value_counts()

# Gráfico faixa etária de atendimento
plt.figure(figsize=(8, 6))  # Ajustar o tamanho da figura conforme necessário
plt.barh(contagem_faixa_etaria.index, contagem_faixa_etaria.values, color='skyblue')
plt.title('Quantidade de pacientes por faixa etária')
plt.xlabel('Quantidade de pacientes')
plt.ylabel('Faixa etária')
plt.gca().invert_yaxis()  # Inverter o eixo y para começar com o maior grupo no topo
plt.show()


# Função para calcular a contagem de pacientes por faixa etária no mês especificado
def contar_pacientes_por_faixa_etaria(mes_desejado):
    # Filtrar o dataset para incluir apenas os pacientes admitidos no mês desejado
    dataset_filtrado = dataset[dataset['Data de Admissão'].dt.month == mes_desejado]
    
    # Calcular a quantidade de pacientes com base na quantidade de linhas na coluna 'Data de Admissão' do mês desejado
    quantidade_pacientes = len(dataset_filtrado)
    
    # Definir os limites das faixas etárias com base na quantidade de pacientes
    quantidade_por_faixa_etaria = quantidade_pacientes // 5  # Dividir o total de pacientes em 5 faixas
    
    # Definir os limites das faixas etárias com base na quantidade por faixa etária
    limites_faixas_etarias = [0] + [quantidade_por_faixa_etaria * (i + 1) for i in range(4)] + [float('inf')]  # Infinito para representar a última faixa
    # Rotular as faixas etárias
    rotulos_faixas_etarias = ['0-20', '21-40', '41-60', '61-80', '81+']
    
    # Usar pd.cut para dividir os valores da coluna 'Idade' em faixas e contar a ocorrência de cada faixa
    contagem_faixa_etaria = pd.cut(dataset_filtrado['Idade'], bins=limites_faixas_etarias, labels=rotulos_faixas_etarias, right=False).value_counts()
    
    return contagem_faixa_etaria

# Mês desejado (será fornecido pela caixa de segmentação do Power BI)
mes_desejado = 3  # Exemplo de mês desejado (maio)

# Calcular a contagem de pacientes por faixa etária no mês especificado
contagem_faixa_etaria = contar_pacientes_por_faixa_etaria(mes_desejado)

# Gráfico faixa etária de atendimento
plt.figure(figsize=(8, 6))  # Ajustar o tamanho da figura conforme necessário
plt.barh(contagem_faixa_etaria.index, contagem_faixa_etaria.values, color='skyblue')
plt.title(f'Quantidade de pacientes por faixa etária no mês {mes_desejado}')
plt.xlabel('Quantidade de pacientes')
plt.ylabel('Faixa etária')
plt.gca().invert_yaxis()  # Inverter o eixo y para começar com o maior grupo no topo
plt.show()



# Gráfico quantidade de atendimentos por setor 
specialty_counts = dataset['Especialidade'].value_counts()
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
specialty_counts.plot(kind='bar', color='skyblue')
plt.title('Quantidade de atendimentos por setor')
plt.xlabel('Especialidade')
plt.ylabel('Número de atendimentos')
plt.xticks(rotation=45, ha='right')  # Rotate x-labels for better visibility
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


# Plotting the donut chart
totals = [float(dataset['Valor do Internamento'].sum()), float(dataset['Valor Consulta'].sum()), float(dataset['Valor Exames'].sum())]

# Plotting the donut chart
plt.figure(figsize=(8, 8))  # Set the figure size (square for a circular appearance)
plt.pie(totals, labels=['Consultas', 'Internamento', 'Exames'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'], wedgeprops={'edgecolor': 'gray'})
plt.title('Faturamento por área', fontsize=16, fontweight='bold')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()


# Verificar se as colunas existem e se os dados nelas são numéricos
numeric_cols = ['Valor do Internamento', 'Valor Consulta', 'Valor Exames']
if all(dataset[col].dtype.kind in 'fi' for col in numeric_cols):
    # Substituir valores NaN por zero de forma mais explícita
    dataset[numeric_cols] = dataset[numeric_cols].fillna(0)
    
    # Calcular os totais para o gráfico de pizza
    totals = [float(dataset['Valor Consulta'].sum()), float(dataset['Valor do Internamento'].sum()), float(dataset['Valor Exames'].sum())]

    # Plotar o gráfico de pizza
    plt.figure(figsize=(8, 8))  # Definir o tamanho da figura
    plt.pie(totals, labels=['Consultas', 'Internamento', 'Exames'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'], wedgeprops={'edgecolor': 'gray'})
    plt.title('Faturamento por área')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
else:
    print("Algumas colunas não contêm dados numéricos.")


# Função para formatar valores monetários
def format_currency(value):
    return f'R$ {value:,.0f}'.replace(',', '.')

# Verificar se as colunas existem e se os dados nelas são numéricos
numeric_cols = ['Valor do Internamento', 'Valor Consulta', 'Valor Exames']
if all(dataset[col].dtype.kind in 'fi' for col in numeric_cols):
    # Substituir valores NaN por zero de forma mais explícita
    dataset[numeric_cols] = dataset[numeric_cols].fillna(0)
    
    # Calcular os totais para o gráfico de pizza
    totals = [float(dataset['Valor Consulta'].sum()), float(dataset['Valor do Internamento'].sum()), float(dataset['Valor Exames'].sum())]

    # Formatando os rótulos em formato monetário (R$)
    labels = [f'Consultas\nTotal: {format_currency(totals[0])}',
              f'Internamento\nTotal: {format_currency(totals[1])}',
              f'Exames\nTotal: {format_currency(totals[2])}']

    # Plotar o gráfico de pizza
    plt.figure(figsize=(8, 8))  # Definir o tamanho da figura
    plt.pie(totals, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'], wedgeprops={'edgecolor': 'gray'})
    plt.title('Faturamento por área', fontsize=30, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
else:
    print("Algumas colunas não contêm dados numéricos.")