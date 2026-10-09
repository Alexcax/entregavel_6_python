
from abc import ABC, abstractmethod
import re


class Cliente:
    """Representa um cliente do banco."""

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("Nome inválido.")
        self._nome = valor.strip()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if type(valor) is not int or not 0 <= valor <= 120:
            raise ValueError("Idade inválida.")
        self._idade = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        padrao = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"
        if not isinstance(valor, str) or not re.fullmatch(padrao, valor):
            raise ValueError("E-mail inválido.")
        self._email = valor

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

    def __repr__(self):
        return f"Cliente({self.nome!r}, {self.idade!r}, {self.email!r})"


class Conta(ABC):
    """Classe abstrata para contas bancárias."""

    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if type(valor) is not int or valor <= 0:
            raise ValueError("Número da conta inválido.")
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not isinstance(valor, Cliente):
            raise TypeError("O titular deve ser um Cliente.")
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if type(valor) not in (int, float) or not 0 <= valor < float("inf"):
            raise ValueError("Saldo inválido.")
        self._saldo = round(valor, 2)

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if type(valor) not in (int, float) or not 0 < valor < float("inf"):
            raise ValueError("Depósito inválido.")
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        """Define o saque obrigatório das subclasses."""
        pass

    def __str__(self):
        return f"Conta {self.numero} | {self.titular.nome} | R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"{type(self).__name__}({self.numero!r}, {self.saldo!r})"


class ContaCorrente(Conta):
    """Conta que possui limite de cheque especial."""

    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if type(valor) not in (int, float) or not 0 <= valor < float("inf"):
            raise ValueError("Limite inválido.")
        self._limite = round(valor, 2)

    def sacar(self, valor):
        """Realiza saque usando saldo e limite."""
        if type(valor) not in (int, float) or not 0 < valor < float("inf"):
            raise ValueError("Saque inválido.")
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo e limite insuficientes.")

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0
            self.limite -= restante

    def __str__(self):
        return f"Corrente | {super().__str__()} | Limite: R$ {self.limite:.2f}"

    def __repr__(self):
        return f"ContaCorrente({self.numero!r}, {self.saldo!r}, {self.limite!r})"


class ContaPoupanca(Conta):
    """Conta que recebe rendimentos."""

    def __init__(self, numero, titular, saldo=0, taxa=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, valor):
        if type(valor) not in (int, float) or not 0 <= valor <= 1:
            raise ValueError("Taxa inválida.")
        self._taxa = valor

    def sacar(self, valor):
        """Realiza saque sem permitir saldo negativo."""
        if type(valor) not in (int, float) or not 0 < valor < float("inf"):
            raise ValueError("Saque inválido.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor

    def aplicar_rendimento(self):
        """Aplica o rendimento ao saldo."""
        rendimento = round(self.saldo * self.taxa, 2)
        self.saldo += rendimento
        return rendimento

    def __str__(self):
        return f"Poupança | {super().__str__()} | Taxa: {self.taxa * 100:.1f}%"

    def __repr__(self):
        return f"ContaPoupanca({self.numero!r}, {self.saldo!r}, {self.taxa!r})"


def main():
    """Cria os objetos e demonstra o funcionamento do sistema."""
    nomes = [
        "Ana Silva", "Carlos Souza", "Maria Costa",
        "Pedro Lima", "Julia Santos", "Lucas Oliveira",
        "Beatriz Rocha", "Rafael Alves",
        "Camila Ferreira", "Bruno Mendes"
    ]

    clientes = [
        Cliente(nome, 20 + i, f"cliente{i + 1}@gmail.com")
        for i, nome in enumerate(nomes)
    ]

    contas = []
    for i, cliente in enumerate(clientes):
        if i % 2 == 0:
            conta = ContaCorrente(1001 + i, cliente, 1000, 500)
        else:
            conta = ContaPoupanca(1001 + i, cliente, 1000, 0.01)
        contas.append(conta)

    print("=== CONTAS CADASTRADAS ===")
    for conta in contas:
        print(conta)

    print("\n=== TESTE DE POLIMORFISMO ===")
    for conta in contas:
        try:
            conta.sacar(1200)
            print(f"{conta.titular.nome}: saque realizado.")
        except ValueError as erro:
            print(f"{conta.titular.nome}: {erro}")

    print("\n=== RENDIMENTOS ===")
    for conta in contas:
        if isinstance(conta, ContaPoupanca):
            rendimento = conta.aplicar_rendimento()
            print(f"{conta.titular.nome}: R$ {rendimento:.2f}")

    print("\n=== TESTES DE EXCEÇÕES ===")
    testes = [
        lambda: Cliente("A", -5, "email"),
        lambda: contas[0].depositar(-100),
        lambda: contas[0].sacar(100000),
        lambda: setattr(contas[0], "saldo", -50),
        lambda: setattr(contas[0], "limite", -10),
        lambda: Conta(9999, clientes[0])
    ]

    for teste in testes:
        try:
            teste()
        except (ValueError, TypeError) as erro:
            print("Erro tratado:", erro)

    print("\n=== SALDOS FINAIS ===")
    for conta in contas:
        print(conta)

    print(f"\nTotal: {len(clientes)} clientes e {len(contas)} contas.")


if __name__ == "__main__":
    main()
