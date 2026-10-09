
programa
{
    // Verifica se o nome possui pelo menos 3 caracteres
    funcao logico validar_nome(cadeia nome)
    {
        retorne tamanho(nome) >= 3
    }

    // Verifica se a idade está no intervalo permitido
    funcao logico validar_idade(inteiro idade)
    {
        retorne idade >= 0 e idade <= 120
    }

    // Verifica se o e-mail contém @ e ponto
    funcao logico validar_email(cadeia email)
    {
        inteiro posicao_arroba = -1
        inteiro posicao_ponto = -1

        para (inteiro i = 0; i < tamanho(email); i++)
        {
            se (email[i] == '@')
            {
                posicao_arroba = i
            }

            se (email[i] == '.')
            {
                posicao_ponto = i
            }
        }

        retorne posicao_arroba > 0 e
                posicao_ponto > posicao_arroba + 1 e
                posicao_ponto < tamanho(email) - 1
    }

    funcao inicio()
    {
        cadeia nome = "Ana Silva"
        inteiro idade = 25
        cadeia email = "ana@gmail.com"

        escreva("=== CADASTRO DE CLIENTE ===\n")

        se (validar_nome(nome) e
            validar_idade(idade) e
            validar_email(email))
        {
            escreva("Cliente cadastrado com sucesso!\n")
            escreva("Nome: ", nome, "\n")
            escreva("Idade: ", idade, "\n")
            escreva("Email: ", email, "\n")
        }
        senao
        {
            escreva("Erro: Dados inválidos!\n")
        }

        // Testando uma idade inválida
        escreva("\n=== TESTE DE VALIDAÇÃO ===\n")

        inteiro nova_idade = -5

        se (validar_idade(nova_idade))
        {
            idade = nova_idade
        }
        senao
        {
            escreva("Erro: Idade inválida!\n")
        }

        escreva("Idade preservada: ", idade, "\n")
    }
}
