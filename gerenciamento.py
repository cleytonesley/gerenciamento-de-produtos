import json

# Nome do arquivo JSON para persistência
FILE_NAME = 'inventario.json'

# Funções para carregar e salvar o inventário
def carregar_inventario(file_name=FILE_NAME):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado. Criando novo inventário.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar {file_name}. Criando novo inventário.")
        return []

def salvar_inventario(inventario, file_name=FILE_NAME):
    try:
        with open(file_name, "w") as file:
            json.dump(inventario, file, indent=4)
        print("Inventário salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o inventário: {e}")

# Gerar um ID único para o produto
def gerar_id(inventario):
    if not inventario:
        return 1
    return max(produto["id"] for produto in inventario) + 1

# Adicionar produtos
def adicionar_produto(inventario):
    print("=== Adicionar Produto ===")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    try:
        quantidade = int(input("Quantidade em Estoque: "))
        preco = float(input("Preço: "))
    except ValueError:
        print("Quantidade e preço devem ser numéricos.")
        return
    produto = {
        "id": gerar_id(inventario),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
    }
    inventario.append(produto)
    salvar_inventario(inventario)
    print("Produto adicionado com sucesso!")

# Listar produtos
def listar_produtos(inventario):
    print("=== Listar Produtos ===")
    if not inventario:
        print("Nenhum produto no inventário.")
        return
    print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Quantidade':<10} {'Preço':<10}")
    print("-" * 60)
    for produto in inventario:
        print(f"{produto['id']:<5} {produto['nome']:<20} {produto['categoria']:<15} {produto['quantidade']:<10} {produto['preco']:<10.2f}")

# Atualizar produto
def atualizar_produto(inventario):
    try:
        id_produto = int(input("Informe o ID do produto a ser atualizado: "))
    except ValueError:
        print("ID inválido.")
        return
    produto = next((p for p in inventario if p["id"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    print("Deixe o campo vazio para manter o valor atual.")
    nome = input(f"Nome ({produto['nome']}): ") or produto["nome"]
    categoria = input(f"Categoria ({produto['categoria']}): ") or produto["categoria"]
    quantidade = input(f"Quantidade ({produto['quantidade']}): ") or produto["quantidade"]
    preco = input(f"Preço ({produto['preco']}): ") or produto["preco"]
    try:
        produto["nome"] = nome
        produto["categoria"] = categoria
        produto["quantidade"] = int(quantidade)
        produto["preco"] = float(preco)
    except ValueError:
        print("Dados inválidos. Atualização cancelada.")
        return
    salvar_inventario(inventario)
    print("Produto atualizado com sucesso!")

# Excluir produto
def excluir_produto(inventario):
    try:
        id_produto = int(input("Informe o ID do produto a ser excluído: "))
    except ValueError:
        print("ID inválido.")
        return
    produto = next((p for p in inventario if p["id"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    confirmar = input(f"Confirma a exclusão do produto {produto['nome']}? (s/n): ").lower()
    if confirmar == 's':
        inventario.remove(produto)
        salvar_inventario(inventario)
        print("Produto excluído com sucesso!")
    else:
        print("Exclusão cancelada.")

# Buscar produto
def buscar_produto(inventario):
    termo = input("Informe o ID ou parte do nome do produto: ").lower()
    try:
        id_produto = int(termo)
        produto = next((p for p in inventario if p["id"] == id_produto), None)
    except ValueError:
        produto = next((p for p in inventario if termo in p["nome"].lower()), None)
    if produto:
        print("Produto encontrado:")
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: {produto['preco']:.2f}")
    else:
        print("Produto não encontrado.")

# Menu principal
def menu():
    inventario = carregar_inventario()
    while True:
        print("\n=== Menu de Gerenciamento de Inventário ===")
        print("1. Adicionar Produtos")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(inventario)
        elif opcao == "2":
            listar_produtos(inventario)
        elif opcao == "3":
            atualizar_produto(inventario)
        elif opcao == "4":
            excluir_produto(inventario)
        elif opcao == "5":
            buscar_produto(inventario)
        elif opcao == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
