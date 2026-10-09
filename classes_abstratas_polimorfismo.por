
programa
{
    // Saque de conta corrente
    funcao real sacar_corrente(
        real saldo,
        real limite,
        real valor
    )
    {
        se (valor <= 0 ou valor > saldo + limite)
        {
            escreva("Erro: Saldo e limite insuficientes!\n")
            retorne saldo
        }

        escreva("Saque autorizado na conta corrente!\n")
        retorne saldo - valor
    }

    // Saque de conta poupança
    funcao real sacar_poupanca(real saldo, real valor)
    {
        se (valor <= 0 ou valor > saldo)
        {
            escreva("Erro: Saldo insuficiente na poupança!\n")
            retorne saldo
        }

        escreva("Saque autorizado na poupança!\n")
        retorne saldo - valor
    }

    // Simula o polimorfismo selecionando o tipo de conta
    funcao real sacar(
        inteiro tipo,
        real saldo,
        real limite,
        real valor
    )
    {
        se (tipo == 1)
        {
            retorne sacar_corrente(saldo, limite, valor)
        }
        senao se (tipo == 2)
        {
            retorne sacar_poupanca(saldo, valor)
        }

        escreva("Erro: Tipo de conta inválido!\n")
        retorne saldo
    }

    funcao inicio()
    {
        cadeia titulares[2]
        inteiro tipos[2]
        real saldos[2]
        real limites[2]

        titulares[0] = "Ana Silva"
        tipos[0] = 1
        saldos[0] = 1000.0
        limites[0] = 500.0

        titulares[1] = "Carlos Souza"
        tipos[1] = 2
        saldos[1] = 1000.0
        limites[1] = 0.0

        escreva("=== TESTE DE POLIMORFISMO ===\n")

        para (inteiro i = 0; i < 2; i++)
        {
            escreva("\nTitular: ", titulares[i], "\n")

            saldos[i] = sacar(
                tipos[i],
                saldos[i],
                limites[i],
                1200.0
            )

            escreva("Saldo após operação: R$ ", saldos[i], "\n")
        }
    }
}
