
programa
{
    // Deposita um valor positivo.
    funcao real depositar(real saldo, real valor)
    {
        se (valor <= 0)
        {
            escreva("Erro: depósito inválido!\n")
            retorne saldo
        }
        retorne saldo + valor
    }

    // Realiza saque em conta corrente.
    // O saldo pode ficar negativo até o limite.
    funcao real sacar_corrente(real saldo, real limite, real valor)
    {
        se (valor <= 0 ou valor > saldo + limite)
        {
            escreva("Erro: saldo e limite insuficientes!\n")
            retorne saldo
        }
        retorne saldo - valor
    }

    // Realiza saque em conta poupança.
    funcao real sacar_poupanca(real saldo, real valor)
    {
        se (valor <= 0 ou valor > saldo)
        {
            escreva("Erro: saldo insuficiente!\n")
            retorne saldo
        }
        retorne saldo - valor
    }

    // Seleciona o comportamento conforme o tipo da conta.
    funcao real sacar(inteiro tipo, real saldo, real limite, real valor)
    {
        se (tipo == 1)
        {
            retorne sacar_corrente(saldo, limite, valor)
        }
        senao se (tipo == 2)
        {
            retorne sacar_poupanca(saldo, valor)
        }

        escreva("Erro: tipo de conta inválido!\n")
        retorne saldo
    }

    // Calcula o rendimento da poupança.
    funcao real aplicar_rendimento(real saldo, real taxa)
    {
        retorne saldo + saldo * taxa
    }

    funcao inicio()
    {
        cadeia nomes[10]
        inteiro numeros[10]
        inteiro tipos[10]
        real saldos[10]
        real limites[10]
        real taxas[10]

        nomes[0] = "Ana Silva"
        nomes[1] = "Carlos Souza"
        nomes[2] = "Maria Costa"
        nomes[3] = "Pedro Lima"
        nomes[4] = "Julia Santos"
        nomes[5] = "Lucas Oliveira"
        nomes[6] = "Beatriz Rocha"
        nomes[7] = "Rafael Alves"
        nomes[8] = "Camila Ferreira"
        nomes[9] = "Bruno Mendes"

        // Inicializa as 10 contas.
        para (inteiro i = 0; i < 10; i++)
        {
            numeros[i] = 1001 + i
            saldos[i] = 1000.0

            se (i % 2 == 0)
            {
                tipos[i] = 1
                limites[i] = 500.0
                taxas[i] = 0.0
            }
            senao
            {
                tipos[i] = 2
                limites[i] = 0.0
                taxas[i] = 0.01
            }
        }

        escreva("=== CONTAS CADASTRADAS ===\n")

        para (inteiro i = 0; i < 10; i++)
        {
            escreva(
                nomes[i], " | Conta: ", numeros[i],
                " | Saldo: R$ ", saldos[i], "\n"
            )
        }

        escreva("\n=== TESTE DE POLIMORFISMO ===\n")

        // Tenta sacar R$ 1.200 de cada conta.
        para (inteiro i = 0; i < 10; i++)
        {
            real saldo_anterior = saldos[i]

            saldos[i] = sacar(
                tipos[i], saldos[i], limites[i], 1200.0
            )

            escreva(
                nomes[i], " | Saldo: R$ ", saldos[i], "\n"
            )
        }

        escreva("\n=== RENDIMENTOS ===\n")

        para (inteiro i = 0; i < 10; i++)
        {
            se (tipos[i] == 2)
            {
                saldos[i] = aplicar_rendimento(
                    saldos[i], taxas[i]
                )

                escreva(
                    nomes[i], " | Novo saldo: R$ ",
                    saldos[i], "\n"
                )
            }
        }

        escreva("\n=== TESTE DE ERRO ===\n")

        saldos[0] = sacar(
            tipos[0], saldos[0], limites[0], 100000.0
        )

        escreva("\n=== SALDOS FINAIS ===\n")

        para (inteiro i = 0; i < 10; i++)
        {
            escreva(
                nomes[i], " | R$ ", saldos[i], "\n"
            )
        }

        escreva("\nTotal de contas: 10\n")
        escreva("=== SISTEMA FINALIZADO ===\n")
    }
}
