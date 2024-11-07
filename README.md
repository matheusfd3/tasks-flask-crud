# tasks-flask-crud

Este é um projeto de uma API RESTful básica construída com Flask para gerenciar tarefas. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em tarefas, sendo ideal para estudos e como exemplo para uma estrutura simples de API. O projeto também inclui testes automatizados usando o `pytest` para garantir a qualidade e a integridade das funcionalidades implementadas.

## Funcionalidades

A API `tasks-flask-crud` oferece os seguintes endpoints para gerenciar tarefas:

- **Criar uma nova tarefa**: Adiciona uma tarefa com título e descrição.
- **Listar todas as tarefas**: Retorna uma lista de todas as tarefas.
- **Visualizar uma tarefa específica**: Retorna os detalhes de uma tarefa pelo seu ID.
- **Atualizar uma tarefa**: Permite modificar o título e/ou descrição de uma tarefa existente.
- **Deletar uma tarefa**: Remove uma tarefa pelo ID.

## Tecnologias Utilizadas

- **Flask**: Framework para criação da API.
- **Pytest**: Framework de testes para automação dos testes da API.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheusfd3/tasks-flask-crud.git
   
   cd tasks-flask-crud
   ```
2. **Instale as dependências:**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Inicie o servidor:**
    ```bash
    python run.py
    ```

## Endpoints

Você pode testar esses endpoints usando o [Postman](https://www.postman.com/) ou outra ferramenta de sua preferência.

| Método | Endpoint           | Descrição                       |
|--------|---------------------|---------------------------------|
| POST   | `/tasks`           | Cria uma nova tarefa           |
| GET    | `/tasks`           | Retorna todas as tarefas       |
| GET    | `/tasks/<id>`      | Retorna uma tarefa específica  |
| PUT    | `/tasks/<id>`      | Atualiza uma tarefa existente  |
| DELETE | `/tasks/<id>`      | Deleta uma tarefa              |

## Testes Automatizados
Os testes automatizados foram implementados com o pytest.

```bash
pytest tests.py -v
```
