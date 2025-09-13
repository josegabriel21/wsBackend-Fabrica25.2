# API de Gerenciamento para Padaria

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2%2B-darkgreen?style=for-the-badge&logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-3.14%2B-red?style=for-the-badge)

## 📝 Descrição do Projeto

Este projeto é uma API RESTful desenvolvida em Django e Django REST Framework. A API simula o backend de um sistema de gerenciamento para uma padaria, permitindo o controle de categorias e produtos em estoque.

Este projeto foi construído para atender a um conjunto de requisitos específicos, incluindo a implementação de um CRUD completo, o relacionamento entre entidades e o consumo de uma API externa.

## ✨ Funcionalidades

- ✅ **CRUD completo para Categorias**: Crie, visualize, atualize e delete categorias de produtos (ex: Pães, Bolos, Doces).
- ✅ **CRUD completo para Produtos**: Gerencie produtos, associando cada um a uma categoria e controlando informações como preço e estoque.
- ✅ **Relacionamento de Dados**: Implementação de uma relação Muitos-para-Um entre Produtos e Categorias.
- ✅ **Validação de Dados**: Regras de negócio como a proibição de categorias com nomes duplicados.
- ✅ **Consumo de API Externa**: Um endpoint dedicado para buscar receitas em uma API pública (`TheMealDB`).
- ✅ **API Navegável**: Interface amigável para testes e interação com a API, gerada pelo DRF.

## 🛠️ Tecnologias Utilizadas

- **Backend:**
  - [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
  - [Django REST Framework](https://www.django-rest-framework.org/)
- **Banco de Dados:**
  - SQLite3 (configuração padrão do Django para desenvolvimento)

## 🚀 Setup e Instalação Local

Siga os passos abaixo para executar o projeto em sua máquina.

**1. Clone o repositório:**
```bash
git clone <URL-do-seu-repositorio-github>
cd <nome-da-pasta-do-projeto>
```

**2. Crie e ative um ambiente virtual:**
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Aplique as migrações do banco de dados:**
```bash
python manage.py migrate
```

**5. Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

## 📚 Documentação da API

A URL base para todos os endpoints é `/api/`.

### Endpoints de Categorias
| Endpoint | Método HTTP | Descrição |
| :--- | :--- | :--- |
| `/api/categorias/` | `GET`, `POST` | Lista todas as categorias ou cria uma nova. |
| `/api/categorias/{id}/`| `GET`, `PUT`, `DELETE` | Busca, atualiza ou deleta uma categoria específica. |

### Endpoints de Produtos
| Endpoint | Método HTTP | Descrição |
| :--- | :--- | :--- |
| `/api/produtos/` | `GET`, `POST` | Lista todos os produtos ou cria um novo. |
| `/api/produtos/{id}/` | `GET`, `PUT`, `DELETE`| Busca, atualiza ou deleta um produto específico. |

### Endpoint de Receitas (API Externa)
| Endpoint | Método HTTP | Descrição |
| :--- | :--- | :--- |
| `/api/receitas/buscar/` | `GET` | Busca receitas na API externa `TheMealDB`. |

**Exemplo de uso:** `http://127.0.0.1:8000/api/receitas/buscar/?q=bread`

