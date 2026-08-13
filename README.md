# API Connect

API REST desenvolvida como MVP para gerenciamento de usuários, implementando as operações CRUD completas (Create, Read, Update, Delete) com validação de entrada e padronização de respostas em JSON.

## 🛠️ Tecnologias

- **Python 3**
- **Flask** — microframework web
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **flask-cors** — habilitação de CORS

## 📁 Estrutura do projeto

api-connect/
├── app.py # Ponto de entrada da aplicação
├── requirements.txt # Dependências do projeto
├── routes/
│ └── user_routes.py # Definição dos endpoints HTTP
├── controllers/
│ └── user_controller.py # Lógica de negócio e validações
└── models/
└── user_model.py # Persistência em memória e geração de IDs

## ⚙️ Como rodar o projeto

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/api-connect.git
cd api-connect

# Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# Instalar as dependências
pip install -r requirements.txt

# Rodar o servidor
python app.py
```

O servidor sobe em `http://localhost:5000`.

## 📌 Endpoints disponíveis

| Método | Rota | Descrição | Status de sucesso |
|--------|------|-----------|--------------------|
| POST | `/users` | Cria um novo usuário | 201 |
| GET | `/users` | Lista todos os usuários | 200 |
| GET | `/users/:id` | Busca um usuário pelo ID | 200 |
| PUT | `/users/:id` | Atualiza um usuário existente | 200 |
| DELETE | `/users/:id` | Remove um usuário | 204 |

## 📨 Padrão de resposta

Todas as respostas seguem um envelope padronizado:

**Sucesso:**
```json
{
  "data": {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@email.com"
  }
}
```

**Erro:**
```json
{
  "error": "O campo 'email' é obrigatório"
}
```

## 🔍 Exemplos de uso

### Criar usuário
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@email.com"}'
```
**Resposta (201):**
```json
{"data": {"id": 1, "nome": "João Silva", "email": "joao@email.com"}}
```

### Listar usuários
```bash
curl -X GET http://localhost:5000/users
```
**Resposta (200):**
```json
{"data": [{"id": 1, "nome": "João Silva", "email": "joao@email.com"}]}
```

### Buscar usuário por ID
```bash
curl -X GET http://localhost:5000/users/1
```

### Atualizar usuário
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Souza"}'
```

### Remover usuário
```bash
curl -X DELETE http://localhost:5000/users/1
```
**Resposta:** `204 No Content`

## ⚠️ Validações

- Os campos `nome` e `email` são obrigatórios na criação de um usuário — sua ausência retorna **400 (Bad Request)**.
- A busca, atualização ou remoção de um ID inexistente retorna **404 (Not Found)**.

## 👤 Autor

Vinicius
