
programa
{
    // Função compartilhada para realizar depósitos
    funcao real depositar(real saldo, real valor)
    {
        se (valor <= 0)
        {
            escreva("Erro: Depósito inválido!\n")
            retorne saldo
        }

        retorne saldo + valor
    }

    // Função compartilhada para realizar saques
    funcao real sacar(real saldo, real valor)
    {
        se (valor <= 0 ou valor > saldo)
        {
            escreva("Erro: Saque inválido!\n")
            retorne saldo
        }

        retorne saldo - valor
    }

    // Comportamento específico da poupança
    funcao real aplicar_rendimento(real saldo, real taxa)
    {
        retorne saldo + (saldo * taxa)
    }

    // Exibe os dados de uma conta
    funcao exibir_conta(
        cadeia tipo,
        inteiro numero,
        cadeia titular,
        real saldo
    )
    {
        escreva("\nTipo: ", tipo, "\n")
        escreva("Conta: ", numero, "\n")
        escreva("Titular: ", titular, "\n")
        escreva("Saldo: R$ ", saldo, "\n")
    }

    funcao inicio()
    {
        // Dados da conta corrente
        inteiro numero_corrente = 1001
        cadeia titular_corrente = "Ana Silva"
        real saldo_corrente = 1000.0
        real limite = 500.0

        // Dados da conta poupança
        inteiro numero_poupanca = 2001
        cadeia titular_poupanca = "Carlos Souza"
        real saldo_poupanca = 1500.0
        real taxa = 0.01

        escreva("=== CONTAS CADASTRADAS ===\n")

        exibir_conta(
            "Conta Corrente",
            numero_corrente,
            titular_corrente,
            saldo_corrente
        )

        exibir_conta(
            "Conta Poupança",
            numero_poupanca,
            titular_poupanca,
            saldo_poupanca
        )

        // Operações bancárias
        saldo_corrente = depositar(saldo_corrente, 200.0)
        saldo_poupanca = sacar(saldo_poupanca, 300.0)

        // Aplicando rendimento na poupança
        saldo_poupanca = aplicar_rendimento(
            saldo_poupanca,
            taxa
        )

        escreva("\n=== SALDOS ATUALIZADOS ===\n")

        exibir_conta(
            "Conta Corrente",
            numero_corrente,
            titular_corrente,
            saldo_corrente
        )

        exibir_conta(
            "Conta Poupança",
            numero_poupanca,
            titular_poupanca,
            saldo_poupanca
        )

        escreva("\nLimite da corrente: R$ ", limite, "\n")
    }
}
