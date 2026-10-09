
import re


class Cliente:
    """Representa um cliente com dados validados."""

    def __init__(self, nome, idade, email):
        """Inicializa o cliente usando as propriedades."""
        self.nome = nome
        self.idade = idade
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")

        self._nome = valor.strip()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if type(valor) is not int or not 0 <= valor <= 120:
            raise ValueError("A idade deve estar entre 0 e 120.")

        self._idade = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        padrao = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"

        if not isinstance(valor, str) or not re.fullmatch(padrao, valor):
            raise ValueError("Formato de e-mail inválido.")

        self._email = valor

    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.email}"

    def __repr__(self):
        return (
            f"Cliente(nome={self.nome!r}, "
            f"idade={self.idade!r}, email={self.email!r})"
        )


# Criando um cliente com dados válidos
cliente = Cliente("Ana Silva", 25, "ana@gmail.com")

print("=== CLIENTE CADASTRADO ===")
print(cliente)

# Alterando os dados pelas propriedades
cliente.idade = 26
print("\nIdade atualizada:", cliente.idade)

# Testando uma idade inválida
try:
    cliente.idade = -5
except ValueError as erro:
    print("\nErro:", erro)

# Testando um e-mail inválido
try:
    cliente.email = "email_invalido"
except ValueError as erro:
    print("Erro:", erro)

# Verificando se os dados válidos foram preservados
print("\n=== DADOS FINAIS ===")
print(cliente)
