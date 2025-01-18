# Flask Todo List App

Este é um projeto simples de lista de tarefas (To-Do List) utilizando Flask, SQLAlchemy e SQLite. A aplicação permite que o usuário adicione, marque como concluída e exclua tarefas de forma interativa. As tarefas são armazenadas em um banco de dados SQLite local.

## Funcionalidades

- **Adicionar Tarefa**: Permite que o usuário adicione uma nova tarefa à lista.
- **Marcar como Concluída**: O usuário pode marcar ou desmarcar uma tarefa como concluída.
- **Excluir Tarefa**: Permite excluir uma tarefa da lista.
- **Exibição de Tarefas**: A lista de tarefas é exibida na página principal.

## Tecnologias Utilizadas

- **Flask**: Micro framework web para Python.
- **SQLAlchemy**: ORM (Object-Relational Mapper) utilizado para interagir com o banco de dados SQLite.
- **SQLite**: Banco de dados local utilizado para armazenar as tarefas.


- **app.py**: Arquivo principal da aplicação Flask. Define as rotas e a lógica de controle.
- **models.py**: Define o modelo da tabela `Task` e configura o banco de dados com SQLAlchemy.
- **index.html**: Template HTML utilizado para renderizar as tarefas na interface do usuário.
