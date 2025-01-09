# Gerenciamento de Inventário (CRUD)

Este projeto é uma aplicação simples em Python que permite gerenciar um inventário de produtos utilizando operações CRUD ( **C**reate, **R**ead, **U**pdate, **D**elete). O inventário é armazenado em um arquivo JSON para garantir a persistência dos dados.

## Funcionalidades

1. **Adicionar Produtos (Create):**
   - Permite adicionar novos produtos ao inventário, especificando nome, categoria, quantidade e preço.

2. **Listar Produtos (Read):**
   - Exibe todos os produtos do inventário em um formato organizado.

3. **Buscar Produto (Read):**
   - Permite localizar produtos por ID ou parte do nome.

4. **Atualizar Produtos (Update):**
   - Permite alterar as informações de um produto existente.

5. **Excluir Produto (Delete):**
   - Permite remover um produto do inventário com base no ID.

## Como Usar

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/usuario/gerenciamento-inventario.git
   cd gerenciamento-inventario
   ```

2. **Executar o Programa**
   Certifique-se de ter o Python instalado e execute o arquivo principal:
   ```bash
   python gerenciamento.py
   ```

3. **Interagir com o Menu**
   Escolha uma das opções no menu para realizar operações no inventário.

## Estrutura do Arquivo JSON

O arquivo `inventario.json` será criado automaticamente caso não exista. Ele segue o seguinte formato:
```json
[
    {
        "id": 1,
        "nome": "Cadeira Gamer",
        "categoria": "Móveis",
        "quantidade": 10,
        "preco": 500.0
    }
]
```

## Requisitos

- Python 3.6 ou superior

## Melhorias Futuras

- Integração com um banco de dados (SQLite ou PostgreSQL).
- Interface gráfica para facilitar a utilização.
- Validação mais robusta de entradas do usuário.

---
**Desenvolvido por:** Seu Nome

