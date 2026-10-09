
from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata que representa uma conta bancária."""

    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    def depositar(self, valor):
        """Adiciona dinheiro ao saldo."""
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        """Método que deve ser implementado pelas classes filhas."""
        pass

    def __str__(self):
        return (
            f"Conta {self.numero} | {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"numero={self.numero!r}, titular={self.titular!r}, "
            f"saldo={self.saldo!r})"
        )


class ContaCorrente(Conta):
    """Conta que permite utilizar cheque especial."""

    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        """Realiza saque usando saldo e limite disponível."""
        if valor <= 0:
            raise ValueError("O saque deve ser positivo.")

        if valor > self.saldo + self.limite:
            raise ValueError("Saldo e limite insuficientes.")

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0
            self.limite -= restante

    def __str__(self):
        return (
            f"Conta Corrente | {super().__str__()} | "
            f"Limite: R$ {self.limite:.2f}"
        )

    def __repr__(self):
        return (
            f"ContaCorrente(numero={self.numero!r}, "
            f"titular={self.titular!r}, saldo={self.saldo!r}, "
            f"limite={self.limite!r})"
        )


class ContaPoupanca(Conta):
    """Conta que permite sacar somente o saldo disponível."""

    def __init__(self, numero, titular, saldo=0, taxa=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa

    def sacar(self, valor):
        """Realiza saque sem utilizar limite adicional."""
        if valor <= 0:
            raise ValueError("O saque deve ser positivo.")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente na poupança.")

        self.saldo -= valor

    def aplicar_rendimento(self):
        """Aplica rendimento ao saldo."""
        rendimento = self.saldo * self.taxa
        self.saldo += rendimento
        return rendimento

    def __str__(self):
        return (
            f"Conta Poupança | {super().__str__()} | "
            f"Taxa: {self.taxa * 100:.1f}%"
        )

    def __repr__(self):
        return (
            f"ContaPoupanca(numero={self.numero!r}, "
            f"titular={self.titular!r}, saldo={self.saldo!r}, "
            f"taxa={self.taxa!r})"
        )


# Criando objetos de classes diferentes
contas = [
    ContaCorrente(1001, "Ana Silva", 1000, 500),
    ContaPoupanca(2001, "Carlos Souza", 1000, 0.01)
]

print("=== TESTE DE POLIMORFISMO ===")

# O mesmo método é chamado para as duas contas
for conta in contas:
    print(f"\n{conta}")

    try:
        conta.sacar(1200)
        print("Saque realizado com sucesso!")
    except ValueError as erro:
        print("Erro:", erro)

    print(f"Saldo atual: R$ {conta.saldo:.2f}")
