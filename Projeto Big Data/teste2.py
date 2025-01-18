import pandas as pd
import matplotlib.pyplot as plt

# URL do arquivo CSV no Google Sheets
url = "https://docs.google.com/spreadsheets/d/10v33NQOtYxcf02eIRY6RTw1TA9xNhte7uoA5qrnhfYo/gviz/tq?tqx=out:csv&gid=1626541184"

# Ler o arquivo CSV diretamente da URL especificando o separador de colunas
dataset = pd.read_csv(url, sep=',')

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
    plt.title('Faturamento por área', fontsize=30, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
else:
    print("Algumas colunas não contêm dados numéricos.")
