def contar_espacos_vogais(frase):
    # (a) Contar espaços em branco
    qtd_espacos = frase.count(' ')

    print(f"(a) Quantidade de espaços em branco: {qtd_espacos}")

    # (b) Contar frequência das vogais a, e, i, o, u
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
frase_exemplo = "Dada uma string, conte: (a) quantos espaços em branco existem na frase. (b) quantas vezes aparecem as vogais a, e, i, o, u."

contar_espacos_vogais(frase_exemplo)
