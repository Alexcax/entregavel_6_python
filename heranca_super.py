
class Conta:
    """Representa uma conta bancária básica."""

    def __init__(self, numero, titular, saldo=0):
        """Inicializa os dados da conta."""
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
        """Adiciona dinheiro à conta."""
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")

        self.saldo += valor

    def sacar(self, valor):
        """Retira dinheiro da conta."""
        if valor <= 0 or valor > self.saldo:
            raise ValueError("Valor de saque inválido.")

        self.saldo -= valor

    def __str__(self):
        return (
            f"Conta: {self.numero} | "
            f"Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"Conta(numero={self.numero!r}, "
            f"titular={self.titular!r}, saldo={self.saldo!r})"
        )


class ContaCorrente(Conta):
    """Conta bancária com limite adicional."""

    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

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
    """Conta bancária que possui rendimento."""

    def __init__(self, numero, titular, saldo=0, taxa=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa

    def aplicar_rendimento(self):
        """Adiciona o rendimento ao saldo."""
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


# Criando os objetos das classes filhas
corrente = ContaCorrente(1001, "Ana Silva", 1000, 500)
poupanca = ContaPoupanca(2001, "Carlos Souza", 1500, 0.01)

print("=== CONTAS CADASTRADAS ===")
print(corrente)
print(poupanca)

# Utilizando métodos herdados da classe Conta
corrente.depositar(200)
poupanca.sacar(300)

# Utilizando um método específico da poupança
rendimento = poupanca.aplicar_rendimento()

print("\n=== OPERAÇÕES REALIZADAS ===")
print(f"Rendimento da poupança: R$ {rendimento:.2f}")
print(corrente)
print(poupanca)
