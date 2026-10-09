
programa
{
    // Exibe os dados de um cliente
    funcao exibir_cliente(cadeia nome, inteiro idade)
    {
        escreva("Cliente: ", nome, " | Idade: ", idade, "\n")
    }

    funcao inicio()
    {
        // Vetores que armazenam os dados dos clientes
        cadeia nomes[3]
        inteiro idades[3]
        cadeia emails[3]

        // Cadastro dos clientes
        nomes[0] = "Ana Silva"
        idades[0] = 25
        emails[0] = "ana@gmail.com"

        nomes[1] = "Carlos Souza"
        idades[1] = 30
        emails[1] = "carlos@gmail.com"

        nomes[2] = "Maria Costa"
        idades[2] = 22
        emails[2] = "maria@gmail.com"

        escreva("=== CLIENTES CADASTRADOS ===\n")

        // Exibe os clientes cadastrados
        para (inteiro i = 0; i < 3; i++)
        {
            exibir_cliente(nomes[i], idades[i])
        }

        escreva("\n=== DADOS COMPLETOS ===\n")
        escreva("Nome: ", nomes[0], "\n")
        escreva("Idade: ", idades[0], "\n")
        escreva("Email: ", emails[0], "\n")
    }
}
