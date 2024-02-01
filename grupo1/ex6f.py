def contar_espacos_vogais(frase):
    # (a) Contar espaços em branco
    qtd_espacos = frase.count(' ')

    print(f"(a) Quantidade de espaços em branco: {qtd_espacos}")

    # (b) Contar frequência qtas vezes aparece cada vogal
    frequencia_vogais = {
        'a': frase.count('a'),
        'e': frase.count('e'),
        'i': frase.count('i'),
        'o': frase.count('o'),
        'u': frase.count('u')
    }

    print("(b) Frequência das vogais:")
    for vogal, frequencia in frequencia_vogais.items():
        print(f"{vogal}: {frequencia}")

# Exemplo de uso
frase_exemplo = "a"

contar_espacos_vogais(frase_exemplo)
