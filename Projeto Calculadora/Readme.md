# Calculadora com SQLite e Tkinter

Este é um projeto de uma **Calculadora** feita em Python, utilizando as bibliotecas **Tkinter** para a interface gráfica e **SQLite** para armazenar o histórico das operações realizadas. A aplicação permite realizar operações matemáticas como soma, subtração, multiplicação, divisão, e cálculo de raiz quadrada (sqrt), além de manter um histórico de cálculos.

## Funcionalidades

- **Operações Básicas**: Soma, subtração, multiplicação e divisão.
- **Raiz Quadrada**: Calcula a raiz quadrada de um número inserido.
- **Histórico de Cálculos**: Armazena todas as operações realizadas em um banco de dados SQLite e exibe o histórico de cálculos realizados.
- **Armazenamento em Banco de Dados**: Usa SQLite para salvar as operações e resultados, que podem ser consultados a qualquer momento.

## Requisitos

Antes de executar o projeto, certifique-se de ter o **Python 3.x** instalado no seu sistema.

Além disso, você precisará instalar as dependências necessárias. Execute o seguinte comando para instalar as bibliotecas requeridas:

```bash
pip install tk sqlite3
```

Nota: O módulo sqlite3 já é parte da biblioteca padrão do Python, então não é necessário instalá-lo separadamente.

## Como Usar
Passo 1: Baixe o código
Baixe ou clone o repositório:

```bash
git clone https://github.com/seu-usuario/calculadora-com-sqlite-tkinter.git
```

Passo 2: Execute a aplicação
Navegue até o diretório onde o arquivo Python (calculadora.py) está localizado e execute o seguinte comando:


```bash
python calculadora.py
```

Passo 3: Interaja com a calculadora
Entrada de dados: Insira dois números nos campos de entrada (Número 1 e Número 2).
Operações: Clique nos botões de operações para somar, subtrair, multiplicar, dividir ou calcular a raiz quadrada.
Histórico: O histórico de cálculos realizados será exibido na parte inferior da interface. O histórico é salvo no banco de dados SQLite.
Resultado: O resultado de cada operação será exibido na área de "Resultado".
Função de Recarregar o Último Resultado: Você pode clicar no botão "⟳" para carregar o último resultado realizado na entrada do primeiro número.

## Estrutura do Banco de Dados
A aplicação utiliza um banco de dados SQLite chamado my_calculator.db, que contém uma tabela chamada calculations. Essa tabela armazena as seguintes informações:

id (INTEGER): Identificador único da operação.
numero1 (REAL): O primeiro número inserido.
numero2 (REAL): O segundo número inserido.
operation (TEXT): A operação realizada (ex: +, -, *, /, sqrt).
result (REAL): O resultado da operação.

## Código
O código da calculadora está estruturado da seguinte forma:

Calculadora Class: Contém toda a lógica da aplicação, incluindo a interface Tkinter, operações matemáticas, armazenamento no banco de dados e exibição do histórico.
SQLite: O banco de dados é usado para salvar as operações realizadas, utilizando a biblioteca sqlite3 do Python.
Exemplo de operação no banco de dados
Quando você realiza uma operação, como somar 2 e 3, o banco de dados armazena a seguinte entrada:

```
numero1: 2
numero2: 3
operation: +
result: 5
```

## Exemplo de Interface
A interface gráfica da calculadora consiste em:

Campos de entrada para inserir dois números.
Botões para realizar as operações básicas e a raiz quadrada.
Área de exibição do resultado.
Um histórico de cálculos anteriores, que é carregado ao iniciar a aplicação e atualizado conforme novas operações são realizadas.

## Considerações Finais
Este é um projeto simples de calculadora com Tkinter e SQLite, perfeito para quem está começando a aprender sobre interfaces gráficas em Python e também sobre como interagir com bancos de dados. O código pode ser expandido para incluir mais funcionalidades, como operações com mais números ou a adição de um sistema de login.


---

### Como utilizar:

1. **Instalar dependências**: Instale as dependências usando o comando `pip install tk sqlite3`.
2. **Rodar a aplicação**: Execute o arquivo Python `calculadora.py` com `python calculadora.py`.
3. **Funcionalidade**: Utilize a interface gráfica para realizar operações matemáticas, ver os resultados, e consultar o histórico de cálculos realizados.



