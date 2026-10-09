
# Classe que representa um cliente do banco
class Cliente:
    """Armazena as informações de um cliente."""

    def __init__(self, nome, idade, email):
        """Inicializa os dados do cliente."""
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        """Retorna uma descrição amigável do cliente."""
        return f"Cliente: {self.nome} | Idade: {self.idade}"

    def __repr__(self):
        """Retorna a representação técnica do objeto."""
        return (
            f"Cliente(nome={self.nome!r}, "
            f"idade={self.idade!r}, email={self.email!r})"
        )


# Criando três objetos da classe Cliente
cliente1 = Cliente("Ana Silva", 25, "ana@gmail.com")
cliente2 = Cliente("Carlos Souza", 30, "carlos@gmail.com")
cliente3 = Cliente("Maria Costa", 22, "maria@gmail.com")

# Exibindo os clientes
print("=== CLIENTES CADASTRADOS ===")
print(cliente1)
print(cliente2)
print(cliente3)

# Demonstrando o método __repr__
print("\n=== REPRESENTAÇÃO DO OBJETO ===")
print(repr(cliente1))
