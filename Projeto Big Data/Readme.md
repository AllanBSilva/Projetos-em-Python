# Projeto Big Data em Saúde

Este projeto foi desenvolvido para disciplina de BIG DATA, para analisar dados de saúde fictícios com o objetivo de gerar insights valiosos sobre pacientes, atendimentos e faturamento hospitalar. Utilizamos diversas bibliotecas do Python, como `Pandas`, `NumPy`, `Matplotlib` e `Seaborn`, para processar, visualizar e extrair informações significativas dos dados. A análise foi realizada dentro do Power BI, com a geração de gráficos interativos.

## Estrutura do Projeto

O código consiste em um processo de análise de dados de pacientes, com base em um conjunto de dados que contém informações sobre a admissão, alta, doenças, especialidades, faturamento e outros aspectos de atendimento hospitalar.

### Bibliotecas Utilizadas

- **Pandas**: Para manipulação e análise de dados em formato de tabelas (DataFrames).
- **NumPy**: Para operações numéricas e manipulação de arrays.
- **Matplotlib**: Para geração de gráficos estáticos.
- **Seaborn**: Para criação de gráficos mais complexos com uma interface de alto nível.

### Etapas de Análise

1. **Carregamento e Pré-processamento dos Dados**:
   - O dataset foi carregado de um arquivo CSV e tratamos os campos de datas e valores financeiros.
   - As datas de alta e admissão foram convertidas para o formato datetime para facilitar cálculos posteriores.
   - A coluna "Dias Internados" foi criada para calcular o tempo de internação dos pacientes.

2. **Análise de Faixa Etária**:
   - Dividimos os pacientes em faixas etárias específicas para entender a distribuição etária dos atendimentos hospitalares.
   - Foi gerado um gráfico de barras horizontais para visualizar a quantidade de atendimentos por faixa etária.

3. **Análise de Atendimento por Especialidade**:
   - Contamos a quantidade de atendimentos por especialidade para entender quais áreas mais demandam serviços médicos.
   - Um gráfico de barras foi gerado para representar essa distribuição.

4. **Análise de Faturamento por Área**:
   - Analisamos os valores financeiros dos atendimentos (consultas, exames e internações).
   - Um gráfico de pizza (ou donut) foi utilizado para mostrar a participação de cada área no faturamento total.

5. **Gráficos Interativos no Power BI**:
   - A contagem de pacientes por faixa etária foi calculada para diferentes meses, permitindo a criação de gráficos dinâmicos no Power BI.
   - Foi possível realizar uma análise interativa e segmentada, com a utilização de filtros para o mês de análise.

### Exemplos de Visualizações

#### Faixa Etária dos Pacientes

![Faixa Etária](./images/faixa_etaria.png)

#### Quantidade de Atendimentos por Especialidade

![Atendimentos por Especialidade](./images/atendimentos_especialidade.png)

#### Faturamento por Área (Consultas, Internamento e Exames)

![Faturamento por Área](./images/faturamento_areas.png)

### Como Executar o Projeto

1. Clone o repositório ou baixe os arquivos para seu ambiente local.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy matplotlib seaborn
